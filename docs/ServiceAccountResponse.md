# ServiceAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workos_id** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from platform_api_python_client.models.service_account_response import ServiceAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountResponse from a JSON string
service_account_response_instance = ServiceAccountResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountResponse.to_json())

# convert the object into a dict
service_account_response_dict = service_account_response_instance.to_dict()
# create an instance of ServiceAccountResponse from a dict
service_account_response_from_dict = ServiceAccountResponse.from_dict(service_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


