# -----------------------------------------------------------------------------
# System Imports
# -----------------------------------------------------------------------------

from typing import List

# -----------------------------------------------------------------------------
# Private Imports
# -----------------------------------------------------------------------------

from ..kentik import KentikClient

# -----------------------------------------------------------------------------
# Exports
# -----------------------------------------------------------------------------

__all__ = ["kt_find_blocked_apps"]


# -----------------------------------------------------------------------------
#
#                                  CODE BEGINS
#
# -----------------------------------------------------------------------------


async def kt_find_blocked_apps() -> List[str]:
    kt: KentikClient

    async with KentikClient() as kt:
        res = await kt.fetch_chart_data(api_payload)

    body = res["results"][0]["data"]
    app_names = [rec["kt_aws_src_vm_name"] for rec in body]
    return app_names


api_payload = {
    "queries": [
        {
            "bucket": "Left +Y Axis",
            "isOverlay": False,
            "query": {
                "all_devices": False,
                "aggregateTypes": [
                    "avg_bits_per_sec",
                    "p95th_bits_per_sec",
                    "max_bits_per_sec",
                ],
                "aggregateThresholds": {
                    "avg_bits_per_sec": 0,
                    "p95th_bits_per_sec": 0,
                    "max_bits_per_sec": 0,
                },
                "bracketOptions": "",
                "hideCidr": False,
                "cidr": 32,
                "cidr6": 128,
                "customAsGroups": True,
                "cutFn": {},
                "cutFnRegex": {},
                "cutFnSelector": {},
                "depth": 75,
                "descriptor": "",
                "device_name": [],
                "device_labels": [],
                "device_sites": [],
                "device_types": ["aws_subnet"],
                "fastData": "Auto",
                "filterDimensionsEnabled": False,
                "filterDimensionName": "Total",
                "filterDimensionOther": False,
                "filterDimensionSort": False,
                "filterDimensions": {},
                "aggregateFiltersEnabled": False,
                "aggregateFiltersDimensionLabel": "",
                "aggregateFilters": [],
                "hostname_lookup": True,
                "isOverlay": False,
                "lookback_seconds": 3600,
                "from_to_lookback": 3600,
                "generatorDimensions": [],
                "generatorPanelMinHeight": 250,
                "generatorMode": False,
                "generatorColumns": 1,
                "generatorQueryTitle": "{{generator_series_name}}",
                "generatorTopx": 8,
                "matrixBy": [],
                "metric": ["bytes"],
                "forceMinsPolling": False,
                "mirror": False,
                "mirrorUnits": True,
                "outsort": "avg_bits_per_sec",
                "overlay_day": -7,
                "overlay_timestamp_adjust": False,
                "query_title": "",
                "secondaryOutsort": "",
                "secondaryTopxSeparate": False,
                "secondaryTopxMirrored": False,
                "show_overlay": True,
                "show_total_overlay": True,
                "starting_time": None,
                "ending_time": None,
                "sync_all_axes": False,
                "sync_axes": False,
                "sync_extents": True,
                "show_site_markers": False,
                "topx": 8,
                "update_frequency": 0,
                "use_log_axis": False,
                "use_secondary_log_axis": False,
                "viz_type": "stackedArea",
                "aggregates": [
                    {
                        "value": "avg_bits_per_sec",
                        "column": "f_sum_both_bytes",
                        "fn": "average",
                        "label": "Bits/s Sampled at Ingress + Egress Average",
                        "unit": "bytes",
                        "group": "Bits/s Sampled at Ingress + Egress",
                        "origLabel": "Average",
                        "sample_rate": 1,
                        "raw": True,
                        "name": "avg_bits_per_sec",
                    },
                    {
                        "value": "p95th_bits_per_sec",
                        "column": "f_sum_both_bytes",
                        "fn": "percentile",
                        "label": "Bits/s Sampled at Ingress + Egress 95th Percentile",
                        "rank": 95,
                        "unit": "bytes",
                        "group": "Bits/s Sampled at Ingress + Egress",
                        "origLabel": "95th Percentile",
                        "sample_rate": 1,
                        "name": "p95th_bits_per_sec",
                    },
                    {
                        "value": "max_bits_per_sec",
                        "column": "f_sum_both_bytes",
                        "fn": "max",
                        "label": "Bits/s Sampled at Ingress + Egress Max",
                        "unit": "bytes",
                        "group": "Bits/s Sampled at Ingress + Egress",
                        "origLabel": "Max",
                        "sample_rate": 1,
                        "name": "max_bits_per_sec",
                    },
                ],
                "filters": {
                    "connector": "All",
                    "filterGroups": [
                        {
                            "name": "",
                            "named": False,
                            "connector": "All",
                            "not": False,
                            "autoAdded": "",
                            "filters": [
                                {
                                    "filterField": "kt_aws_action",
                                    "operator": "=",
                                    "filterValue": "REJECT",
                                },
                                {
                                    "filterField": "kt_aws_src_vm_name",
                                    "operator": "<>",
                                    "filterValue": "",
                                },
                            ],
                            "saved_filters": [],
                            "filterGroups": [],
                        }
                    ],
                },
                "dimension": ["kt_aws_src_vm_name"],
            },
        }
    ]
}
