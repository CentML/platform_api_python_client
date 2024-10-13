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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from platform_api_python_client.models.deployment_status import DeploymentStatus
from platform_api_python_client.models.deployment_type import DeploymentType
from typing import Optional, Set
from typing_extensions import Self

class GetInferenceV2DeploymentResponse(BaseModel):
    """
    GetInferenceV2DeploymentResponse
    """ # noqa: E501
    cluster_id: StrictInt
    id: StrictInt
    name: StrictStr
    endpoint_url: StrictStr
    image_url: Optional[StrictStr]
    type: DeploymentType
    status: DeploymentStatus
    created_at: datetime
    hardware_instance_id: StrictInt
    container_port: StrictInt
    min_scale: StrictInt
    max_scale: StrictInt
    concurrency: Optional[StrictInt]
    healthcheck: Optional[StrictStr]
    endpoint_certificate_authority: Optional[StrictStr]
    env_vars: Optional[Dict[str, StrictStr]]
    __properties: ClassVar[List[str]] = ["cluster_id", "id", "name", "endpoint_url", "image_url", "type", "status", "created_at", "hardware_instance_id", "container_port", "min_scale", "max_scale", "concurrency", "healthcheck", "endpoint_certificate_authority", "env_vars"]

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
        """Create an instance of GetInferenceV2DeploymentResponse from a JSON string"""
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
        # set to None if image_url (nullable) is None
        # and model_fields_set contains the field
        if self.image_url is None and "image_url" in self.model_fields_set:
            _dict['image_url'] = None

        # set to None if concurrency (nullable) is None
        # and model_fields_set contains the field
        if self.concurrency is None and "concurrency" in self.model_fields_set:
            _dict['concurrency'] = None

        # set to None if healthcheck (nullable) is None
        # and model_fields_set contains the field
        if self.healthcheck is None and "healthcheck" in self.model_fields_set:
            _dict['healthcheck'] = None

        # set to None if endpoint_certificate_authority (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint_certificate_authority is None and "endpoint_certificate_authority" in self.model_fields_set:
            _dict['endpoint_certificate_authority'] = None

        # set to None if env_vars (nullable) is None
        # and model_fields_set contains the field
        if self.env_vars is None and "env_vars" in self.model_fields_set:
            _dict['env_vars'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetInferenceV2DeploymentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cluster_id": obj.get("cluster_id"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "endpoint_url": obj.get("endpoint_url"),
            "image_url": obj.get("image_url"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "created_at": obj.get("created_at"),
            "hardware_instance_id": obj.get("hardware_instance_id"),
            "container_port": obj.get("container_port"),
            "min_scale": obj.get("min_scale"),
            "max_scale": obj.get("max_scale"),
            "concurrency": obj.get("concurrency"),
            "healthcheck": obj.get("healthcheck"),
            "endpoint_certificate_authority": obj.get("endpoint_certificate_authority"),
            "env_vars": obj.get("env_vars")
        })
        return _obj


