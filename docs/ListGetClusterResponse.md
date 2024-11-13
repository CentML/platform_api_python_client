# ListGetClusterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GetClusterResponse]**](GetClusterResponse.md) |  | 

## Example

```python
from platform_api_external_client.models.list_get_cluster_response import ListGetClusterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListGetClusterResponse from a JSON string
list_get_cluster_response_instance = ListGetClusterResponse.from_json(json)
# print the JSON string representation of the object
print(ListGetClusterResponse.to_json())

# convert the object into a dict
list_get_cluster_response_dict = list_get_cluster_response_instance.to_dict()
# create an instance of ListGetClusterResponse from a dict
list_get_cluster_response_from_dict = ListGetClusterResponse.from_dict(list_get_cluster_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


