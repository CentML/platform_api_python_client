# CreateInferenceDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**created_at** | **datetime** |  | 
**endpoint_url** | **str** |  | 

## Example

```python
from platform_api_client.models.create_inference_deployment_response import CreateInferenceDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInferenceDeploymentResponse from a JSON string
create_inference_deployment_response_instance = CreateInferenceDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print CreateInferenceDeploymentResponse.to_json()

# convert the object into a dict
create_inference_deployment_response_dict = create_inference_deployment_response_instance.to_dict()
# create an instance of CreateInferenceDeploymentResponse from a dict
create_inference_deployment_response_form_dict = create_inference_deployment_response.from_dict(create_inference_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


