# CDI

CDI configures the Container Device Interface.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**default** | **bool** |  | [optional] 

## Example

```python
from platform_api_python_client.models.cdi import CDI

# TODO update the JSON string below
json = "{}"
# create an instance of CDI from a JSON string
cdi_instance = CDI.from_json(json)
# print the JSON string representation of the object
print(CDI.to_json())

# convert the object into a dict
cdi_dict = cdi_instance.to_dict()
# create an instance of CDI from a dict
cdi_from_dict = CDI.from_dict(cdi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


