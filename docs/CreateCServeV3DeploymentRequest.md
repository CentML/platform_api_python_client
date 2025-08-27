# CreateCServeV3DeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_surge** | **int** |  | [optional] 
**max_unavailable** | **int** |  | [optional] 
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**hardware_instance_id** | **int** |  | 
**recipe** | [**CServeV2Recipe**](CServeV2Recipe.md) |  | 
**cserve_version** | **str** |  | [optional] 
**hf_token** | **str** |  | [optional] 
**endpoint_bearer_token** | **str** |  | [optional] 
**endpoint_certificate_authority** | **str** |  | [optional] 
**min_replicas** | **int** |  | 
**max_replicas** | **int** |  | 
**initial_replicas** | **int** |  | [optional] 
**concurrency** | **int** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 

## Example

```python
from platform_api_python_client.models.create_c_serve_v3_deployment_request import CreateCServeV3DeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCServeV3DeploymentRequest from a JSON string
create_c_serve_v3_deployment_request_instance = CreateCServeV3DeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCServeV3DeploymentRequest.to_json())

# convert the object into a dict
create_c_serve_v3_deployment_request_dict = create_c_serve_v3_deployment_request_instance.to_dict()
# create an instance of CreateCServeV3DeploymentRequest from a dict
create_c_serve_v3_deployment_request_from_dict = CreateCServeV3DeploymentRequest.from_dict(create_c_serve_v3_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


