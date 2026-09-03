# OrganizationGpuQuotaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | 
**cluster_id** | **int** |  | 
**gpu_quota** | **int** |  | 

## Example

```python
from platform_api_python_client.models.organization_gpu_quota_response import OrganizationGpuQuotaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationGpuQuotaResponse from a JSON string
organization_gpu_quota_response_instance = OrganizationGpuQuotaResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationGpuQuotaResponse.to_json())

# convert the object into a dict
organization_gpu_quota_response_dict = organization_gpu_quota_response_instance.to_dict()
# create an instance of OrganizationGpuQuotaResponse from a dict
organization_gpu_quota_response_from_dict = OrganizationGpuQuotaResponse.from_dict(organization_gpu_quota_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


