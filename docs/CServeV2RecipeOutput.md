# CServeV2RecipeOutput

Inputs to start deployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**is_embedding_model** | **bool** |  | [default to False]

## Example

```python
from platform_api_python_client.models.c_serve_v2_recipe_output import CServeV2RecipeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CServeV2RecipeOutput from a JSON string
c_serve_v2_recipe_output_instance = CServeV2RecipeOutput.from_json(json)
# print the JSON string representation of the object
print(CServeV2RecipeOutput.to_json())

# convert the object into a dict
c_serve_v2_recipe_output_dict = c_serve_v2_recipe_output_instance.to_dict()
# create an instance of CServeV2RecipeOutput from a dict
c_serve_v2_recipe_output_from_dict = CServeV2RecipeOutput.from_dict(c_serve_v2_recipe_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


