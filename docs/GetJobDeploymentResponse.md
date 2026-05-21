# GetJobDeploymentResponse


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
**user_annotations** | **Dict[str, str]** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**command** | **List[str]** |  | [optional] 
**args** | **List[str]** |  | [optional] 
**original_command** | **str** |  | [optional] 
**completions** | **int** |  | [optional] [default to 1]
**parallelism** | **int** |  | [optional] [default to 1]
**image_pull_secret_credentials** | [**ImagePullSecretCredentials**](ImagePullSecretCredentials.md) |  | [optional] 
**enable_logging** | **bool** |  | [optional] [default to True]

## Example

```python
from platform_api_python_client.models.get_job_deployment_response import GetJobDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetJobDeploymentResponse from a JSON string
get_job_deployment_response_instance = GetJobDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(GetJobDeploymentResponse.to_json())

# convert the object into a dict
get_job_deployment_response_dict = get_job_deployment_response_instance.to_dict()
# create an instance of GetJobDeploymentResponse from a dict
get_job_deployment_response_from_dict = GetJobDeploymentResponse.from_dict(get_job_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


