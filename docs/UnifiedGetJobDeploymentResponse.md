# UnifiedGetJobDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 
**creator_email** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**revision_number** | **int** |  | 
**endpoint_url** | **str** |  | 
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
from platform_api_python_client.models.unified_get_job_deployment_response import UnifiedGetJobDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedGetJobDeploymentResponse from a JSON string
unified_get_job_deployment_response_instance = UnifiedGetJobDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(UnifiedGetJobDeploymentResponse.to_json())

# convert the object into a dict
unified_get_job_deployment_response_dict = unified_get_job_deployment_response_instance.to_dict()
# create an instance of UnifiedGetJobDeploymentResponse from a dict
unified_get_job_deployment_response_from_dict = UnifiedGetJobDeploymentResponse.from_dict(unified_get_job_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


