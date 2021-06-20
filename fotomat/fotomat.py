import asyncio

from httpx import AsyncClient, Response
from tenacity import retry, wait_exponential
from slack_sdk.models.blocks import ImageBlock, PlainTextObject


FOTOMAT_URL = "https://fotomat.ngrok.io"


async def request_foto(title: str, say, thread_ts, payload):

    foto_req = dict(api_query=dict(imageType="png", ttl=3600, **payload))

    async with AsyncClient(base_url=FOTOMAT_URL) as fotomat_api:
        fm_res = await fotomat_api.post("/requests", json=foto_req)
        fm_body = fm_res.json()
        fm_id = fm_body["id"]

    await say(f"Requesting {title} image ... ", thread_ts=thread_ts)

    # await say(f"Fotomat pickup ID is: `{fm_id}`", thread_ts=thread_ts)
    asyncio.create_task(pickup_foto(say, thread_ts, image_id=fm_id))


async def pickup_foto(say, thread_ts, image_id):
    image_url = f"/image/{image_id}"

    async with AsyncClient(base_url=FOTOMAT_URL) as f_api:

        @retry(wait=wait_exponential(min=4, max=30))
        async def await_foto():
            res: Response = await f_api.get(image_url)
            assert not res.is_error

        await await_foto()

    image_url = f"{FOTOMAT_URL}{image_url}"

    await say(
        f"Pickup ID `{image_id}`",
        thread_ts=thread_ts,
        blocks=[
            ImageBlock(
                title=PlainTextObject(text="Photo-1"),
                image_url=image_url,
                alt_text="photo-1",
            )
        ],
    )
