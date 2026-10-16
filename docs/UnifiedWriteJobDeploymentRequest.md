# UnifiedWriteJobDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**hardware_instance_id** | **int** |  | 
**user_annotations** | **Dict[str, str]** |  | [optional] 
**chart_revision** | **str** |  | [optional] 
**volume_mounts** | [**List[VolumeMount]**](VolumeMount.md) |  | [optional] 
**priority** | **str** |  | [optional] 
**image_url** | **str** |  | 
**image_pull_secret_credentials** | [**ImagePullSecretCredentials**](ImagePullSecretCredentials.md) |  | [optional] 
**image_pull_ref** | **int** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**env_vars_refs** | **object** |  | [optional] 
**command** | **str** |  | [optional] 
**completions** | **int** |  | [optional] [default to 1]
**parallelism** | **int** |  | [optional] [default to 1]
**backoff_limit** | **int** |  | [optional] [default to 3]
**active_deadline_seconds** | **int** |  | [optional] 
**enable_logging** | **bool** |  | [optional] [default to True]
**config_file** | [**ConfigFileMount**](ConfigFileMount.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from platform_api_python_client.models.unified_write_job_deployment_request import UnifiedWriteJobDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedWriteJobDeploymentRequest from a JSON string
unified_write_job_deployment_request_instance = UnifiedWriteJobDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(UnifiedWriteJobDeploymentRequest.to_json())

# convert the object into a dict
unified_write_job_deployment_request_dict = unified_write_job_deployment_request_instance.to_dict()
# create an instance of UnifiedWriteJobDeploymentRequest from a dict
unified_write_job_deployment_request_from_dict = UnifiedWriteJobDeploymentRequest.from_dict(unified_write_job_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


