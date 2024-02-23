# CreateInferenceDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**image_url** | **str** |  | 
**hardware_instance_id** | **int** |  | 
**env_vars** | **Dict[str, str]** |  | [optional] 
**secrets** | [**AuthSecret**](AuthSecret.md) |  | [optional] 
**port** | **int** |  | 
**min_replicas** | **int** |  | 
**max_replicas** | **int** |  | 
**timeout** | **int** |  | [optional] 
**healthcheck** | **str** |  | [optional] 

## Example

```python
from platform_api_client.models.create_inference_deployment_request import CreateInferenceDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInferenceDeploymentRequest from a JSON string
create_inference_deployment_request_instance = CreateInferenceDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print CreateInferenceDeploymentRequest.to_json()

# convert the object into a dict
create_inference_deployment_request_dict = create_inference_deployment_request_instance.to_dict()
# create an instance of CreateInferenceDeploymentRequest from a dict
create_inference_deployment_request_form_dict = create_inference_deployment_request.from_dict(create_inference_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


