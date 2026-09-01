# ListOrganizationGpuQuotaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[OrganizationGpuQuotaResponse]**](OrganizationGpuQuotaResponse.md) |  | 

## Example

```python
from platform_api_python_client.models.list_organization_gpu_quota_response import ListOrganizationGpuQuotaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrganizationGpuQuotaResponse from a JSON string
list_organization_gpu_quota_response_instance = ListOrganizationGpuQuotaResponse.from_json(json)
# print the JSON string representation of the object
print(ListOrganizationGpuQuotaResponse.to_json())

# convert the object into a dict
list_organization_gpu_quota_response_dict = list_organization_gpu_quota_response_instance.to_dict()
# create an instance of ListOrganizationGpuQuotaResponse from a dict
list_organization_gpu_quota_response_from_dict = ListOrganizationGpuQuotaResponse.from_dict(list_organization_gpu_quota_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


