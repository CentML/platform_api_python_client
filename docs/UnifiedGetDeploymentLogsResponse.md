# UnifiedGetDeploymentLogsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[DeploymentLogEventV4]**](DeploymentLogEventV4.md) | Log events, oldest first. Page boundaries are minted client-side from the events&#39; timestamp field (see the endpoint description): an empty fetch_newer&#x3D;false page means history is exhausted; an empty fetch_newer&#x3D;true page means nothing new yet. | 

## Example

```python
from platform_api_python_client.models.unified_get_deployment_logs_response import UnifiedGetDeploymentLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedGetDeploymentLogsResponse from a JSON string
unified_get_deployment_logs_response_instance = UnifiedGetDeploymentLogsResponse.from_json(json)
# print the JSON string representation of the object
print(UnifiedGetDeploymentLogsResponse.to_json())

# convert the object into a dict
unified_get_deployment_logs_response_dict = unified_get_deployment_logs_response_instance.to_dict()
# create an instance of UnifiedGetDeploymentLogsResponse from a dict
unified_get_deployment_logs_response_from_dict = UnifiedGetDeploymentLogsResponse.from_dict(unified_get_deployment_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


