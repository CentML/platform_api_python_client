# KubePrometheusStack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | **object** |  | [optional] 

## Example

```python
from platform_api_python_client.models.kube_prometheus_stack import KubePrometheusStack

# TODO update the JSON string below
json = "{}"
# create an instance of KubePrometheusStack from a JSON string
kube_prometheus_stack_instance = KubePrometheusStack.from_json(json)
# print the JSON string representation of the object
print(KubePrometheusStack.to_json())

# convert the object into a dict
kube_prometheus_stack_dict = kube_prometheus_stack_instance.to_dict()
# create an instance of KubePrometheusStack from a dict
kube_prometheus_stack_from_dict = KubePrometheusStack.from_dict(kube_prometheus_stack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


