# UnifiedUpdateDeploymentRolloutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paused** | **bool** |  | 

## Example

```python
from platform_api_python_client.models.unified_update_deployment_rollout_request import UnifiedUpdateDeploymentRolloutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedUpdateDeploymentRolloutRequest from a JSON string
unified_update_deployment_rollout_request_instance = UnifiedUpdateDeploymentRolloutRequest.from_json(json)
# print the JSON string representation of the object
print(UnifiedUpdateDeploymentRolloutRequest.to_json())

# convert the object into a dict
unified_update_deployment_rollout_request_dict = unified_update_deployment_rollout_request_instance.to_dict()
# create an instance of UnifiedUpdateDeploymentRolloutRequest from a dict
unified_update_deployment_rollout_request_from_dict = UnifiedUpdateDeploymentRolloutRequest.from_dict(unified_update_deployment_rollout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


