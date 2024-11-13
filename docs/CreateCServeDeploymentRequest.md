# CreateCServeDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**hardware_instance_id** | **int** |  | 
**recipe** | [**CServeRecipeInput**](CServeRecipeInput.md) |  | 
**hf_token** | **str** |  | 
**endpoint_certificate_authority** | **str** |  | [optional] 
**min_scale** | **int** |  | 
**max_scale** | **int** |  | 
**concurrency** | **int** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 

## Example

```python
from platform_api_external_client.models.create_c_serve_deployment_request import CreateCServeDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCServeDeploymentRequest from a JSON string
create_c_serve_deployment_request_instance = CreateCServeDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCServeDeploymentRequest.to_json())

# convert the object into a dict
create_c_serve_deployment_request_dict = create_c_serve_deployment_request_instance.to_dict()
# create an instance of CreateCServeDeploymentRequest from a dict
create_c_serve_deployment_request_from_dict = CreateCServeDeploymentRequest.from_dict(create_c_serve_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


