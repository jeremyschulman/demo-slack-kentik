from os import getenv

from httpx import AsyncClient

__all__ = ['KentikClient']


class KentikClient(AsyncClient):
    KENTIK_BASE_URL = 'https://api.kentik.com/api/v5'

    def __init__(self, *vargs, **kwargs):
        kt_auth_email = kwargs.pop('kentik_auth_email', getenv('KT_AUTH_EMAIL'))
        kt_auth_token = kwargs.pop('kentik_auth_token', getenv('KT_AUTH_TOKEN'))

        if not all((kt_auth_email, kt_auth_token)):
            raise RuntimeError(f"Missing Kentik authentication setting")

        kwargs.setdefault('base_url', self.KENTIK_BASE_URL)
        super(KentikClient, self).__init__(*vargs, **kwargs)
        self.headers['X-CH-Auth-Email'] = kt_auth_email
        self.headers['X-CH-Auth-API-Token'] = kt_auth_token

    async def fetch_chart_data(self, payload: dict) -> dict:
        res = await self.post('/query/topXdata', json=payload)
        res.raise_for_status()
        return res.json()
