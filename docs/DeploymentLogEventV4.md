# DeploymentLogEventV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Stable event identity: &#39;&lt;nanosecond timestamp&gt;-&lt;content hash&gt;&#39;. Deduplication key for the re-deliveries of fetch_newer pages; its nanosecond prefix orders events (sorted insert for late arrivals, never append). | 
**timestamp** | **int** | Event timestamp in epoch milliseconds. | 
**message** | **str** | Raw log line as emitted by the container. | 

## Example

```python
from platform_api_python_client.models.deployment_log_event_v4 import DeploymentLogEventV4

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentLogEventV4 from a JSON string
deployment_log_event_v4_instance = DeploymentLogEventV4.from_json(json)
# print the JSON string representation of the object
print(DeploymentLogEventV4.to_json())

# convert the object into a dict
deployment_log_event_v4_dict = deployment_log_event_v4_instance.to_dict()
# create an instance of DeploymentLogEventV4 from a dict
deployment_log_event_v4_from_dict = DeploymentLogEventV4.from_dict(deployment_log_event_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


