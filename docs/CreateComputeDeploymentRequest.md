# CreateComputeDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**image_url** | **str** |  | 
**hardware_instance_id** | **int** |  | 
**env_vars** | **Dict[str, str]** |  | [optional] 
**secrets** | [**AuthSecret**](AuthSecret.md) |  | [optional] 
**ssh_key** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from platform_api_client.models.create_compute_deployment_request import CreateComputeDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateComputeDeploymentRequest from a JSON string
create_compute_deployment_request_instance = CreateComputeDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print CreateComputeDeploymentRequest.to_json()

# convert the object into a dict
create_compute_deployment_request_dict = create_compute_deployment_request_instance.to_dict()
# create an instance of CreateComputeDeploymentRequest from a dict
create_compute_deployment_request_form_dict = create_compute_deployment_request.from_dict(create_compute_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


