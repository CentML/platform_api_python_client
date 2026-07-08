# OpentelemetryCollector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | **object** |  | [optional] 

## Example

```python
from platform_api_python_client.models.opentelemetry_collector import OpentelemetryCollector

# TODO update the JSON string below
json = "{}"
# create an instance of OpentelemetryCollector from a JSON string
opentelemetry_collector_instance = OpentelemetryCollector.from_json(json)
# print the JSON string representation of the object
print(OpentelemetryCollector.to_json())

# convert the object into a dict
opentelemetry_collector_dict = opentelemetry_collector_instance.to_dict()
# create an instance of OpentelemetryCollector from a dict
opentelemetry_collector_from_dict = OpentelemetryCollector.from_dict(opentelemetry_collector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


