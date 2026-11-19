# UpdateClusterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**components** | [**ClusterBaseComponents**](ClusterBaseComponents.md) |  | 

## Example

```python
from platform_api_python_client.models.update_cluster_request import UpdateClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClusterRequest from a JSON string
update_cluster_request_instance = UpdateClusterRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateClusterRequest.to_json())

# convert the object into a dict
update_cluster_request_dict = update_cluster_request_instance.to_dict()
# create an instance of UpdateClusterRequest from a dict
update_cluster_request_from_dict = UpdateClusterRequest.from_dict(update_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


