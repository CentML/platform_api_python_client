# ResourceList

ResourceList is one side of ResourceRequirements, as Kubernetes quantities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **str** |  | [optional] 
**memory** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.resource_list import ResourceList

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceList from a JSON string
resource_list_instance = ResourceList.from_json(json)
# print the JSON string representation of the object
print(ResourceList.to_json())

# convert the object into a dict
resource_list_dict = resource_list_instance.to_dict()
# create an instance of ResourceList from a dict
resource_list_from_dict = ResourceList.from_dict(resource_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


