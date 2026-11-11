# UnifiedWriteJobDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**user_annotations** | **Dict[str, str]** |  | [optional] 
**chart_revision** | **str** |  | [optional] 
**volume_mounts** | [**List[VolumeMount]**](VolumeMount.md) |  | [optional] 
**priority** | **str** |  | [optional] 
**pools** | [**CclMainPools**](CclMainPools.md) |  | 
**env** | [**Env**](Env.md) |  | [optional] 
**image** | [**Image**](Image.md) |  | 
**command** | **str** |  | [optional] 
**config_file** | [**ConfigFileMount**](ConfigFileMount.md) |  | [optional] 
**completions** | **int** |  | [optional] [default to 1]
**parallelism** | **int** |  | [optional] [default to 1]
**backoff_limit** | **int** |  | [optional] [default to 3]
**active_deadline_seconds** | **int** |  | [optional] 
**enable_logging** | **bool** |  | [optional] [default to True]

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


