# CServeRecipePerf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe** | [**CServeRecipeOutput**](CServeRecipeOutput.md) |  | 
**hardware_instance_id** | **int** |  | 
**output_tp** | **List[List[object]]** |  | 
**mean_ttft** | **List[List[object]]** |  | 

## Example

```python
from platform_api_external_client.models.c_serve_recipe_perf import CServeRecipePerf

# TODO update the JSON string below
json = "{}"
# create an instance of CServeRecipePerf from a JSON string
c_serve_recipe_perf_instance = CServeRecipePerf.from_json(json)
# print the JSON string representation of the object
print(CServeRecipePerf.to_json())

# convert the object into a dict
c_serve_recipe_perf_dict = c_serve_recipe_perf_instance.to_dict()
# create an instance of CServeRecipePerf from a dict
c_serve_recipe_perf_from_dict = CServeRecipePerf.from_dict(c_serve_recipe_perf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


