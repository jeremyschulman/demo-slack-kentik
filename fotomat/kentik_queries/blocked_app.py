# -----------------------------------------------------------------------------
# System Imports
# -----------------------------------------------------------------------------

from typing import List
import json
from pathlib import Path
from copy import deepcopy

# -----------------------------------------------------------------------------
# Private Imports
# -----------------------------------------------------------------------------


from fotomat.kentik import KentikClient

# -----------------------------------------------------------------------------
# Exports
# -----------------------------------------------------------------------------

__all__ = [
    "kt_find_blocked_apps",
    "blocked_app_table_payload",
    "blocked_app_chart_payload",
]

# -----------------------------------------------------------------------------
# Private Data
# -----------------------------------------------------------------------------

_api_chart_payload = json.load(
    Path(__file__).parent.joinpath("blocked_app_chart.json").open()
)


_api_table_payload = json.load(
    Path(__file__).parent.joinpath("blocked_app_table.json").open()
)


_api_find_blocked_payload = json.load(
    Path(__file__).parent.joinpath("find_blocked_apps.json").open()
)

# -----------------------------------------------------------------------------
#
#                                  CODE BEGINS
#
# -----------------------------------------------------------------------------


async def kt_find_blocked_apps() -> List[str]:
    kt: KentikClient

    async with KentikClient() as kt:
        res = await kt.fetch_chart_data(_api_find_blocked_payload)

    body = res["results"][0]["data"]
    app_names = [rec["kt_aws_src_vm_name"] for rec in body]
    return app_names


def blocked_app_chart_payload(app_name: str):
    payload = deepcopy(_api_chart_payload)
    query = payload["queries"][0]["query"]

    query["query_title"] = f"{app_name} having blocked (REJECT) Traffic"

    query["filters"]["filterGroups"][0]["filters"][0]["filterValue"] = app_name

    return payload


def blocked_app_table_payload(app_name: str):
    payload = deepcopy(_api_table_payload)
    query = payload["queries"][0]["query"]

    query["query_title"] = f"{app_name} having blocked (REJECT) Traffic"

    query["filters"]["filterGroups"][0]["filters"][0]["filterValue"] = app_name

    return payload
