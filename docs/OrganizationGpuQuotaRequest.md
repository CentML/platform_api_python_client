# OrganizationGpuQuotaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_quota** | **int** |  | 

## Example

```python
from platform_api_python_client.models.organization_gpu_quota_request import OrganizationGpuQuotaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationGpuQuotaRequest from a JSON string
organization_gpu_quota_request_instance = OrganizationGpuQuotaRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationGpuQuotaRequest.to_json())

# convert the object into a dict
organization_gpu_quota_request_dict = organization_gpu_quota_request_instance.to_dict()
# create an instance of OrganizationGpuQuotaRequest from a dict
organization_gpu_quota_request_from_dict = OrganizationGpuQuotaRequest.from_dict(organization_gpu_quota_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


