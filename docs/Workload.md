# Workload

Workload is a KAI component's resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.workload import Workload

# TODO update the JSON string below
json = "{}"
# create an instance of Workload from a JSON string
workload_instance = Workload.from_json(json)
# print the JSON string representation of the object
print(Workload.to_json())

# convert the object into a dict
workload_dict = workload_instance.to_dict()
# create an instance of Workload from a dict
workload_from_dict = Workload.from_dict(workload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


