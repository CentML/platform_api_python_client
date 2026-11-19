# CclusterCatalogsClusterBaseKedaChartValues

ChartValues are the upstream keda values worth setting per cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | [**Replicas**](Replicas.md) |  | [optional] 
**metrics_server** | [**Replicas**](Replicas.md) |  | [optional] 
**webhooks** | [**Toggle**](Toggle.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.ccluster_catalogs_cluster_base_keda_chart_values import CclusterCatalogsClusterBaseKedaChartValues

# TODO update the JSON string below
json = "{}"
# create an instance of CclusterCatalogsClusterBaseKedaChartValues from a JSON string
ccluster_catalogs_cluster_base_keda_chart_values_instance = CclusterCatalogsClusterBaseKedaChartValues.from_json(json)
# print the JSON string representation of the object
print(CclusterCatalogsClusterBaseKedaChartValues.to_json())

# convert the object into a dict
ccluster_catalogs_cluster_base_keda_chart_values_dict = ccluster_catalogs_cluster_base_keda_chart_values_instance.to_dict()
# create an instance of CclusterCatalogsClusterBaseKedaChartValues from a dict
ccluster_catalogs_cluster_base_keda_chart_values_from_dict = CclusterCatalogsClusterBaseKedaChartValues.from_dict(ccluster_catalogs_cluster_base_keda_chart_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


