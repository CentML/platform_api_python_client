# ClusterComponents

Per-component ApplicationSet entries — the caller-facing surface.  This is the request-body schema for cluster updates: callers may flip `enabled` and supply per-component `values`, but nothing here is cluster identity. Cluster identity lives in `Shared` and is passed as serialization context when building ApplicationSet elements.  Field declaration order is for code locality only — actual bring-up order is driven by each subclass's `wave` ClassVar (rendered into the child Application's argocd.argoproj.io/sync-wave annotation).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kube_prometheus_stack** | [**KubePrometheusStack**](KubePrometheusStack.md) |  | [optional] 
**istio** | [**Istio**](Istio.md) |  | [optional] 
**cert_manager** | [**CertManager**](CertManager.md) |  | [optional] 
**ingress_nginx** | [**IngressNginx**](IngressNginx.md) |  | [optional] 
**spire_crds** | [**SpireCrds**](SpireCrds.md) |  | [optional] 
**spire** | [**Spire**](Spire.md) |  | [optional] 
**external_dns** | [**ExternalDns**](ExternalDns.md) |  | [optional] 
**prometheus_adapter** | [**PrometheusAdapter**](PrometheusAdapter.md) |  | [optional] 
**keda** | [**Keda**](Keda.md) |  | [optional] 
**fluent_bit** | [**FluentBit**](FluentBit.md) |  | [optional] 
**argo_rollouts** | [**ArgoRollouts**](ArgoRollouts.md) |  | [optional] 
**network_operator** | [**NetworkOperator**](NetworkOperator.md) |  | [optional] 
**opentelemetry_collector** | [**OpentelemetryCollector**](OpentelemetryCollector.md) |  | [optional] 
**gpu_operator** | [**GpuOperator**](GpuOperator.md) |  | [optional] 
**longhorn** | [**Longhorn**](Longhorn.md) |  | [optional] 
**metrics_server** | [**MetricsServer**](MetricsServer.md) |  | [optional] 
**teleport_kube_agent** | [**TeleportKubeAgent**](TeleportKubeAgent.md) |  | [optional] 
**final_stack** | [**FinalStack**](FinalStack.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.cluster_components import ClusterComponents

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComponents from a JSON string
cluster_components_instance = ClusterComponents.from_json(json)
# print the JSON string representation of the object
print(ClusterComponents.to_json())

# convert the object into a dict
cluster_components_dict = cluster_components_instance.to_dict()
# create an instance of ClusterComponents from a dict
cluster_components_from_dict = ClusterComponents.from_dict(cluster_components_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


