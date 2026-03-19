# GpuTypeCapacity

Allocatable vs requested GPU counts for a single resource type.  Attributes:     gpu_type: Human-readable name. For full GPUs this is the         ``nvidia.com/gpu.product`` node label (e.g. ``NVIDIA-H200``).         For MIG slices the profile is appended (e.g. ``NVIDIA-H200 MIG-1g.18gb``).     total_gpus: Total allocatable units of this resource across the cluster.     used_gpus: Units currently requested by running pods.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_type** | **str** |  | 
**total_gpus** | **int** |  | 
**used_gpus** | **int** |  | 

## Example

```python
from platform_api_python_client.models.gpu_type_capacity import GpuTypeCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of GpuTypeCapacity from a JSON string
gpu_type_capacity_instance = GpuTypeCapacity.from_json(json)
# print the JSON string representation of the object
print(GpuTypeCapacity.to_json())

# convert the object into a dict
gpu_type_capacity_dict = gpu_type_capacity_instance.to_dict()
# create an instance of GpuTypeCapacity from a dict
gpu_type_capacity_from_dict = GpuTypeCapacity.from_dict(gpu_type_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


