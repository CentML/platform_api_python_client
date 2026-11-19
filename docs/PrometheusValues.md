# PrometheusValues

PrometheusValues configures cert-manager's metrics scraping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**servicemonitor** | [**Toggle**](Toggle.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.prometheus_values import PrometheusValues

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusValues from a JSON string
prometheus_values_instance = PrometheusValues.from_json(json)
# print the JSON string representation of the object
print(PrometheusValues.to_json())

# convert the object into a dict
prometheus_values_dict = prometheus_values_instance.to_dict()
# create an instance of PrometheusValues from a dict
prometheus_values_from_dict = PrometheusValues.from_dict(prometheus_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


