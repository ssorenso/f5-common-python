# coding=utf-8
#
# Copyright 2016 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""BIG-IP® utility module

REST URI
    ``http://localhost/mgmt/tm/util/unix-ls``

GUI Path
    N/A

REST Kind
    ``tm:util:unix-ls:*``
"""

from f5.bigip.mixins import CommandExecutionMixin
from f5.bigip.resource import UnnamedResource


class Unix_Ls(UnnamedResource, CommandExecutionMixin):

    def __init__(self, util):
        super(Unix_Ls, self).__init__(util)
        self._meta_data['required_command_parameters'].update(('utilCmdArgs',))
        self._meta_data['required_json_kind'] = 'tm:util:unix-ls:runstate'
        self._meta_data['allowed_commands'].append('run')
