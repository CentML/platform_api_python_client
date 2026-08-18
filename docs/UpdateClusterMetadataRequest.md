# UpdateClusterMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_creation_disabled** | **bool** |  | 

## Example

```python
from platform_api_python_client.models.update_cluster_metadata_request import UpdateClusterMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClusterMetadataRequest from a JSON string
update_cluster_metadata_request_instance = UpdateClusterMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateClusterMetadataRequest.to_json())

# convert the object into a dict
update_cluster_metadata_request_dict = update_cluster_metadata_request_instance.to_dict()
# create an instance of UpdateClusterMetadataRequest from a dict
update_cluster_metadata_request_from_dict = UpdateClusterMetadataRequest.from_dict(update_cluster_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


