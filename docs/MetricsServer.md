# MetricsServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | **object** |  | [optional] 

## Example

```python
from platform_api_python_client.models.metrics_server import MetricsServer

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsServer from a JSON string
metrics_server_instance = MetricsServer.from_json(json)
# print the JSON string representation of the object
print(MetricsServer.to_json())

# convert the object into a dict
metrics_server_dict = metrics_server_instance.to_dict()
# create an instance of MetricsServer from a dict
metrics_server_from_dict = MetricsServer.from_dict(metrics_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


