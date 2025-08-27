# RolloutStrategyParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_surge** | **int** |  | [optional] 
**max_unavailable** | **int** |  | [optional] 

## Example

```python
from platform_api_python_client.models.rollout_strategy_params import RolloutStrategyParams

# TODO update the JSON string below
json = "{}"
# create an instance of RolloutStrategyParams from a JSON string
rollout_strategy_params_instance = RolloutStrategyParams.from_json(json)
# print the JSON string representation of the object
print(RolloutStrategyParams.to_json())

# convert the object into a dict
rollout_strategy_params_dict = rollout_strategy_params_instance.to_dict()
# create an instance of RolloutStrategyParams from a dict
rollout_strategy_params_from_dict = RolloutStrategyParams.from_dict(rollout_strategy_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


