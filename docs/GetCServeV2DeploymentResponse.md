# GetCServeV2DeploymentResponse


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
**min_scale** | **int** |  | 
**max_scale** | **int** |  | 
**endpoint_certificate_authority** | **str** |  | [optional] 
**concurrency** | **int** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 

## Example

```python
from platform_api_python_client.models.get_c_serve_v2_deployment_response import GetCServeV2DeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCServeV2DeploymentResponse from a JSON string
get_c_serve_v2_deployment_response_instance = GetCServeV2DeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(GetCServeV2DeploymentResponse.to_json())

# convert the object into a dict
get_c_serve_v2_deployment_response_dict = get_c_serve_v2_deployment_response_instance.to_dict()
# create an instance of GetCServeV2DeploymentResponse from a dict
get_c_serve_v2_deployment_response_from_dict = GetCServeV2DeploymentResponse.from_dict(get_c_serve_v2_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


