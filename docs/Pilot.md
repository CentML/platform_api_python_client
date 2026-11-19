# Pilot

Pilot configures istiod's pilot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoscale_min** | **int** |  | [optional] 

## Example

```python
from platform_api_python_client.models.pilot import Pilot

# TODO update the JSON string below
json = "{}"
# create an instance of Pilot from a JSON string
pilot_instance = Pilot.from_json(json)
# print the JSON string representation of the object
print(Pilot.to_json())

# convert the object into a dict
pilot_dict = pilot_instance.to_dict()
# create an instance of Pilot from a dict
pilot_from_dict = Pilot.from_dict(pilot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


