payload = {
    "api_query": {
        "imageType": "png",
        "ttl": 3600,
        "queries": [
            {
                "bucket": "Flow",
                "isOverlay": False,
                "query": {
                    "all_devices": True,
                    "aggregateTypes": [
                        "avg_bits_per_sec",
                        "p95th_bits_per_sec",
                        "max_bits_per_sec"
                    ],
                    "aggregateThresholds": {},
                    "bracketOptions": "",
                    "hideCidr": False,
                    "cidr": 32,
                    "cidr6": 128,
                    "customAsGroups": False,
                    "cutFn": {},
                    "cutFnRegex": {},
                    "cutFnSelector": {},
                    "depth": 75,
                    "descriptor": "",
                    "device_name": [],
                    "device_labels": [],
                    "device_sites": [],
                    "device_types": [],
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
                    "metric": [
                        "bytes"
                    ],
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
                    "viz_type": "sankey",
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
                            "name": "avg_bits_per_sec"
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
                            "name": "p95th_bits_per_sec"
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
                            "name": "max_bits_per_sec"
                        }
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
                                        "filterField": "inet_src_addr",
                                        "operator": "ILIKE",
                                        "filterValue": "example_IP_address/32"
                                    }
                                ],
                                "saved_filters": [],
                                "filterGroups": []
                            }
                        ]
                    },
                    "dimension": [
                        "i_device_site_name",
                        "InterfaceID_src",
                        "IP_src",
                        "IP_dst",
                        "InterfaceID_dst"
                    ]
                }
            }
        ]
    }
}
