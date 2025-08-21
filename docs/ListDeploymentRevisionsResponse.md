# ListDeploymentRevisionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GetDeploymentRevisionResponse]**](GetDeploymentRevisionResponse.md) |  | 

## Example

```python
from platform_api_python_client.models.list_deployment_revisions_response import ListDeploymentRevisionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDeploymentRevisionsResponse from a JSON string
list_deployment_revisions_response_instance = ListDeploymentRevisionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListDeploymentRevisionsResponse.to_json())

# convert the object into a dict
list_deployment_revisions_response_dict = list_deployment_revisions_response_instance.to_dict()
# create an instance of ListDeploymentRevisionsResponse from a dict
list_deployment_revisions_response_from_dict = ListDeploymentRevisionsResponse.from_dict(list_deployment_revisions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


