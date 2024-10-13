# GetDeploymentV2Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**endpoint_url** | **str** |  | 
**image_url** | **str** |  | 
**type** | [**DeploymentType**](DeploymentType.md) |  | 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 
**created_at** | **datetime** |  | 
**hardware_instance_id** | **int** |  | 

## Example

```python
from platform_api_python_client.models.get_deployment_v2_response import GetDeploymentV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeploymentV2Response from a JSON string
get_deployment_v2_response_instance = GetDeploymentV2Response.from_json(json)
# print the JSON string representation of the object
print(GetDeploymentV2Response.to_json())

# convert the object into a dict
get_deployment_v2_response_dict = get_deployment_v2_response_instance.to_dict()
# create an instance of GetDeploymentV2Response from a dict
get_deployment_v2_response_from_dict = GetDeploymentV2Response.from_dict(get_deployment_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


