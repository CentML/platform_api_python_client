# CServeRecipe

Base class for deployment planner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**is_embedding_model** | **bool** |  | [optional] [default to False]
**tensor_parallel_size** | **int** |  | 
**pipeline_parallel_size** | **int** |  | 
**block_size** | **int** |  | [optional] [default to 32]
**swap_space** | **int** |  | [optional] [default to 0]
**gpu_mem_util** | **float** |  | [optional] [default to 0.95]
**max_num_seqs** | **int** |  | [optional] [default to 256]
**offloading_num** | **int** |  | [optional] [default to 0]
**use_prefix_caching** | **bool** |  | [optional] 
**use_chunked_prefill** | **bool** |  | [optional] 
**chunked_prefill_size** | **int** |  | [optional] 
**eager_execution** | **bool** |  | [optional] 
**num_scheduler_steps** | **int** |  | [optional] 
**use_flashinfer** | **bool** |  | [optional] [default to False]
**max_model_len** | **int** |  | [optional] 
**dtype** | **str** |  | [optional] [default to 'auto']
**tokenizer** | **str** |  | [optional] 
**spec_proposer** | **str** |  | [optional] 
**spec_draft_model** | **str** |  | [optional] 
**spec_tokens** | **int** |  | [optional] 
**spec_prompt_lookup_min** | **int** |  | [optional] 
**spec_prompt_lookup_max** | **int** |  | [optional] 
**seed** | **int** |  | [optional] [default to 0]

## Example

```python
from platform_api_python_client.models.c_serve_recipe import CServeRecipe

# TODO update the JSON string below
json = "{}"
# create an instance of CServeRecipe from a JSON string
c_serve_recipe_instance = CServeRecipe.from_json(json)
# print the JSON string representation of the object
print(CServeRecipe.to_json())

# convert the object into a dict
c_serve_recipe_dict = c_serve_recipe_instance.to_dict()
# create an instance of CServeRecipe from a dict
c_serve_recipe_from_dict = CServeRecipe.from_dict(c_serve_recipe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


