# Replicas

Replicas is a subchart's replica count.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replica_count** | **int** |  | [optional] 

## Example

```python
from platform_api_python_client.models.replicas import Replicas

# TODO update the JSON string below
json = "{}"
# create an instance of Replicas from a JSON string
replicas_instance = Replicas.from_json(json)
# print the JSON string representation of the object
print(Replicas.to_json())

# convert the object into a dict
replicas_dict = replicas_instance.to_dict()
# create an instance of Replicas from a dict
replicas_from_dict = Replicas.from_dict(replicas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


