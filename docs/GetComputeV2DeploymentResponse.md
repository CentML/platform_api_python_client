# GetComputeV2DeploymentResponse


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
from platform_api_python_client.models.get_compute_v2_deployment_response import GetComputeV2DeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetComputeV2DeploymentResponse from a JSON string
get_compute_v2_deployment_response_instance = GetComputeV2DeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(GetComputeV2DeploymentResponse.to_json())

# convert the object into a dict
get_compute_v2_deployment_response_dict = get_compute_v2_deployment_response_instance.to_dict()
# create an instance of GetComputeV2DeploymentResponse from a dict
get_compute_v2_deployment_response_from_dict = GetComputeV2DeploymentResponse.from_dict(get_compute_v2_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


