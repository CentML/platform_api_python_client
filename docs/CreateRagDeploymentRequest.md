# CreateRagDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**hardware_instance_id** | **int** |  | 
**recipe** | [**CServeV2Recipe**](CServeV2Recipe.md) |  | 
**hf_token** | **str** |  | [optional] 
**llm_model** | **str** |  | 
**centml_api_key** | **str** |  | 
**min_scale** | **int** |  | [optional] [default to 1]
**max_scale** | **int** |  | [optional] [default to 1]
**initial_scale** | **int** |  | [optional] 
**endpoint_bearer_token** | **str** |  | [optional] 
**endpoint_certificate_authority** | **str** |  | [optional] 
**concurrency** | **int** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 

## Example

```python
from platform_api_python_client.models.create_rag_deployment_request import CreateRagDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRagDeploymentRequest from a JSON string
create_rag_deployment_request_instance = CreateRagDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRagDeploymentRequest.to_json())

# convert the object into a dict
create_rag_deployment_request_dict = create_rag_deployment_request_instance.to_dict()
# create an instance of CreateRagDeploymentRequest from a dict
create_rag_deployment_request_from_dict = CreateRagDeploymentRequest.from_dict(create_rag_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


