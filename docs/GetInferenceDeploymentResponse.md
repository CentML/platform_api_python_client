# GetInferenceDeploymentResponse


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
**container_port** | **int** |  | 
**min_scale** | **int** |  | 
**max_scale** | **int** |  | 
**concurrency** | **int** |  | 
**healthcheck** | **str** |  | 
**endpoint_certificate_authority** | **str** |  | 
**env_vars** | **Dict[str, str]** |  | 
**command** | **List[str]** |  | 
**command_args** | **List[str]** |  | 

## Example

```python
from platform_api_external_client.models.get_inference_deployment_response import GetInferenceDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInferenceDeploymentResponse from a JSON string
get_inference_deployment_response_instance = GetInferenceDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(GetInferenceDeploymentResponse.to_json())

# convert the object into a dict
get_inference_deployment_response_dict = get_inference_deployment_response_instance.to_dict()
# create an instance of GetInferenceDeploymentResponse from a dict
get_inference_deployment_response_from_dict = GetInferenceDeploymentResponse.from_dict(get_inference_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


