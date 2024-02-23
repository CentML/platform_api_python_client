# CreateTrainingDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**image_url** | **str** |  | 
**hardware_instance_id** | **int** |  | 
**env_vars** | **Dict[str, str]** |  | [optional] 
**secrets** | [**AuthSecret**](AuthSecret.md) |  | [optional] 

## Example

```python
from platform_api_client.models.create_training_deployment_request import CreateTrainingDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTrainingDeploymentRequest from a JSON string
create_training_deployment_request_instance = CreateTrainingDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print CreateTrainingDeploymentRequest.to_json()

# convert the object into a dict
create_training_deployment_request_dict = create_training_deployment_request_instance.to_dict()
# create an instance of CreateTrainingDeploymentRequest from a dict
create_training_deployment_request_form_dict = create_training_deployment_request.from_dict(create_training_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


