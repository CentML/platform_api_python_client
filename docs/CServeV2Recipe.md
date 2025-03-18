# CServeV2Recipe

Inputs to start deployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**is_embedding_model** | **bool** |  | [optional] [default to False]

## Example

```python
from platform_api_python_client.models.c_serve_v2_recipe import CServeV2Recipe

# TODO update the JSON string below
json = "{}"
# create an instance of CServeV2Recipe from a JSON string
c_serve_v2_recipe_instance = CServeV2Recipe.from_json(json)
# print the JSON string representation of the object
print(CServeV2Recipe.to_json())

# convert the object into a dict
c_serve_v2_recipe_dict = c_serve_v2_recipe_instance.to_dict()
# create an instance of CServeV2Recipe from a dict
c_serve_v2_recipe_from_dict = CServeV2Recipe.from_dict(c_serve_v2_recipe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


