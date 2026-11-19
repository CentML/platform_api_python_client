# CclusterCatalogsClusterBaseKubePrometheusStackValues

Values of the catalogs/cluster_base/kube_prometheus_stack chart, generated from its Go package.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kube_prometheus_stack** | [**CclusterCatalogsClusterBaseKubePrometheusStackChartValues**](CclusterCatalogsClusterBaseKubePrometheusStackChartValues.md) |  | [optional] 
**prometheus_rules** | [**PrometheusRules**](PrometheusRules.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.ccluster_catalogs_cluster_base_kube_prometheus_stack_values import CclusterCatalogsClusterBaseKubePrometheusStackValues

# TODO update the JSON string below
json = "{}"
# create an instance of CclusterCatalogsClusterBaseKubePrometheusStackValues from a JSON string
ccluster_catalogs_cluster_base_kube_prometheus_stack_values_instance = CclusterCatalogsClusterBaseKubePrometheusStackValues.from_json(json)
# print the JSON string representation of the object
print(CclusterCatalogsClusterBaseKubePrometheusStackValues.to_json())

# convert the object into a dict
ccluster_catalogs_cluster_base_kube_prometheus_stack_values_dict = ccluster_catalogs_cluster_base_kube_prometheus_stack_values_instance.to_dict()
# create an instance of CclusterCatalogsClusterBaseKubePrometheusStackValues from a dict
ccluster_catalogs_cluster_base_kube_prometheus_stack_values_from_dict = CclusterCatalogsClusterBaseKubePrometheusStackValues.from_dict(ccluster_catalogs_cluster_base_kube_prometheus_stack_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


