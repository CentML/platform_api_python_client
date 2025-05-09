# SetupUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_workos_organization_id** | **str** |  | 

## Example

```python
from platform_api_python_client.models.setup_user_response import SetupUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetupUserResponse from a JSON string
setup_user_response_instance = SetupUserResponse.from_json(json)
# print the JSON string representation of the object
print(SetupUserResponse.to_json())

# convert the object into a dict
setup_user_response_dict = setup_user_response_instance.to_dict()
# create an instance of SetupUserResponse from a dict
setup_user_response_from_dict = SetupUserResponse.from_dict(setup_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


