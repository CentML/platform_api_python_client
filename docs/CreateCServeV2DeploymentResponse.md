# CreateCServeV2DeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**created_at** | **datetime** |  | 
**endpoint_url** | **str** |  | 

## Example

```python
from platform_api_python_client.models.create_c_serve_v2_deployment_response import CreateCServeV2DeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCServeV2DeploymentResponse from a JSON string
create_c_serve_v2_deployment_response_instance = CreateCServeV2DeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(CreateCServeV2DeploymentResponse.to_json())

# convert the object into a dict
create_c_serve_v2_deployment_response_dict = create_c_serve_v2_deployment_response_instance.to_dict()
# create an instance of CreateCServeV2DeploymentResponse from a dict
create_c_serve_v2_deployment_response_from_dict = CreateCServeV2DeploymentResponse.from_dict(create_c_serve_v2_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


