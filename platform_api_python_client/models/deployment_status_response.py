# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from platform_api_python_client.models.deployment_status import DeploymentStatus
from platform_api_python_client.models.deployment_type import DeploymentType
from platform_api_python_client.models.service_status import ServiceStatus
from typing import Optional, Set
from typing_extensions import Self

class DeploymentStatusResponse(BaseModel):
    """
    DeploymentStatusResponse
    """ # noqa: E501
    id: StrictInt
    type: DeploymentType
    status: DeploymentStatus
    service_status: Optional[ServiceStatus] = None
    error_message: Optional[StrictStr] = None
    endpoint_url: Optional[StrictStr] = None
    pod_status: Optional[List[Annotated[List[Any], Field(min_length=2, max_length=2)]]] = None
    __properties: ClassVar[List[str]] = ["id", "type", "status", "service_status", "error_message", "endpoint_url", "pod_status"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DeploymentStatusResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if service_status (nullable) is None
        # and model_fields_set contains the field
        if self.service_status is None and "service_status" in self.model_fields_set:
            _dict['service_status'] = None

        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict['error_message'] = None

        # set to None if endpoint_url (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint_url is None and "endpoint_url" in self.model_fields_set:
            _dict['endpoint_url'] = None

        # set to None if pod_status (nullable) is None
        # and model_fields_set contains the field
        if self.pod_status is None and "pod_status" in self.model_fields_set:
            _dict['pod_status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeploymentStatusResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "service_status": obj.get("service_status"),
            "error_message": obj.get("error_message"),
            "endpoint_url": obj.get("endpoint_url"),
            "pod_status": obj.get("pod_status")
        })
        return _obj


