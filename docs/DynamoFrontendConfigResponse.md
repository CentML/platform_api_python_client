# DynamoFrontendConfigResponse

The Frontend a revision requests, as read back. The size bounds stay on the request: in a response they would make a client generated from an older spec reject deployments sized above its caps once the caps are raised. The replica bounds keep the shape this response already has.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_replicas** | **int** |  | [optional] [default to 3]
**max_replicas** | **int** |  | [optional] [default to 3]
**cpu** | **int** | CPU for each Frontend pod, in millicores. | [optional] 
**memory** | **int** | Memory for each Frontend pod, in MiB. | [optional] 

## Example

```python
from platform_api_python_client.models.dynamo_frontend_config_response import DynamoFrontendConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DynamoFrontendConfigResponse from a JSON string
dynamo_frontend_config_response_instance = DynamoFrontendConfigResponse.from_json(json)
# print the JSON string representation of the object
print(DynamoFrontendConfigResponse.to_json())

# convert the object into a dict
dynamo_frontend_config_response_dict = dynamo_frontend_config_response_instance.to_dict()
# create an instance of DynamoFrontendConfigResponse from a dict
dynamo_frontend_config_response_from_dict = DynamoFrontendConfigResponse.from_dict(dynamo_frontend_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


