# DeploymentStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 

## Example

```python
from platform_api_python_client.models.deployment_status_request import DeploymentStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStatusRequest from a JSON string
deployment_status_request_instance = DeploymentStatusRequest.from_json(json)
# print the JSON string representation of the object
print(DeploymentStatusRequest.to_json())

# convert the object into a dict
deployment_status_request_dict = deployment_status_request_instance.to_dict()
# create an instance of DeploymentStatusRequest from a dict
deployment_status_request_from_dict = DeploymentStatusRequest.from_dict(deployment_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


