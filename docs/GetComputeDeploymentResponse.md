# GetComputeDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**endpoint_url** | **str** |  | 
**image_url** | **str** |  | 
**type** | [**DeploymentType**](DeploymentType.md) |  | 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 
**created_at** | **datetime** |  | 
**hardware_instance_id** | **int** |  | 
**exposed_port** | **int** |  | 
**ssh_public_key** | **str** |  | 
**ssh_password** | **str** |  | 
**env_vars** | **Dict[str, str]** |  | 

## Example

```python
from platform_api_external_client.models.get_compute_deployment_response import GetComputeDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetComputeDeploymentResponse from a JSON string
get_compute_deployment_response_instance = GetComputeDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(GetComputeDeploymentResponse.to_json())

# convert the object into a dict
get_compute_deployment_response_dict = get_compute_deployment_response_instance.to_dict()
# create an instance of GetComputeDeploymentResponse from a dict
get_compute_deployment_response_from_dict = GetComputeDeploymentResponse.from_dict(get_compute_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


