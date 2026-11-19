# CclusterCatalogsClusterBaseIngressNginxController

Controller configures the ingress controller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**Metrics**](Metrics.md) |  | [optional] 
**autoscaling** | [**Autoscaling**](Autoscaling.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.ccluster_catalogs_cluster_base_ingress_nginx_controller import CclusterCatalogsClusterBaseIngressNginxController

# TODO update the JSON string below
json = "{}"
# create an instance of CclusterCatalogsClusterBaseIngressNginxController from a JSON string
ccluster_catalogs_cluster_base_ingress_nginx_controller_instance = CclusterCatalogsClusterBaseIngressNginxController.from_json(json)
# print the JSON string representation of the object
print(CclusterCatalogsClusterBaseIngressNginxController.to_json())

# convert the object into a dict
ccluster_catalogs_cluster_base_ingress_nginx_controller_dict = ccluster_catalogs_cluster_base_ingress_nginx_controller_instance.to_dict()
# create an instance of CclusterCatalogsClusterBaseIngressNginxController from a dict
ccluster_catalogs_cluster_base_ingress_nginx_controller_from_dict = CclusterCatalogsClusterBaseIngressNginxController.from_dict(ccluster_catalogs_cluster_base_ingress_nginx_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


