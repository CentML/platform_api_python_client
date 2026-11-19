# Prometheus

Prometheus configures the Prometheus instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prometheus_spec** | [**PrometheusSpec**](PrometheusSpec.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.prometheus import Prometheus

# TODO update the JSON string below
json = "{}"
# create an instance of Prometheus from a JSON string
prometheus_instance = Prometheus.from_json(json)
# print the JSON string representation of the object
print(Prometheus.to_json())

# convert the object into a dict
prometheus_dict = prometheus_instance.to_dict()
# create an instance of Prometheus from a dict
prometheus_from_dict = Prometheus.from_dict(prometheus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


