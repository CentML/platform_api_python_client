# DefaultQueue

DefaultQueue configures the queue for unlabelled pods.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_default_queue** | **bool** |  | [optional] 

## Example

```python
from platform_api_python_client.models.default_queue import DefaultQueue

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultQueue from a JSON string
default_queue_instance = DefaultQueue.from_json(json)
# print the JSON string representation of the object
print(DefaultQueue.to_json())

# convert the object into a dict
default_queue_dict = default_queue_instance.to_dict()
# create an instance of DefaultQueue from a dict
default_queue_from_dict = DefaultQueue.from_dict(default_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


