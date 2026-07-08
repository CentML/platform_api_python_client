# ClusterRegistrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**storage_class** | **str** |  | 
**region** | **str** |  | [optional] 
**cloud_provider** | [**CloudProvider**](CloudProvider.md) |  | [optional] 
**credential** | [**ClusterCredential**](ClusterCredential.md) |  | 

## Example

```python
from platform_api_python_client.models.cluster_registration_request import ClusterRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRegistrationRequest from a JSON string
cluster_registration_request_instance = ClusterRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print(ClusterRegistrationRequest.to_json())

# convert the object into a dict
cluster_registration_request_dict = cluster_registration_request_instance.to_dict()
# create an instance of ClusterRegistrationRequest from a dict
cluster_registration_request_from_dict = ClusterRegistrationRequest.from_dict(cluster_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


