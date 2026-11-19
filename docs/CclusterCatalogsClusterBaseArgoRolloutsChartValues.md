# CclusterCatalogsClusterBaseArgoRolloutsChartValues

ChartValues are the upstream argo-rollouts values worth setting per cluster. Anything not set here comes from catalogs/cluster_base/argo_rollouts/values.yaml.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller** | [**CclusterCatalogsClusterBaseArgoRolloutsController**](CclusterCatalogsClusterBaseArgoRolloutsController.md) |  | [optional] 
**dashboard** | [**Dashboard**](Dashboard.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.ccluster_catalogs_cluster_base_argo_rollouts_chart_values import CclusterCatalogsClusterBaseArgoRolloutsChartValues

# TODO update the JSON string below
json = "{}"
# create an instance of CclusterCatalogsClusterBaseArgoRolloutsChartValues from a JSON string
ccluster_catalogs_cluster_base_argo_rollouts_chart_values_instance = CclusterCatalogsClusterBaseArgoRolloutsChartValues.from_json(json)
# print the JSON string representation of the object
print(CclusterCatalogsClusterBaseArgoRolloutsChartValues.to_json())

# convert the object into a dict
ccluster_catalogs_cluster_base_argo_rollouts_chart_values_dict = ccluster_catalogs_cluster_base_argo_rollouts_chart_values_instance.to_dict()
# create an instance of CclusterCatalogsClusterBaseArgoRolloutsChartValues from a dict
ccluster_catalogs_cluster_base_argo_rollouts_chart_values_from_dict = CclusterCatalogsClusterBaseArgoRolloutsChartValues.from_dict(ccluster_catalogs_cluster_base_argo_rollouts_chart_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


