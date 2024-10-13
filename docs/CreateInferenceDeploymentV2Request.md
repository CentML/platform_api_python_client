# CreateInferenceDeploymentV2Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**hardware_instance_id** | **int** |  | 
**image_url** | **str** |  | 
**port** | **int** |  | 
**min_scale** | **int** |  | 
**max_scale** | **int** |  | 
**concurrency** | **int** |  | [optional] 
**healthcheck** | **str** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**command** | **List[str]** |  | [optional] 
**command_args** | **List[str]** |  | [optional] 
**endpoint_certificate_authority** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.create_inference_deployment_v2_request import CreateInferenceDeploymentV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInferenceDeploymentV2Request from a JSON string
create_inference_deployment_v2_request_instance = CreateInferenceDeploymentV2Request.from_json(json)
# print the JSON string representation of the object
print(CreateInferenceDeploymentV2Request.to_json())

# convert the object into a dict
create_inference_deployment_v2_request_dict = create_inference_deployment_v2_request_instance.to_dict()
# create an instance of CreateInferenceDeploymentV2Request from a dict
create_inference_deployment_v2_request_from_dict = CreateInferenceDeploymentV2Request.from_dict(create_inference_deployment_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


