# GetDeploymentLogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **List[object]** |  | 
**next_page_token** | **str** |  | 

## Example

```python
from platform_api_python_client.models.get_deployment_log_response import GetDeploymentLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeploymentLogResponse from a JSON string
get_deployment_log_response_instance = GetDeploymentLogResponse.from_json(json)
# print the JSON string representation of the object
print(GetDeploymentLogResponse.to_json())

# convert the object into a dict
get_deployment_log_response_dict = get_deployment_log_response_instance.to_dict()
# create an instance of GetDeploymentLogResponse from a dict
get_deployment_log_response_from_dict = GetDeploymentLogResponse.from_dict(get_deployment_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


