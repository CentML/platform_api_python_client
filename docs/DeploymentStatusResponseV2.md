# DeploymentStatusResponseV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**type** | [**DeploymentType**](DeploymentType.md) |  | 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 
**service_status** | [**HealthStatus**](HealthStatus.md) |  | 
**error_message** | **str** |  | 
**endpoint_url** | **str** |  | 

## Example

```python
from platform_api_python_client.models.deployment_status_response_v2 import DeploymentStatusResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStatusResponseV2 from a JSON string
deployment_status_response_v2_instance = DeploymentStatusResponseV2.from_json(json)
# print the JSON string representation of the object
print(DeploymentStatusResponseV2.to_json())

# convert the object into a dict
deployment_status_response_v2_dict = deployment_status_response_v2_instance.to_dict()
# create an instance of DeploymentStatusResponseV2 from a dict
deployment_status_response_v2_from_dict = DeploymentStatusResponseV2.from_dict(deployment_status_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


