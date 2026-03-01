import dlt
from dlt.sources.rest_api import rest_api_resources
from dlt.sources.rest_api.typing import RESTAPIConfig

@dlt.source
def taxi_rest_api_source():
    """REST API source for NYC taxi trip records."""
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api/",
        },
        "resource_defaults": {
            "endpoint": {
                "params": {"page_size": 1000},
                "data_selector": "$[*]",
                "paginator": {
                    "type": "page_number",
                    "page_param": "page",
                    "base_page": 1,
                    "total_path": None,
                    "stop_after_empty_page": True,
                },
            },
        },
        "resources": [
            {
                "name": "nyc_taxi",
                "endpoint": {"path": ""},
            },
        ],
    }
    yield from rest_api_resources(config)

pipeline = dlt.pipeline(
    pipeline_name="taxi_pipeline",
    destination="duckdb",
    dataset_name="taxi_data",
    progress="log",
)

if __name__ == "__main__":
    load_info = pipeline.run(taxi_rest_api_source())
    print(load_info)