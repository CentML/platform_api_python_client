# PrometheusSpec

PrometheusSpec is the Prometheus custom resource's spec.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_labels** | **Dict[str, str]** |  | [optional] 
**remote_write** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from platform_api_python_client.models.prometheus_spec import PrometheusSpec

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusSpec from a JSON string
prometheus_spec_instance = PrometheusSpec.from_json(json)
# print the JSON string representation of the object
print(PrometheusSpec.to_json())

# convert the object into a dict
prometheus_spec_dict = prometheus_spec_instance.to_dict()
# create an instance of PrometheusSpec from a dict
prometheus_spec_from_dict = PrometheusSpec.from_dict(prometheus_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


