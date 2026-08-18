# GetDeploymentLogV4Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[DeploymentLogEventV4]**](DeploymentLogEventV4.md) | Log events, oldest first. Page boundaries are minted client-side from the events&#39; timestamp field (see the endpoint description): an empty fetch_newer&#x3D;false page means history is exhausted; an empty fetch_newer&#x3D;true page means nothing new yet. | 

## Example

```python
from platform_api_python_client.models.get_deployment_log_v4_response import GetDeploymentLogV4Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeploymentLogV4Response from a JSON string
get_deployment_log_v4_response_instance = GetDeploymentLogV4Response.from_json(json)
# print the JSON string representation of the object
print(GetDeploymentLogV4Response.to_json())

# convert the object into a dict
get_deployment_log_v4_response_dict = get_deployment_log_v4_response_instance.to_dict()
# create an instance of GetDeploymentLogV4Response from a dict
get_deployment_log_v4_response_from_dict = GetDeploymentLogV4Response.from_dict(get_deployment_log_v4_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


