# MetricsConfig

User-application Prometheus metrics endpoint.  Atomic: both `port` and `path` must be supplied together. To omit the endpoint entirely, leave the parent request's `metrics` field unset — it persists as null and the Helm chart applies the defaults (`container_port` + `/metrics`) at render time. The API never synthesizes these values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** |  | 
**path** | **str** |  | 

## Example

```python
from platform_api_python_client.models.metrics_config import MetricsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsConfig from a JSON string
metrics_config_instance = MetricsConfig.from_json(json)
# print the JSON string representation of the object
print(MetricsConfig.to_json())

# convert the object into a dict
metrics_config_dict = metrics_config_instance.to_dict()
# create an instance of MetricsConfig from a dict
metrics_config_from_dict = MetricsConfig.from_dict(metrics_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


