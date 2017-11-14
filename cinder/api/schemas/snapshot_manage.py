# Copyright (C) 2017 NTT DATA
# All Rights Reserved.
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Schema for V3 snapshot_manage API.

"""

from cinder.api.validation import parameter_types


create = {
    'type': 'object',
    'properties': {
        'type': 'object',
        'snapshot': {
            'type': 'object',
            'properties': {
                "description": parameter_types.description,
                "metadata": parameter_types.extra_specs,
                "name": parameter_types.name_allow_zero_min_length,
                "volume_id": parameter_types.uuid,
                "ref": {'type': ['object', 'null']},
            },
            'required': ['ref', 'volume_id'],
            'additionalProperties': False,
        },
    },
    'required': ['snapshot'],
    'additionalProperties': False,
}
