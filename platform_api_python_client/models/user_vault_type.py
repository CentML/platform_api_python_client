# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class UserVaultType(str, Enum):
    """
    UserVaultType
    """

    """
    allowed enum values
    """
    ENV_VARS = 'env_vars'
    SSH_KEYS = 'ssh_keys'
    ACCESS_TOKENS = 'access_tokens'
    CERTIFICATES = 'certificates'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UserVaultType from a JSON string"""
        return cls(json.loads(json_str))

