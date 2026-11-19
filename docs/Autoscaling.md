# Autoscaling

Autoscaling configures the controller's HorizontalPodAutoscaler.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**min_replicas** | **int** |  | [optional] 
**max_replicas** | **int** |  | [optional] 

## Example

```python
from platform_api_python_client.models.autoscaling import Autoscaling

# TODO update the JSON string below
json = "{}"
# create an instance of Autoscaling from a JSON string
autoscaling_instance = Autoscaling.from_json(json)
# print the JSON string representation of the object
print(Autoscaling.to_json())

# convert the object into a dict
autoscaling_dict = autoscaling_instance.to_dict()
# create an instance of Autoscaling from a dict
autoscaling_from_dict = Autoscaling.from_dict(autoscaling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


