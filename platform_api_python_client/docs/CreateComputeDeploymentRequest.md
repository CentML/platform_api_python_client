# CreateComputeDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**hardware_instance_id** | **int** |  | 
**image_url** | **str** |  | 
**enable_jupyter** | **bool** |  | [optional] [default to False]
**ssh_public_key** | **str** |  | [optional] 
**ssh_password** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.create_compute_deployment_request import CreateComputeDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateComputeDeploymentRequest from a JSON string
create_compute_deployment_request_instance = CreateComputeDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateComputeDeploymentRequest.to_json())

# convert the object into a dict
create_compute_deployment_request_dict = create_compute_deployment_request_instance.to_dict()
# create an instance of CreateComputeDeploymentRequest from a dict
create_compute_deployment_request_from_dict = CreateComputeDeploymentRequest.from_dict(create_compute_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


