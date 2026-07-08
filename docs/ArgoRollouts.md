# ArgoRollouts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | **object** |  | [optional] 

## Example

```python
from platform_api_python_client.models.argo_rollouts import ArgoRollouts

# TODO update the JSON string below
json = "{}"
# create an instance of ArgoRollouts from a JSON string
argo_rollouts_instance = ArgoRollouts.from_json(json)
# print the JSON string representation of the object
print(ArgoRollouts.to_json())

# convert the object into a dict
argo_rollouts_dict = argo_rollouts_instance.to_dict()
# create an instance of ArgoRollouts from a dict
argo_rollouts_from_dict = ArgoRollouts.from_dict(argo_rollouts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


