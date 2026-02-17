# GetInferenceV3DeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator_email** | **str** |  | 
**cluster_id** | **int** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**endpoint_url** | **str** |  | 
**image_url** | **str** |  | [optional] 
**type** | [**DeploymentType**](DeploymentType.md) |  | 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 
**created_at** | **datetime** |  | 
**hardware_instance_id** | **int** |  | 
**revision_number** | **int** |  | 
**container_port** | **int** |  | 
**min_replicas** | **int** |  | 
**max_replicas** | **int** |  | 
**initial_replicas** | **int** |  | [optional] 
**concurrency** | **int** |  | [optional] 
**healthcheck** | **str** |  | [optional] 
**endpoint_certificate_authority** | **str** |  | [optional] 
**endpoint_bearer_token** | **str** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**command** | **List[str]** |  | [optional] 
**command_args** | **List[str]** |  | [optional] 
**original_command** | **str** |  | [optional] 
**image_pull_secret_credentials** | [**ImagePullSecretCredentials**](ImagePullSecretCredentials.md) |  | [optional] 
**backend_protocol** | [**BackendProtocol**](BackendProtocol.md) |  | [optional] 
**enable_logging** | **bool** |  | [optional] [default to True]

## Example

```python
from platform_api_python_client.models.get_inference_v3_deployment_response import GetInferenceV3DeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInferenceV3DeploymentResponse from a JSON string
get_inference_v3_deployment_response_instance = GetInferenceV3DeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(GetInferenceV3DeploymentResponse.to_json())

# convert the object into a dict
get_inference_v3_deployment_response_dict = get_inference_v3_deployment_response_instance.to_dict()
# create an instance of GetInferenceV3DeploymentResponse from a dict
get_inference_v3_deployment_response_from_dict = GetInferenceV3DeploymentResponse.from_dict(get_inference_v3_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


