# CclusterCatalogsClusterBaseDynamoPlatformValues

Values of the catalogs/cluster_base/dynamo_platform chart, generated from its Go package.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamo_platform** | **Dict[str, object]** | ChartValues are the upstream dynamo-platform values worth setting per cluster.  It is empty: no per-cluster tunable has been identified yet, and the chart&#39;s values.yaml fixes the upstream values the catalog relies on. It exists as a named struct rather than an anonymous one so that adding the first field later is a narrow change. | [optional] 

## Example

```python
from platform_api_python_client.models.ccluster_catalogs_cluster_base_dynamo_platform_values import CclusterCatalogsClusterBaseDynamoPlatformValues

# TODO update the JSON string below
json = "{}"
# create an instance of CclusterCatalogsClusterBaseDynamoPlatformValues from a JSON string
ccluster_catalogs_cluster_base_dynamo_platform_values_instance = CclusterCatalogsClusterBaseDynamoPlatformValues.from_json(json)
# print the JSON string representation of the object
print(CclusterCatalogsClusterBaseDynamoPlatformValues.to_json())

# convert the object into a dict
ccluster_catalogs_cluster_base_dynamo_platform_values_dict = ccluster_catalogs_cluster_base_dynamo_platform_values_instance.to_dict()
# create an instance of CclusterCatalogsClusterBaseDynamoPlatformValues from a dict
ccluster_catalogs_cluster_base_dynamo_platform_values_from_dict = CclusterCatalogsClusterBaseDynamoPlatformValues.from_dict(ccluster_catalogs_cluster_base_dynamo_platform_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


