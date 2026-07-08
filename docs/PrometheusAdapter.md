# PrometheusAdapter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | **object** |  | [optional] 

## Example

```python
from platform_api_python_client.models.prometheus_adapter import PrometheusAdapter

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusAdapter from a JSON string
prometheus_adapter_instance = PrometheusAdapter.from_json(json)
# print the JSON string representation of the object
print(PrometheusAdapter.to_json())

# convert the object into a dict
prometheus_adapter_dict = prometheus_adapter_instance.to_dict()
# create an instance of PrometheusAdapter from a dict
prometheus_adapter_from_dict = PrometheusAdapter.from_dict(prometheus_adapter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


