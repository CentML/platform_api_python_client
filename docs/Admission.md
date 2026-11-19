# Admission

Admission configures KAI's admission webhook.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_pod_runtime_class_name** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.admission import Admission

# TODO update the JSON string below
json = "{}"
# create an instance of Admission from a JSON string
admission_instance = Admission.from_json(json)
# print the JSON string representation of the object
print(Admission.to_json())

# convert the object into a dict
admission_dict = admission_instance.to_dict()
# create an instance of Admission from a dict
admission_from_dict = Admission.from_dict(admission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


