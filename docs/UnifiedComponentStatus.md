# UnifiedComponentStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**health** | [**ComponentHealth**](ComponentHealth.md) |  | 
**reason** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from platform_api_python_client.models.unified_component_status import UnifiedComponentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedComponentStatus from a JSON string
unified_component_status_instance = UnifiedComponentStatus.from_json(json)
# print the JSON string representation of the object
print(UnifiedComponentStatus.to_json())

# convert the object into a dict
unified_component_status_dict = unified_component_status_instance.to_dict()
# create an instance of UnifiedComponentStatus from a dict
unified_component_status_from_dict = UnifiedComponentStatus.from_dict(unified_component_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


