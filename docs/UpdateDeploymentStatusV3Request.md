# UpdateDeploymentStatusV3Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | [optional] 
**rollout_status** | [**RolloutStatus**](RolloutStatus.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.update_deployment_status_v3_request import UpdateDeploymentStatusV3Request

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDeploymentStatusV3Request from a JSON string
update_deployment_status_v3_request_instance = UpdateDeploymentStatusV3Request.from_json(json)
# print the JSON string representation of the object
print(UpdateDeploymentStatusV3Request.to_json())

# convert the object into a dict
update_deployment_status_v3_request_dict = update_deployment_status_v3_request_instance.to_dict()
# create an instance of UpdateDeploymentStatusV3Request from a dict
update_deployment_status_v3_request_from_dict = UpdateDeploymentStatusV3Request.from_dict(update_deployment_status_v3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


