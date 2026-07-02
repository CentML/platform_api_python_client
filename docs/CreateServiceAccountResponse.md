# CreateServiceAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workos_id** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**client_secret** | **str** |  | 

## Example

```python
from platform_api_python_client.models.create_service_account_response import CreateServiceAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServiceAccountResponse from a JSON string
create_service_account_response_instance = CreateServiceAccountResponse.from_json(json)
# print the JSON string representation of the object
print(CreateServiceAccountResponse.to_json())

# convert the object into a dict
create_service_account_response_dict = create_service_account_response_instance.to_dict()
# create an instance of CreateServiceAccountResponse from a dict
create_service_account_response_from_dict = CreateServiceAccountResponse.from_dict(create_service_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


