# CclusterCatalogsClusterBaseKubePrometheusStackChartValues

ChartValues are the upstream kube-prometheus-stack values worth setting per cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grafana** | [**Toggle**](Toggle.md) |  | [optional] 
**prometheus** | [**Prometheus**](Prometheus.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.ccluster_catalogs_cluster_base_kube_prometheus_stack_chart_values import CclusterCatalogsClusterBaseKubePrometheusStackChartValues

# TODO update the JSON string below
json = "{}"
# create an instance of CclusterCatalogsClusterBaseKubePrometheusStackChartValues from a JSON string
ccluster_catalogs_cluster_base_kube_prometheus_stack_chart_values_instance = CclusterCatalogsClusterBaseKubePrometheusStackChartValues.from_json(json)
# print the JSON string representation of the object
print(CclusterCatalogsClusterBaseKubePrometheusStackChartValues.to_json())

# convert the object into a dict
ccluster_catalogs_cluster_base_kube_prometheus_stack_chart_values_dict = ccluster_catalogs_cluster_base_kube_prometheus_stack_chart_values_instance.to_dict()
# create an instance of CclusterCatalogsClusterBaseKubePrometheusStackChartValues from a dict
ccluster_catalogs_cluster_base_kube_prometheus_stack_chart_values_from_dict = CclusterCatalogsClusterBaseKubePrometheusStackChartValues.from_dict(ccluster_catalogs_cluster_base_kube_prometheus_stack_chart_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


