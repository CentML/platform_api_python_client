# CclusterCatalogsClusterBaseKaiSchedulerValues

Values of the catalogs/cluster_base/kai_scheduler chart, generated from its Go package.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kai_scheduler** | [**CclusterCatalogsClusterBaseKaiSchedulerChartValues**](CclusterCatalogsClusterBaseKaiSchedulerChartValues.md) |  | [optional] 
**default_priorities** | [**DefaultPriorities**](DefaultPriorities.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.ccluster_catalogs_cluster_base_kai_scheduler_values import CclusterCatalogsClusterBaseKaiSchedulerValues

# TODO update the JSON string below
json = "{}"
# create an instance of CclusterCatalogsClusterBaseKaiSchedulerValues from a JSON string
ccluster_catalogs_cluster_base_kai_scheduler_values_instance = CclusterCatalogsClusterBaseKaiSchedulerValues.from_json(json)
# print the JSON string representation of the object
print(CclusterCatalogsClusterBaseKaiSchedulerValues.to_json())

# convert the object into a dict
ccluster_catalogs_cluster_base_kai_scheduler_values_dict = ccluster_catalogs_cluster_base_kai_scheduler_values_instance.to_dict()
# create an instance of CclusterCatalogsClusterBaseKaiSchedulerValues from a dict
ccluster_catalogs_cluster_base_kai_scheduler_values_from_dict = CclusterCatalogsClusterBaseKaiSchedulerValues.from_dict(ccluster_catalogs_cluster_base_kai_scheduler_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


