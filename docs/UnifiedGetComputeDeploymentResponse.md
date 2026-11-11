# UnifiedGetComputeDeploymentResponse


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
**ssh_public_key** | **str** |  | 
**enable_logging** | **bool** |  | [optional] [default to False]
**exposed_port** | **int** |  | 

## Example

```python
from platform_api_python_client.models.unified_get_compute_deployment_response import UnifiedGetComputeDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedGetComputeDeploymentResponse from a JSON string
unified_get_compute_deployment_response_instance = UnifiedGetComputeDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(UnifiedGetComputeDeploymentResponse.to_json())

# convert the object into a dict
unified_get_compute_deployment_response_dict = unified_get_compute_deployment_response_instance.to_dict()
# create an instance of UnifiedGetComputeDeploymentResponse from a dict
unified_get_compute_deployment_response_from_dict = UnifiedGetComputeDeploymentResponse.from_dict(unified_get_compute_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


