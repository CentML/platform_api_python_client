# UnifiedGetDeploymentRolloutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paused** | **bool** |  | 
**status** | [**RolloutStatus**](RolloutStatus.md) |  | 

## Example

```python
from platform_api_python_client.models.unified_get_deployment_rollout_response import UnifiedGetDeploymentRolloutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedGetDeploymentRolloutResponse from a JSON string
unified_get_deployment_rollout_response_instance = UnifiedGetDeploymentRolloutResponse.from_json(json)
# print the JSON string representation of the object
print(UnifiedGetDeploymentRolloutResponse.to_json())

# convert the object into a dict
unified_get_deployment_rollout_response_dict = unified_get_deployment_rollout_response_instance.to_dict()
# create an instance of UnifiedGetDeploymentRolloutResponse from a dict
unified_get_deployment_rollout_response_from_dict = UnifiedGetDeploymentRolloutResponse.from_dict(unified_get_deployment_rollout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


