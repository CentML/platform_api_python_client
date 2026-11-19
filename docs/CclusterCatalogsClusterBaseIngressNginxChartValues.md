# CclusterCatalogsClusterBaseIngressNginxChartValues

ChartValues are the upstream ingress-nginx values worth setting per cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller** | [**CclusterCatalogsClusterBaseIngressNginxController**](CclusterCatalogsClusterBaseIngressNginxController.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.ccluster_catalogs_cluster_base_ingress_nginx_chart_values import CclusterCatalogsClusterBaseIngressNginxChartValues

# TODO update the JSON string below
json = "{}"
# create an instance of CclusterCatalogsClusterBaseIngressNginxChartValues from a JSON string
ccluster_catalogs_cluster_base_ingress_nginx_chart_values_instance = CclusterCatalogsClusterBaseIngressNginxChartValues.from_json(json)
# print the JSON string representation of the object
print(CclusterCatalogsClusterBaseIngressNginxChartValues.to_json())

# convert the object into a dict
ccluster_catalogs_cluster_base_ingress_nginx_chart_values_dict = ccluster_catalogs_cluster_base_ingress_nginx_chart_values_instance.to_dict()
# create an instance of CclusterCatalogsClusterBaseIngressNginxChartValues from a dict
ccluster_catalogs_cluster_base_ingress_nginx_chart_values_from_dict = CclusterCatalogsClusterBaseIngressNginxChartValues.from_dict(ccluster_catalogs_cluster_base_ingress_nginx_chart_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


