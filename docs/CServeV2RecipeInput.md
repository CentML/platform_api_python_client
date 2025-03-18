# CServeV2RecipeInput

Inputs to start deployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**is_embedding_model** | **bool** |  | [optional] [default to False]

## Example

```python
from platform_api_python_client.models.c_serve_v2_recipe_input import CServeV2RecipeInput

# TODO update the JSON string below
json = "{}"
# create an instance of CServeV2RecipeInput from a JSON string
c_serve_v2_recipe_input_instance = CServeV2RecipeInput.from_json(json)
# print the JSON string representation of the object
print(CServeV2RecipeInput.to_json())

# convert the object into a dict
c_serve_v2_recipe_input_dict = c_serve_v2_recipe_input_instance.to_dict()
# create an instance of CServeV2RecipeInput from a dict
c_serve_v2_recipe_input_from_dict = CServeV2RecipeInput.from_dict(c_serve_v2_recipe_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


