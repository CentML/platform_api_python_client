# ListClusterCapacityResponse

All accessible clusters' GPU capacity, returned by ``GET /capacity``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ClusterCapacityResponse]**](ClusterCapacityResponse.md) |  | 

## Example

```python
from platform_api_python_client.models.list_cluster_capacity_response import ListClusterCapacityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListClusterCapacityResponse from a JSON string
list_cluster_capacity_response_instance = ListClusterCapacityResponse.from_json(json)
# print the JSON string representation of the object
print(ListClusterCapacityResponse.to_json())

# convert the object into a dict
list_cluster_capacity_response_dict = list_cluster_capacity_response_instance.to_dict()
# create an instance of ListClusterCapacityResponse from a dict
list_cluster_capacity_response_from_dict = ListClusterCapacityResponse.from_dict(list_cluster_capacity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


