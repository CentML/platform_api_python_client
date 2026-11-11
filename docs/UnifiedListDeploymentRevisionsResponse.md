# UnifiedListDeploymentRevisionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[UnifiedGetDeploymentRevisionResponse]**](UnifiedGetDeploymentRevisionResponse.md) |  | 

## Example

```python
from platform_api_python_client.models.unified_list_deployment_revisions_response import UnifiedListDeploymentRevisionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedListDeploymentRevisionsResponse from a JSON string
unified_list_deployment_revisions_response_instance = UnifiedListDeploymentRevisionsResponse.from_json(json)
# print the JSON string representation of the object
print(UnifiedListDeploymentRevisionsResponse.to_json())

# convert the object into a dict
unified_list_deployment_revisions_response_dict = unified_list_deployment_revisions_response_instance.to_dict()
# create an instance of UnifiedListDeploymentRevisionsResponse from a dict
unified_list_deployment_revisions_response_from_dict = UnifiedListDeploymentRevisionsResponse.from_dict(unified_list_deployment_revisions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


