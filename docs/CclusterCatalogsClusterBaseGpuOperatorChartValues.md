# CclusterCatalogsClusterBaseGpuOperatorChartValues

ChartValues are the upstream gpu-operator values worth setting per cluster.  Driver and Toolkit are the important ones, and the reason every optional scalar in these packages is a pointer. The chart ships both disabled for k3d and kind, where the node is a container sharing the host kernel and the in-cluster driver DaemonSet cannot load modules — there, the host supplies the driver and the container toolkit. On bare metal, EKS and GKE both must be enabled. A plain bool could not express the difference between \"leave the chart's default\" and \"explicitly false\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | [**Toggle**](Toggle.md) |  | [optional] 
**toolkit** | [**Toggle**](Toggle.md) |  | [optional] 
**nfd** | [**Toggle**](Toggle.md) |  | [optional] 
**cdi** | [**CDI**](CDI.md) |  | [optional] 
**mig** | [**MIG**](MIG.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.ccluster_catalogs_cluster_base_gpu_operator_chart_values import CclusterCatalogsClusterBaseGpuOperatorChartValues

# TODO update the JSON string below
json = "{}"
# create an instance of CclusterCatalogsClusterBaseGpuOperatorChartValues from a JSON string
ccluster_catalogs_cluster_base_gpu_operator_chart_values_instance = CclusterCatalogsClusterBaseGpuOperatorChartValues.from_json(json)
# print the JSON string representation of the object
print(CclusterCatalogsClusterBaseGpuOperatorChartValues.to_json())

# convert the object into a dict
ccluster_catalogs_cluster_base_gpu_operator_chart_values_dict = ccluster_catalogs_cluster_base_gpu_operator_chart_values_instance.to_dict()
# create an instance of CclusterCatalogsClusterBaseGpuOperatorChartValues from a dict
ccluster_catalogs_cluster_base_gpu_operator_chart_values_from_dict = CclusterCatalogsClusterBaseGpuOperatorChartValues.from_dict(ccluster_catalogs_cluster_base_gpu_operator_chart_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


