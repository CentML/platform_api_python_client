# ClusterCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **str** |  | 
**bearer_token** | **str** |  | 
**ca_cert** | **str** |  | 

## Example

```python
from platform_api_python_client.models.cluster_credential import ClusterCredential

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCredential from a JSON string
cluster_credential_instance = ClusterCredential.from_json(json)
# print the JSON string representation of the object
print(ClusterCredential.to_json())

# convert the object into a dict
cluster_credential_dict = cluster_credential_instance.to_dict()
# create an instance of ClusterCredential from a dict
cluster_credential_from_dict = ClusterCredential.from_dict(cluster_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


