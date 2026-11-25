# GetClusterStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ClusterStatus**](ClusterStatus.md) | deleting while the cluster&#39;s infra plane is being deleted, whatever its conditions. Otherwise ready when the Available, ClusterConfigApplied, Verified and DNSReady conditions are all True, and if not, the first of them, in that order, that is not True decides: pending when it is False or not reported yet, unknown when it is Unknown. | 
**message** | **str** | Why the cluster is not ready; null when ready. | 

## Example

```python
from platform_api_python_client.models.get_cluster_status_response import GetClusterStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClusterStatusResponse from a JSON string
get_cluster_status_response_instance = GetClusterStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetClusterStatusResponse.to_json())

# convert the object into a dict
get_cluster_status_response_dict = get_cluster_status_response_instance.to_dict()
# create an instance of GetClusterStatusResponse from a dict
get_cluster_status_response_from_dict = GetClusterStatusResponse.from_dict(get_cluster_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


