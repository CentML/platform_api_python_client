# UnifiedGetDeploymentUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[DeploymentUsage]**](DeploymentUsage.md) |  | 
**availability** | [**UsageAvailability**](UsageAvailability.md) |  | [optional] 
**last_sample_at** | **int** |  | [optional] 

## Example

```python
from platform_api_python_client.models.unified_get_deployment_usage_response import UnifiedGetDeploymentUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedGetDeploymentUsageResponse from a JSON string
unified_get_deployment_usage_response_instance = UnifiedGetDeploymentUsageResponse.from_json(json)
# print the JSON string representation of the object
print(UnifiedGetDeploymentUsageResponse.to_json())

# convert the object into a dict
unified_get_deployment_usage_response_dict = unified_get_deployment_usage_response_instance.to_dict()
# create an instance of UnifiedGetDeploymentUsageResponse from a dict
unified_get_deployment_usage_response_from_dict = UnifiedGetDeploymentUsageResponse.from_dict(unified_get_deployment_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


