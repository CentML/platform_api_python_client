# CServeRecipeOutput

Base class for deployment planner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**is_embedding_model** | **bool** |  | [default to False]
**tensor_parallel_size** | **int** |  | 
**pipeline_parallel_size** | **int** |  | 
**block_size** | **int** |  | [default to 32]
**swap_space** | **int** |  | [default to 0]
**gpu_mem_util** | **float** |  | [default to 0.95]
**max_num_seqs** | **int** |  | [default to 256]
**use_prefix_caching** | **bool** |  | 
**offloading_num** | **int** |  | [default to 0]
**use_flashinfer** | **bool** |  | [default to False]
**max_model_len** | **int** |  | 
**dtype** | **str** |  | [default to 'auto']
**tokenizer** | **str** |  | 
**spec_proposer** | **str** |  | 
**spec_draft_model** | **str** |  | 
**spec_tokens** | **int** |  | 
**spec_prompt_lookup_min** | **int** |  | 
**spec_prompt_lookup_max** | **int** |  | 
**seed** | **int** |  | [default to 0]

## Example

```python
from platform_api_python_client.models.c_serve_recipe_output import CServeRecipeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CServeRecipeOutput from a JSON string
c_serve_recipe_output_instance = CServeRecipeOutput.from_json(json)
# print the JSON string representation of the object
print(CServeRecipeOutput.to_json())

# convert the object into a dict
c_serve_recipe_output_dict = c_serve_recipe_output_instance.to_dict()
# create an instance of CServeRecipeOutput from a dict
c_serve_recipe_output_from_dict = CServeRecipeOutput.from_dict(c_serve_recipe_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


