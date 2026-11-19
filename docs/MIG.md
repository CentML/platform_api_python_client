# MIG

MIG configures Multi-Instance GPU partitioning.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.mig import MIG

# TODO update the JSON string below
json = "{}"
# create an instance of MIG from a JSON string
mig_instance = MIG.from_json(json)
# print the JSON string representation of the object
print(MIG.to_json())

# convert the object into a dict
mig_dict = mig_instance.to_dict()
# create an instance of MIG from a dict
mig_from_dict = MIG.from_dict(mig_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


