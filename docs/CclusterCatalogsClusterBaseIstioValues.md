# CclusterCatalogsClusterBaseIstioValues

Values of the catalogs/cluster_base/istio chart, generated from its Go package.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**istio_base** | [**IstioBase**](IstioBase.md) |  | [optional] 
**istiod** | [**Istiod**](Istiod.md) |  | [optional] 
**istio_gateway** | [**IstioGateway**](IstioGateway.md) |  | [optional] 
**istio_cni** | [**IstioCNI**](IstioCNI.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.ccluster_catalogs_cluster_base_istio_values import CclusterCatalogsClusterBaseIstioValues

# TODO update the JSON string below
json = "{}"
# create an instance of CclusterCatalogsClusterBaseIstioValues from a JSON string
ccluster_catalogs_cluster_base_istio_values_instance = CclusterCatalogsClusterBaseIstioValues.from_json(json)
# print the JSON string representation of the object
print(CclusterCatalogsClusterBaseIstioValues.to_json())

# convert the object into a dict
ccluster_catalogs_cluster_base_istio_values_dict = ccluster_catalogs_cluster_base_istio_values_instance.to_dict()
# create an instance of CclusterCatalogsClusterBaseIstioValues from a dict
ccluster_catalogs_cluster_base_istio_values_from_dict = CclusterCatalogsClusterBaseIstioValues.from_dict(ccluster_catalogs_cluster_base_istio_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


