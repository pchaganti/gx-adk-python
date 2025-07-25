# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Loop agent implementation."""

from __future__ import annotations

from typing import Literal
from typing import Optional

from pydantic import ConfigDict

from ..utils.feature_decorator import working_in_progress
from .base_agent_config import BaseAgentConfig


@working_in_progress('LoopAgentConfig is not ready for use.')
class LoopAgentConfig(BaseAgentConfig):
  """The config for the YAML schema of a LoopAgent."""

  model_config = ConfigDict(
      extra='forbid',
  )

  agent_class: Literal['LoopAgent'] = 'LoopAgent'

  max_iterations: Optional[int] = None
  """Optional. LoopAgent.max_iterations."""
