# -----------------------------------------------------------------------------
# Public Imports
# -----------------------------------------------------------------------------

import click

from slack_bolt.request.async_request import AsyncBoltRequest
from slack_click.async_click import AsyncSlackClickGroup, version_option, click_async

# -----------------------------------------------------------------------------
# Private Imports
# -----------------------------------------------------------------------------

from fotomat.app_data import app

FOTOMAT_URL = "https://fotomat.ngrok.io"


# -----------------------------------------------------------------------------
#
#                Register the '/cloud' command with Click + Slacks
#
# -----------------------------------------------------------------------------


@click.group(name="/cloud", cls=AsyncSlackClickGroup)
@version_option(version="0.1.0")
@click_async
@click.pass_context
async def cli_slash_cloud(ctx: click.Context):
    """
    This is the top /cloud command; nothing here, other than
    to support the --help and --version commands.
    """
    request: AsyncBoltRequest = ctx.obj
    help_payload = cli_slash_cloud.slack_format_help(ctx)
    await request.context.say(help_payload)


@app.command(cli_slash_cloud.name)
async def on_cli_slash_cloud(request: AsyncBoltRequest, ack):
    await ack()
    return await cli_slash_cloud(prog_name=cli_slash_cloud.name, obj=request)


@cli_slash_cloud.group(name="vpn")
@click.pass_context
async def cli_cloud_vpn(ctx: click.Context):
    """
    Cloud VPN commands.
    """
    request: AsyncBoltRequest = ctx.obj
    help_payload = cli_cloud_vpn.slack_format_help(ctx)
    await request.context.say(help_payload)


# -----------------------------------------------------------------------------
#
#                            /cloud app blocked?
#
# -----------------------------------------------------------------------------


@cli_slash_cloud.group(name="app")
@click.pass_context
async def cli_cloud_app(ctx: click.Context):
    """
    Cloud application commands.
    """
    request: AsyncBoltRequest = ctx.obj
    help_payload = cli_cloud_app.slack_format_help(ctx)
    await request.context.say(help_payload)


@cli_cloud_app.command("chaos!")
async def cli_cloud_app_chaos():
    """
    Run chaos testing on cloud app.
    """
    pass


@cli_cloud_app.command("cost?")
async def cli_cloud_app_cost():
    """
    Report the current cost running an app.
    """
    pass
