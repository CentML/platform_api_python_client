# Scheduler

Scheduler configures the scheduler.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_strategy** | **str** |  | [optional] 
**resources** | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.scheduler import Scheduler

# TODO update the JSON string below
json = "{}"
# create an instance of Scheduler from a JSON string
scheduler_instance = Scheduler.from_json(json)
# print the JSON string representation of the object
print(Scheduler.to_json())

# convert the object into a dict
scheduler_dict = scheduler_instance.to_dict()
# create an instance of Scheduler from a dict
scheduler_from_dict = Scheduler.from_dict(scheduler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


