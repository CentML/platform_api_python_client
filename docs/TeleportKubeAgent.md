# TeleportKubeAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | **object** |  | [optional] 

## Example

```python
from platform_api_python_client.models.teleport_kube_agent import TeleportKubeAgent

# TODO update the JSON string below
json = "{}"
# create an instance of TeleportKubeAgent from a JSON string
teleport_kube_agent_instance = TeleportKubeAgent.from_json(json)
# print the JSON string representation of the object
print(TeleportKubeAgent.to_json())

# convert the object into a dict
teleport_kube_agent_dict = teleport_kube_agent_instance.to_dict()
# create an instance of TeleportKubeAgent from a dict
teleport_kube_agent_from_dict = TeleportKubeAgent.from_dict(teleport_kube_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


