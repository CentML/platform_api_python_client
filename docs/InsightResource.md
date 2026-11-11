# InsightResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**InsightResourceType**](InsightResourceType.md) |  | 
**id** | **int** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.insight_resource import InsightResource

# TODO update the JSON string below
json = "{}"
# create an instance of InsightResource from a JSON string
insight_resource_instance = InsightResource.from_json(json)
# print the JSON string representation of the object
print(InsightResource.to_json())

# convert the object into a dict
insight_resource_dict = insight_resource_instance.to_dict()
# create an instance of InsightResource from a dict
insight_resource_from_dict = InsightResource.from_dict(insight_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


