# CreateOrganizationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from platform_api_python_client.models.create_organization_response import CreateOrganizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationResponse from a JSON string
create_organization_response_instance = CreateOrganizationResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationResponse.to_json())

# convert the object into a dict
create_organization_response_dict = create_organization_response_instance.to_dict()
# create an instance of CreateOrganizationResponse from a dict
create_organization_response_from_dict = CreateOrganizationResponse.from_dict(create_organization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


