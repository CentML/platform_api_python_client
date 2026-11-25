# UnifiedUpdateDeploymentStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 

## Example

```python
from platform_api_python_client.models.unified_update_deployment_status_request import UnifiedUpdateDeploymentStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedUpdateDeploymentStatusRequest from a JSON string
unified_update_deployment_status_request_instance = UnifiedUpdateDeploymentStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UnifiedUpdateDeploymentStatusRequest.to_json())

# convert the object into a dict
unified_update_deployment_status_request_dict = unified_update_deployment_status_request_instance.to_dict()
# create an instance of UnifiedUpdateDeploymentStatusRequest from a dict
unified_update_deployment_status_request_from_dict = UnifiedUpdateDeploymentStatusRequest.from_dict(unified_update_deployment_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


