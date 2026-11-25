# UnifiedGetDeploymentStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**type** | [**DeploymentType**](DeploymentType.md) |  | 
**status** | [**DeploymentStatus**](DeploymentStatus.md) | The desired status, as stored. | 
**endpoint_url** | **str** |  | 
**applied** | **str** | Whether the latest apply, of the selected revision, is live: complete once the cluster runs it and every component is healthy; failed when the rollout cannot go on without a change; progressing otherwise, also when a component degrades after the rollout completed. Null when the deployment is not ACTIVE. | 
**message** | **str** | What the rollout waits on, or why it failed. | 
**components** | [**List[UnifiedComponentStatus]**](UnifiedComponentStatus.md) | The health of each released component&#39;s running objects. Empty when the deployment is not ACTIVE. | 

## Example

```python
from platform_api_python_client.models.unified_get_deployment_status_response import UnifiedGetDeploymentStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedGetDeploymentStatusResponse from a JSON string
unified_get_deployment_status_response_instance = UnifiedGetDeploymentStatusResponse.from_json(json)
# print the JSON string representation of the object
print(UnifiedGetDeploymentStatusResponse.to_json())

# convert the object into a dict
unified_get_deployment_status_response_dict = unified_get_deployment_status_response_instance.to_dict()
# create an instance of UnifiedGetDeploymentStatusResponse from a dict
unified_get_deployment_status_response_from_dict = UnifiedGetDeploymentStatusResponse.from_dict(unified_get_deployment_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


