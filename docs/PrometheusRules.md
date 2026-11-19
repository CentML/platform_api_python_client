# PrometheusRules

PrometheusRules toggles the rules and monitors this chart renders itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod_alerts** | [**Toggle**](Toggle.md) |  | [optional] 
**envoy_stats** | [**Toggle**](Toggle.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.prometheus_rules import PrometheusRules

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusRules from a JSON string
prometheus_rules_instance = PrometheusRules.from_json(json)
# print the JSON string representation of the object
print(PrometheusRules.to_json())

# convert the object into a dict
prometheus_rules_dict = prometheus_rules_instance.to_dict()
# create an instance of PrometheusRules from a dict
prometheus_rules_from_dict = PrometheusRules.from_dict(prometheus_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


