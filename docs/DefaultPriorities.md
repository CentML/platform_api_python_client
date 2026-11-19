# DefaultPriorities

DefaultPriorities configures the per-kind preemptibility ConfigMap.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 

## Example

```python
from platform_api_python_client.models.default_priorities import DefaultPriorities

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultPriorities from a JSON string
default_priorities_instance = DefaultPriorities.from_json(json)
# print the JSON string representation of the object
print(DefaultPriorities.to_json())

# convert the object into a dict
default_priorities_dict = default_priorities_instance.to_dict()
# create an instance of DefaultPriorities from a dict
default_priorities_from_dict = DefaultPriorities.from_dict(default_priorities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


