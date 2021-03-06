# -----------------------------------------------------------------------------
# System Imports
# -----------------------------------------------------------------------------

import asyncio
from enum import Enum, auto

# -----------------------------------------------------------------------------
# Public Imports
# -----------------------------------------------------------------------------

import click

from slack_sdk.models.views import View
from slack_sdk.models.blocks import (
    SectionBlock,
    MarkdownTextObject as MText,
    PlainTextObject as PText,
    InputBlock,
    StaticSelectElement,
    Option,
)

from slack_sdk.web.async_slack_response import AsyncSlackResponse
from slack_bolt.request.async_request import AsyncBoltRequest
from slack_bolt.context.say.async_say import AsyncSay

# -----------------------------------------------------------------------------
# Private Imports
# -----------------------------------------------------------------------------

from fotomat import fotomat
from fotomat.app_data import app
from fotomat.cli.cloud import cli_cloud_app
from fotomat import kentik_queries


class AutoSlackIDs(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return last_values[0] + name

    def __repr__(self):
        return self.value


class _EventIDs(AutoSlackIDs):
    base = cli_cloud_app.event_id + ".blocked."
    view_id = auto()
    selectapp_id = auto()


_BE_PATIENT_ = (
    "This could take a few moments, please be patient ... :hourglass_flowing_sand:"
)

# -----------------------------------------------------------------------------
#
#                           /cloud app blocked?
#
# -----------------------------------------------------------------------------


@cli_cloud_app.command("blocked?")
@click.pass_obj
async def cli_cloud_app_blocked_cmd(request: AsyncBoltRequest):
    """
    Show apps blocked by firewall.
    """

    # Open a modal to let the User know we are looking for blocked applications
    # in the cloud.

    view = View(type="modal", title="Please Wait ...")
    view.blocks = [
        SectionBlock(
            text=MText(
                text=(
                    "Finding cloud applications that are being blocked by a firewall.\n\n"
                    f"{_BE_PATIENT_}"
                )
            )
        )
    ]

    client = request.context.client
    resp = await client.views_open(trigger_id=request.body["trigger_id"], view=view)

    # create a new task that will actually get the data from the Kentik portal.
    # ... TDODO

    asyncio.create_task(fetch_blocked_apps_from_kentik(req=request, res=resp))


async def fetch_blocked_apps_from_kentik(
    req: AsyncBoltRequest, res: AsyncSlackResponse
):
    orig_view = res.data["view"]
    view_id = orig_view["id"]

    app_names = await kentik_queries.kt_find_blocked_apps()
    if not app_names:
        # TODO: show that no apps are being blocked at this time
        pass

    view = View(type="modal", title="Select App")
    view.submit = PText(text="Execute")
    view.callback_id = _EventIDs.view_id

    option_apps = [Option(label=name, value=name) for name in app_names]

    ele = StaticSelectElement(
        placeholder="app ...", action_id=_EventIDs.selectapp_id, options=option_apps
    )

    view.blocks = [
        InputBlock(
            label="Please select an application from the drop-down",
            block_id=ele.action_id,
            element=ele,
        )
    ]

    client = req.context.client
    await client.views_update(view=view, view_id=view_id)


@app.view_submission(_EventIDs.view_id)
async def on_execute(context, say: AsyncSay, ack, view: dict):
    await ack()

    _id = _EventIDs.selectapp_id
    app_name = view["state"]["values"][_id][_id]["selected_option"]["value"]

    say.channel = context.user_id

    res = await say(
        f"Retrieving chart image.\n" f"*Name*: {app_name}\n\n" f"{_BE_PATIENT_}\n"
    )

    thread_ts = res["ts"]

    # now go fetch the chart image from the fotomat.
    payload = kentik_queries.blocked_app_chart_payload(app_name=app_name)
    await fotomat.request_foto(
        title=f"{app_name} traffic chart", say=say, thread_ts=thread_ts, payload=payload
    )

    # now go fetch the table image from the fotomat.
    payload = kentik_queries.blocked_app_table_payload(app_name=app_name)
    await fotomat.request_foto(
        title=f"{app_name} traffic table", say=say, thread_ts=thread_ts, payload=payload
    )
