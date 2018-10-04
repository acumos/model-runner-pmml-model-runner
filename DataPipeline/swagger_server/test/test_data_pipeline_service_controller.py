# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.data_pipeline_service_empty import DataPipelineServiceEmpty  # noqa: E501
from swagger_server.models.data_pipeline_service_identifier import DataPipelineServiceIdentifier  # noqa: E501
from swagger_server.models.data_pipeline_service_pools import DataPipelineServicePools  # noqa: E501
from swagger_server.models.data_pipeline_service_state import DataPipelineServiceState  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDataPipelineServiceController(BaseTestCase):
    """DataPipelineServiceController integration test stubs"""

    def test_create_pool(self):
        """Test case for create_pool

        ------------------- DATA PIPELINE POOLS ----------------
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/datapipeline/pool/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_pool(self):
        """Test case for delete_pool

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/datapipeline/pool/delete',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_all_pools(self):
        """Test case for list_all_pools

        
        """
        response = self.client.open(
            '/v1/datapipeline/pool/listall',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_shutdown(self):
        """Test case for shutdown

        SHUTDOWN SERVICE
        """
        response = self.client.open(
            '/v1/champion_challenger/shutdown',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_startup(self):
        """Test case for startup

        START SERVICE
        """
        response = self.client.open(
            '/v1/champion_challenger/startup',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_status(self):
        """Test case for status

        CHECK STATUS OF SERVICE HEALTH
        """
        response = self.client.open(
            '/v1/champion_challenger/status',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
