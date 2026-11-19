# CclusterCatalogsClusterBaseCertManagerChartValues

ChartValues are the upstream cert-manager values worth setting per cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replica_count** | **int** |  | [optional] 
**prometheus** | [**PrometheusValues**](PrometheusValues.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.ccluster_catalogs_cluster_base_cert_manager_chart_values import CclusterCatalogsClusterBaseCertManagerChartValues

# TODO update the JSON string below
json = "{}"
# create an instance of CclusterCatalogsClusterBaseCertManagerChartValues from a JSON string
ccluster_catalogs_cluster_base_cert_manager_chart_values_instance = CclusterCatalogsClusterBaseCertManagerChartValues.from_json(json)
# print the JSON string representation of the object
print(CclusterCatalogsClusterBaseCertManagerChartValues.to_json())

# convert the object into a dict
ccluster_catalogs_cluster_base_cert_manager_chart_values_dict = ccluster_catalogs_cluster_base_cert_manager_chart_values_instance.to_dict()
# create an instance of CclusterCatalogsClusterBaseCertManagerChartValues from a dict
ccluster_catalogs_cluster_base_cert_manager_chart_values_from_dict = CclusterCatalogsClusterBaseCertManagerChartValues.from_dict(ccluster_catalogs_cluster_base_cert_manager_chart_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


