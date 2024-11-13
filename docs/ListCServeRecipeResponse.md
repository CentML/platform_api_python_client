# ListCServeRecipeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CServeRecipeResponse]**](CServeRecipeResponse.md) |  | 

## Example

```python
from platform_api_python_client.models.list_c_serve_recipe_response import ListCServeRecipeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCServeRecipeResponse from a JSON string
list_c_serve_recipe_response_instance = ListCServeRecipeResponse.from_json(json)
# print the JSON string representation of the object
print(ListCServeRecipeResponse.to_json())

# convert the object into a dict
list_c_serve_recipe_response_dict = list_c_serve_recipe_response_instance.to_dict()
# create an instance of ListCServeRecipeResponse from a dict
list_c_serve_recipe_response_from_dict = ListCServeRecipeResponse.from_dict(list_c_serve_recipe_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


