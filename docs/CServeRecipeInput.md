# CServeRecipeInput

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
**use_prefix_caching** | **bool** |  | [optional] 
**offloading_num** | **int** |  | [optional] [default to 0]
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
from platform_api_external_client.models.c_serve_recipe_input import CServeRecipeInput

# TODO update the JSON string below
json = "{}"
# create an instance of CServeRecipeInput from a JSON string
c_serve_recipe_input_instance = CServeRecipeInput.from_json(json)
# print the JSON string representation of the object
print(CServeRecipeInput.to_json())

# convert the object into a dict
c_serve_recipe_input_dict = c_serve_recipe_input_instance.to_dict()
# create an instance of CServeRecipeInput from a dict
c_serve_recipe_input_from_dict = CServeRecipeInput.from_dict(c_serve_recipe_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


