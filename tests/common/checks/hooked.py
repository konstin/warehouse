# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from warehouse.malware.checks.base import MalwareCheckBase
from warehouse.malware.errors import FatalCheckError
from warehouse.malware.models import VerdictClassification, VerdictConfidence


class ExampleHookedCheck(MalwareCheckBase):
    version = 1
    short_description = "An example hook-based check"
    long_description = "The purpose of this check is to test the \
implementation of a hook-based check. This check will generate verdicts if enabled."
    check_type = "event_hook"
    hooked_object = "File"

    def __init__(self, db):
        super().__init__(db)

    def scan(self, **kwargs):
        file_id = kwargs.get("obj_id")
        if file_id is None:
            raise FatalCheckError("Missing required kwarg `obj_id`")

        self.add_verdict(
            file_id=file_id,
            classification=VerdictClassification.Benign,
            confidence=VerdictConfidence.High,
            message="Nothing to see here!",
        )
