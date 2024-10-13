# GetClusterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**display_name** | **str** |  | 

## Example

```python
from platform_api_python_client.models.get_cluster_response import GetClusterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClusterResponse from a JSON string
get_cluster_response_instance = GetClusterResponse.from_json(json)
# print the JSON string representation of the object
print(GetClusterResponse.to_json())

# convert the object into a dict
get_cluster_response_dict = get_cluster_response_instance.to_dict()
# create an instance of GetClusterResponse from a dict
get_cluster_response_from_dict = GetClusterResponse.from_dict(get_cluster_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


