# CreateJobDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**hardware_instance_id** | **int** |  | 
**user_annotations** | **Dict[str, str]** |  | [optional] 
**image_url** | **str** |  | 
**image_pull_secret_credentials** | [**ImagePullSecretCredentials**](ImagePullSecretCredentials.md) |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**command** | **str** |  | [optional] 
**completions** | **int** |  | [optional] [default to 1]
**parallelism** | **int** |  | [optional] [default to 1]
**backoff_limit** | **int** |  | [optional] [default to 3]
**active_deadline_seconds** | **int** |  | [optional] 
**enable_logging** | **bool** |  | [optional] [default to True]

## Example

```python
from platform_api_python_client.models.create_job_deployment_request import CreateJobDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJobDeploymentRequest from a JSON string
create_job_deployment_request_instance = CreateJobDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateJobDeploymentRequest.to_json())

# convert the object into a dict
create_job_deployment_request_dict = create_job_deployment_request_instance.to_dict()
# create an instance of CreateJobDeploymentRequest from a dict
create_job_deployment_request_from_dict = CreateJobDeploymentRequest.from_dict(create_job_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


