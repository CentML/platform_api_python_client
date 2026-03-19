# ClusterCapacityResponse

Per-cluster GPU capacity breakdown returned inside ``GET /capacity``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** |  | 
**cluster_name** | **str** |  | 
**gpu_types** | [**List[GpuTypeCapacity]**](GpuTypeCapacity.md) |  | 

## Example

```python
from platform_api_python_client.models.cluster_capacity_response import ClusterCapacityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCapacityResponse from a JSON string
cluster_capacity_response_instance = ClusterCapacityResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterCapacityResponse.to_json())

# convert the object into a dict
cluster_capacity_response_dict = cluster_capacity_response_instance.to_dict()
# create an instance of ClusterCapacityResponse from a dict
cluster_capacity_response_from_dict = ClusterCapacityResponse.from_dict(cluster_capacity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


