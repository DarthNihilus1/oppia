# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Controllers for the Oppia admin view."""

__author__ = 'sll@google.com (Sean Lip)'

from oppia.apps.exploration import exp_services
from oppia.apps.widget import widget_domain
from oppia.controllers import base


def reload_widgets():
    """Refresh the default widgets."""
    widget_domain.Registry.refresh()


def reload_explorations():
    """Reload the default explorations."""
    exp_services.delete_demos()
    exp_services.load_demos()


def reload_demos():
    """Reload default widgets and explorations (in that order)."""
    reload_widgets()
    reload_explorations()


class AdminPage(base.BaseHandler):
    """Admin page shown in the App Engine admin console."""

    @base.require_admin
    def get(self):
        """Handles GET requests."""
        self.render_template('admin/admin.html')

    @base.require_admin
    def post(self):
        """Reloads the default widgets and explorations."""
        if self.payload.get('action') == 'reload':
            if self.payload.get('item') == 'explorations':
                reload_explorations()
            elif self.payload.get('item') == 'widgets':
                reload_widgets()