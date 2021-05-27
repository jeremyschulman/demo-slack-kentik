# -----------------------------------------------------------------------------
# Public Imports
# -----------------------------------------------------------------------------
import asyncio

from httpx import AsyncClient, Response
import click
from slack_bolt.request.async_request import AsyncBoltRequest as Request
from slack_click import SlackClickGroup, version_option
from slack_sdk.models.blocks import ImageBlock, PlainTextObject

from tenacity import retry, wait_exponential

# -----------------------------------------------------------------------------
# Private Imports
# -----------------------------------------------------------------------------

from .app_data import slack_commands
from . import query_1, query_2, query_3

# The Kentik Fotomat URL is routing through ngrok since I am using this on my
# laptop for dev-testing. YMMV.

FOTOMAT_URL = 'https://fotomat.ngrok.io'

# -----------------------------------------------------------------------------
#                                 CLI CODE BEGINS
# -----------------------------------------------------------------------------


@slack_commands.register()
@click.group(name="/fotomat", cls=SlackClickGroup)
@version_option(version="0.1.0")
@click.pass_obj
async def cli_fotomat_group(obj: dict):
    """
    This is the Kentik fotomat command.
    """
    request: Request = obj["request"]
    say = request.context["say"]
    await say(f"`{cli_fotomat_group.name}` command invoked without any commands or options.")


@cli_fotomat_group.command("debug-foto")
@click.pass_obj
async def cli_query_1(obj: dict):
    request: Request = obj["request"]
    say = request.context["say"]
    res = await say(f'Requesting debug photo from Kentik Fotomat')
    thread_ts = res.data['ts']
    await request_foto(say, thread_ts, query_1.payload)


@cli_fotomat_group.command("mcast-foto")
@click.option(
    '--ipaddr', help='source IP address', required=True
)
@click.pass_obj
async def cli_query_2(obj: dict, ipaddr: str):
    request: Request = obj["request"]
    say = request.context["say"]
    res = await say(f'Requesting multicast photo from Kentik Fotomat')
    thread_ts = res.data['ts']
    payload = query_2.payload
    p_filters = payload['api_query']['queries'][0]['query']['filters']
    p_filters['filterGroups'][0]['filters'][0]['filterValue'] = ipaddr + "/32"
    await request_foto(say, thread_ts, query_2.payload)


@cli_fotomat_group.command("sp-foto")
@click.option(
    '--site', help='SP site name',
    type=click.Choice(['kentiksp.ORD1', 'kentiksp.ORD2', 'kentiksp.NYC1', 'kentiksp.SFO1']),
    required=True, metavar='SITE'
)
@click.pass_obj
async def cli_query_2(obj: dict, site: str):
    request: Request = obj["request"]
    say = request.context["say"]
    res = await say(f'Requesting SP site *{site}* photo from Kentik Fotomat')
    thread_ts = res.data['ts']
    payload = query_3.payload
    p_filters = payload['api_query']['queries'][0]['query']['filters']
    p_filters['filterGroups'][0]['filters'][0]['filterValue'] = site
    await request_foto(say, thread_ts, query_3.payload)


# -----------------------------------------------------------------------------
#                            Task Processing Code
# -----------------------------------------------------------------------------

async def request_foto(say, thread_ts, payload):
    async with AsyncClient(base_url=FOTOMAT_URL) as fotomat_api:
        fm_res = await fotomat_api.post('/requests', json=payload)
        fm_body = fm_res.json()
        fm_id = fm_body['id']
        print(fm_id)

    await say(f'Fotomat pickup ID is: `{fm_id}`', thread_ts=thread_ts)
    asyncio.create_task(pickup_foto(say, thread_ts, image_id=fm_id))


async def pickup_foto(say, thread_ts, image_id):
    image_url = f'/image/{image_id}'

    await say('Waiting for image ... ', thread_ts=thread_ts)

    async with AsyncClient(base_url=FOTOMAT_URL) as f_api:

        @retry(wait=wait_exponential(min=4, max=30))
        async def await_foto():
            res: Response = await f_api.get(image_url)
            assert not res.is_error

        await await_foto()

    image_url = f"{FOTOMAT_URL}{image_url}"
    print(image_url)

    await say(f'Pickup ID `{image_id}`', thread_ts=thread_ts, blocks=[
        ImageBlock(
            title=PlainTextObject(text='Photo-1'),
            image_url=image_url,
            alt_text='photo-1'
        )
    ])
