# CNI

CNI is where istio-cni writes its plugin binary and configuration. These are the only values in this chart that must be tuned per cluster: the chart's defaults are the standard paths, and the correct paths depend on the node image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cni_conf_dir** | **str** |  | [optional] 
**cni_bin_dir** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.cni import CNI

# TODO update the JSON string below
json = "{}"
# create an instance of CNI from a JSON string
cni_instance = CNI.from_json(json)
# print the JSON string representation of the object
print(CNI.to_json())

# convert the object into a dict
cni_dict = cni_instance.to_dict()
# create an instance of CNI from a dict
cni_from_dict = CNI.from_dict(cni_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


