# GpuOperator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | **object** |  | [optional] 

## Example

```python
from platform_api_python_client.models.gpu_operator import GpuOperator

# TODO update the JSON string below
json = "{}"
# create an instance of GpuOperator from a JSON string
gpu_operator_instance = GpuOperator.from_json(json)
# print the JSON string representation of the object
print(GpuOperator.to_json())

# convert the object into a dict
gpu_operator_dict = gpu_operator_instance.to_dict()
# create an instance of GpuOperator from a dict
gpu_operator_from_dict = GpuOperator.from_dict(gpu_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


