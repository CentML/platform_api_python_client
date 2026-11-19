# CclusterCatalogsClusterBaseGpuOperatorValues

Values of the catalogs/cluster_base/gpu_operator chart, generated from its Go package.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_operator** | [**CclusterCatalogsClusterBaseGpuOperatorChartValues**](CclusterCatalogsClusterBaseGpuOperatorChartValues.md) |  | [optional] 
**quota** | [**Quota**](Quota.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.ccluster_catalogs_cluster_base_gpu_operator_values import CclusterCatalogsClusterBaseGpuOperatorValues

# TODO update the JSON string below
json = "{}"
# create an instance of CclusterCatalogsClusterBaseGpuOperatorValues from a JSON string
ccluster_catalogs_cluster_base_gpu_operator_values_instance = CclusterCatalogsClusterBaseGpuOperatorValues.from_json(json)
# print the JSON string representation of the object
print(CclusterCatalogsClusterBaseGpuOperatorValues.to_json())

# convert the object into a dict
ccluster_catalogs_cluster_base_gpu_operator_values_dict = ccluster_catalogs_cluster_base_gpu_operator_values_instance.to_dict()
# create an instance of CclusterCatalogsClusterBaseGpuOperatorValues from a dict
ccluster_catalogs_cluster_base_gpu_operator_values_from_dict = CclusterCatalogsClusterBaseGpuOperatorValues.from_dict(ccluster_catalogs_cluster_base_gpu_operator_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


