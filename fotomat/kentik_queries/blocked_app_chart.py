import json
from pathlib import Path
from copy import deepcopy

_heredir = Path(__file__).parent
_api_payload = json.load(_heredir.joinpath("blocked_app_chart.json").open())


def blocked_app_chart_payload(app_name: str):
    payload = deepcopy(_api_payload)
    payload["queries"][0]["query"]["filters"]["filterGroups"][0]["filters"][0][
        "filterValue"
    ] = app_name
    return payload
