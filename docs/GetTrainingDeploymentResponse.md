# GetTrainingDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**image_url** | **str** |  | 
**type** | [**DeploymentType**](DeploymentType.md) |  | 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 
**created_at** | **datetime** |  | 
**hardware_instance_id** | **int** |  | 
**endpoint_url** | **str** |  | 
**env_vars** | **Dict[str, str]** |  | 
**secrets** | [**AuthSecret**](AuthSecret.md) |  | 

## Example

```python
from platform_api_client.models.get_training_deployment_response import GetTrainingDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTrainingDeploymentResponse from a JSON string
get_training_deployment_response_instance = GetTrainingDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print GetTrainingDeploymentResponse.to_json()

# convert the object into a dict
get_training_deployment_response_dict = get_training_deployment_response_instance.to_dict()
# create an instance of GetTrainingDeploymentResponse from a dict
get_training_deployment_response_form_dict = get_training_deployment_response.from_dict(get_training_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


