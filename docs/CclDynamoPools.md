# CclDynamoPools

Hardware and scaling per worker role. Aggregated mode uses exactly `worker`; disaggregated mode uses exactly `prefill` and `decode`. Unused roles are null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**worker** | [**Pool**](Pool.md) |  | [optional] 
**prefill** | [**Pool**](Pool.md) |  | [optional] 
**decode** | [**Pool**](Pool.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.ccl_dynamo_pools import CclDynamoPools

# TODO update the JSON string below
json = "{}"
# create an instance of CclDynamoPools from a JSON string
ccl_dynamo_pools_instance = CclDynamoPools.from_json(json)
# print the JSON string representation of the object
print(CclDynamoPools.to_json())

# convert the object into a dict
ccl_dynamo_pools_dict = ccl_dynamo_pools_instance.to_dict()
# create an instance of CclDynamoPools from a dict
ccl_dynamo_pools_from_dict = CclDynamoPools.from_dict(ccl_dynamo_pools_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


