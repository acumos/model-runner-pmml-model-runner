#ACUMOS
#================================================================================
#Copyright @ 2018 AT&T Intellectual Property. All rights reserved.
#================================================================================
#This Acumos software file is distributed by AT&T under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#This file is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and 
#limitations under the License.

import logging

import connexion
from flask_testing import TestCase

from swagger_server.encoder import JSONEncoder


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        return app.app
