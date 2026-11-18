# DynamoFrontendConfig

Replica bounds for the Dynamo Frontend, shaped like a worker pool's so that Frontend autoscaling can arrive without an API change. Until it does, the Frontend runs a fixed count: ``min_replicas`` must equal ``max_replicas``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_replicas** | **int** |  | [optional] [default to 3]
**max_replicas** | **int** |  | [optional] [default to 3]

## Example

```python
from platform_api_python_client.models.dynamo_frontend_config import DynamoFrontendConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DynamoFrontendConfig from a JSON string
dynamo_frontend_config_instance = DynamoFrontendConfig.from_json(json)
# print the JSON string representation of the object
print(DynamoFrontendConfig.to_json())

# convert the object into a dict
dynamo_frontend_config_dict = dynamo_frontend_config_instance.to_dict()
# create an instance of DynamoFrontendConfig from a dict
dynamo_frontend_config_from_dict = DynamoFrontendConfig.from_dict(dynamo_frontend_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


