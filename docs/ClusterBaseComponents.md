# ClusterBaseComponents

The cluster_base components to install on a ccluster cluster, each as its chart's values.  A component is installed only when its field is set (``{}`` for the catalog defaults), with exactly the values given. One left out is not installed, and is uninstalled if an earlier update installed it. final_stack is required.  The values use the chart's own keys and may include keys the typed model doesn't list; they reach the chart unchanged. Inference deployments on GKE need ingress_nginx's `ingress-nginx.controller.podLabels` (`sidecar.istio.io/inject: \"true\"`), istio's CNI paths and gpu_operator's GKE driver paths. An unknown component name is rejected rather than read as one left out, which would uninstall it.  With the generated Python client, build the request with `UpdateClusterRequest.from_dict(...)`: its model constructors drop the keys a typed model doesn't list (CentML/platform#4946).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kube_prometheus_stack** | [**CclusterCatalogsClusterBaseKubePrometheusStackValues**](CclusterCatalogsClusterBaseKubePrometheusStackValues.md) |  | [optional] 
**istio** | [**CclusterCatalogsClusterBaseIstioValues**](CclusterCatalogsClusterBaseIstioValues.md) |  | [optional] 
**cert_manager** | [**CclusterCatalogsClusterBaseCertManagerValues**](CclusterCatalogsClusterBaseCertManagerValues.md) |  | [optional] 
**ingress_nginx** | [**CclusterCatalogsClusterBaseIngressNginxValues**](CclusterCatalogsClusterBaseIngressNginxValues.md) |  | [optional] 
**keda** | [**CclusterCatalogsClusterBaseKedaValues**](CclusterCatalogsClusterBaseKedaValues.md) |  | [optional] 
**argo_rollouts** | [**CclusterCatalogsClusterBaseArgoRolloutsValues**](CclusterCatalogsClusterBaseArgoRolloutsValues.md) |  | [optional] 
**gpu_operator** | [**CclusterCatalogsClusterBaseGpuOperatorValues**](CclusterCatalogsClusterBaseGpuOperatorValues.md) |  | [optional] 
**kai_scheduler** | [**CclusterCatalogsClusterBaseKaiSchedulerValues**](CclusterCatalogsClusterBaseKaiSchedulerValues.md) |  | [optional] 
**metrics_server** | [**CclusterCatalogsClusterBaseMetricsServerValues**](CclusterCatalogsClusterBaseMetricsServerValues.md) |  | [optional] 
**final_stack** | **Dict[str, object]** | Values of the catalogs/cluster_base/final_stack chart, generated from its Go package. | 

## Example

```python
from platform_api_python_client.models.cluster_base_components import ClusterBaseComponents

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterBaseComponents from a JSON string
cluster_base_components_instance = ClusterBaseComponents.from_json(json)
# print the JSON string representation of the object
print(ClusterBaseComponents.to_json())

# convert the object into a dict
cluster_base_components_dict = cluster_base_components_instance.to_dict()
# create an instance of ClusterBaseComponents from a dict
cluster_base_components_from_dict = ClusterBaseComponents.from_dict(cluster_base_components_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


