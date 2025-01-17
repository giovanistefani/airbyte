# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class RecordFilter(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RecordFilter - a model defined in OpenAPI

        config: The config of this RecordFilter.
        condition: The condition of this RecordFilter [Optional].
    """

    config: Dict[str, Any]
    condition: Optional[str] = None

RecordFilter.update_forward_refs()
