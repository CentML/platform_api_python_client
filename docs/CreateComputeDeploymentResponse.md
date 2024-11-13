# CreateComputeDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**created_at** | **datetime** |  | 
**endpoint_url** | **str** |  | 
**port** | **int** |  | 

## Example

```python
from platform_api_external_client.models.create_compute_deployment_response import CreateComputeDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateComputeDeploymentResponse from a JSON string
create_compute_deployment_response_instance = CreateComputeDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(CreateComputeDeploymentResponse.to_json())

# convert the object into a dict
create_compute_deployment_response_dict = create_compute_deployment_response_instance.to_dict()
# create an instance of CreateComputeDeploymentResponse from a dict
create_compute_deployment_response_from_dict = CreateComputeDeploymentResponse.from_dict(create_compute_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


