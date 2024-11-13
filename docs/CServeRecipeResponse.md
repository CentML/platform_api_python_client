# CServeRecipeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**cluster_id** | **int** |  | 
**fastest** | [**CServeRecipePerf**](CServeRecipePerf.md) |  | 
**cheapest** | [**CServeRecipePerf**](CServeRecipePerf.md) |  | 
**best_value** | [**CServeRecipePerf**](CServeRecipePerf.md) |  | 

## Example

```python
from platform_api_python_client.models.c_serve_recipe_response import CServeRecipeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CServeRecipeResponse from a JSON string
c_serve_recipe_response_instance = CServeRecipeResponse.from_json(json)
# print the JSON string representation of the object
print(CServeRecipeResponse.to_json())

# convert the object into a dict
c_serve_recipe_response_dict = c_serve_recipe_response_instance.to_dict()
# create an instance of CServeRecipeResponse from a dict
c_serve_recipe_response_from_dict = CServeRecipeResponse.from_dict(c_serve_recipe_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


