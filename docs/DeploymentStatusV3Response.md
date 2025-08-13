# DeploymentStatusV3Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**type** | [**DeploymentType**](DeploymentType.md) |  | 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 
**rollout_status** | [**RolloutStatus**](RolloutStatus.md) |  | [optional] 
**endpoint_url** | **str** |  | [optional] 
**revision_pod_details_list** | [**List[RevisionPodDetails]**](RevisionPodDetails.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.deployment_status_v3_response import DeploymentStatusV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStatusV3Response from a JSON string
deployment_status_v3_response_instance = DeploymentStatusV3Response.from_json(json)
# print the JSON string representation of the object
print(DeploymentStatusV3Response.to_json())

# convert the object into a dict
deployment_status_v3_response_dict = deployment_status_v3_response_instance.to_dict()
# create an instance of DeploymentStatusV3Response from a dict
deployment_status_v3_response_from_dict = DeploymentStatusV3Response.from_dict(deployment_status_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


