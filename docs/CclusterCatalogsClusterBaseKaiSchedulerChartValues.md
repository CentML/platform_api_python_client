# CclusterCatalogsClusterBaseKaiSchedulerChartValues

ChartValues are the upstream kai-scheduler values worth setting per cluster.  Scheduler.Resources, Binder and Admission reach the KAI components through the kai-config Config CR, which the upstream chart applies from a hook Job rather than as an Application resource. Argo CD does not diff hooks, so the chart also renders a ConfigMap holding a checksum of these values: changing them marks the Application OutOfSync, and the sync reruns the hook. Scheduler.PlacementStrategy goes to the SchedulingShard, Operator to the KAI operator Deployment and DefaultQueue to the default Queues, all ordinary Application resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduler** | [**Scheduler**](Scheduler.md) |  | [optional] 
**binder** | [**Workload**](Workload.md) |  | [optional] 
**operator** | [**Operator**](Operator.md) |  | [optional] 
**admission** | [**Admission**](Admission.md) |  | [optional] 
**default_queue** | [**DefaultQueue**](DefaultQueue.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.ccluster_catalogs_cluster_base_kai_scheduler_chart_values import CclusterCatalogsClusterBaseKaiSchedulerChartValues

# TODO update the JSON string below
json = "{}"
# create an instance of CclusterCatalogsClusterBaseKaiSchedulerChartValues from a JSON string
ccluster_catalogs_cluster_base_kai_scheduler_chart_values_instance = CclusterCatalogsClusterBaseKaiSchedulerChartValues.from_json(json)
# print the JSON string representation of the object
print(CclusterCatalogsClusterBaseKaiSchedulerChartValues.to_json())

# convert the object into a dict
ccluster_catalogs_cluster_base_kai_scheduler_chart_values_dict = ccluster_catalogs_cluster_base_kai_scheduler_chart_values_instance.to_dict()
# create an instance of CclusterCatalogsClusterBaseKaiSchedulerChartValues from a dict
ccluster_catalogs_cluster_base_kai_scheduler_chart_values_from_dict = CclusterCatalogsClusterBaseKaiSchedulerChartValues.from_dict(ccluster_catalogs_cluster_base_kai_scheduler_chart_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


