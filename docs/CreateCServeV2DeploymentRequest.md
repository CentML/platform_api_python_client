# CreateCServeV2DeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**hardware_instance_id** | **int** |  | 
**recipe** | [**CServeV2Recipe**](CServeV2Recipe.md) |  | 
**hf_token** | **str** |  | [optional] 
**endpoint_bearer_token** | **str** |  | [optional] 
**endpoint_certificate_authority** | **str** |  | [optional] 
**min_scale** | **int** |  | 
**max_scale** | **int** |  | 
**initial_scale** | **int** |  | [optional] 
**concurrency** | **int** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 

## Example

```python
from platform_api_python_client.models.create_c_serve_v2_deployment_request import CreateCServeV2DeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCServeV2DeploymentRequest from a JSON string
create_c_serve_v2_deployment_request_instance = CreateCServeV2DeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCServeV2DeploymentRequest.to_json())

# convert the object into a dict
create_c_serve_v2_deployment_request_dict = create_c_serve_v2_deployment_request_instance.to_dict()
# create an instance of CreateCServeV2DeploymentRequest from a dict
create_c_serve_v2_deployment_request_from_dict = CreateCServeV2DeploymentRequest.from_dict(create_c_serve_v2_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


