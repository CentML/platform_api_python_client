# GetRagDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**endpoint_url** | **str** |  | 
**image_url** | **str** |  | [optional] 
**type** | [**DeploymentType**](DeploymentType.md) |  | 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 
**created_at** | **datetime** |  | 
**hardware_instance_id** | **int** |  | 
**recipe** | [**CServeV2Recipe**](CServeV2Recipe.md) |  | 
**llm_model** | **str** |  | 
**centml_api_key** | **str** |  | 
**min_scale** | **int** |  | [optional] [default to 1]
**max_scale** | **int** |  | [optional] [default to 1]
**initial_scale** | **int** |  | [optional] 
**endpoint_certificate_authority** | **str** |  | [optional] 
**concurrency** | **int** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 

## Example

```python
from platform_api_python_client.models.get_rag_deployment_response import GetRagDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRagDeploymentResponse from a JSON string
get_rag_deployment_response_instance = GetRagDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(GetRagDeploymentResponse.to_json())

# convert the object into a dict
get_rag_deployment_response_dict = get_rag_deployment_response_instance.to_dict()
# create an instance of GetRagDeploymentResponse from a dict
get_rag_deployment_response_from_dict = GetRagDeploymentResponse.from_dict(get_rag_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


