# CreateTrainingDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**created_at** | **datetime** |  | 
**endpoint_url** | **str** |  | 

## Example

```python
from platform_api_client.models.create_training_deployment_response import CreateTrainingDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTrainingDeploymentResponse from a JSON string
create_training_deployment_response_instance = CreateTrainingDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print CreateTrainingDeploymentResponse.to_json()

# convert the object into a dict
create_training_deployment_response_dict = create_training_deployment_response_instance.to_dict()
# create an instance of CreateTrainingDeploymentResponse from a dict
create_training_deployment_response_form_dict = create_training_deployment_response.from_dict(create_training_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


