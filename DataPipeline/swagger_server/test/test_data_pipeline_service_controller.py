# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.data_pipeline_service_data_source import DataPipelineServiceDataSource  # noqa: E501
from swagger_server.models.data_pipeline_service_data_source_pool import DataPipelineServiceDataSourcePool  # noqa: E501
from swagger_server.models.data_pipeline_service_empty import DataPipelineServiceEmpty  # noqa: E501
from swagger_server.models.data_pipeline_service_extract import DataPipelineServiceExtract  # noqa: E501
from swagger_server.models.data_pipeline_service_identifier import DataPipelineServiceIdentifier  # noqa: E501
from swagger_server.models.data_pipeline_service_objects import DataPipelineServiceObjects  # noqa: E501
from swagger_server.models.data_pipeline_service_pools import DataPipelineServicePools  # noqa: E501
from swagger_server.models.data_pipeline_service_state import DataPipelineServiceState  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDataPipelineServiceController(BaseTestCase):
    """DataPipelineServiceController integration test stubs"""

    def test_create_pipeline(self):
        """Test case for create_pipeline

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/pipeline/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_pool(self):
        """Test case for create_pool

        Create A datapipeline Pool for a set of pipelines . Pipelines are always associated with a pool. A pool can have 0 or more pipelines
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/datapipeline/pool/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_pipeline(self):
        """Test case for delete_pipeline

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/pipeline/delete',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_pool(self):
        """Test case for delete_pool

        Delete A Data Pipeline pool , To delete a pool, all pipelines in the pool must be deleted
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
            '/v1/datapipeline/pool/list',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_objects_in_pool(self):
        """Test case for list_objects_in_pool

        
        """
        query_string = [('uuid', 'uuid_example'),
                        ('type', 'READ_DATASOURCE'),
                        ('name', 'name_example')]
        response = self.client.open(
            '/v1/datapipeline/pool/objects/list',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pause_pipeline(self):
        """Test case for pause_pipeline

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/pipeline/pause',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pause_pool(self):
        """Test case for pause_pool

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/datapipeline/pool/pause',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_data_source(self):
        """Test case for register_data_source

        
        """
        body = DataPipelineServiceDataSource()
        response = self.client.open(
            '/v1/datasource/register',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_data_source_to_pool(self):
        """Test case for register_data_source_to_pool

        
        """
        body = DataPipelineServiceDataSourcePool()
        response = self.client.open(
            '/v1/datasource/pool/register',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_run_pipeline(self):
        """Test case for run_pipeline

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/pipeline/run',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sample_data_source(self):
        """Test case for sample_data_source

        
        """
        query_string = [('uuid', 'uuid_example'),
                        ('type', 'READ_DATASOURCE'),
                        ('name', 'name_example')]
        response = self.client.open(
            '/v1/datasource/register',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_shutdown(self):
        """Test case for shutdown

        SHUTDOWN SERVICE
        """
        response = self.client.open(
            '/v1/datapipelineservice/shutdown',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_start_pool(self):
        """Test case for start_pool

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/datapipeline/pool/start',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_startup(self):
        """Test case for startup

        START SERVICE
        """
        response = self.client.open(
            '/v1/datapipelineservice/startup',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_status(self):
        """Test case for status

        CHECK STATUS OF SERVICE HEALTH
        """
        response = self.client.open(
            '/v1/datapipelineservice/status',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_stop_pipeline(self):
        """Test case for stop_pipeline

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/pipeline/unpause',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_stop_pool(self):
        """Test case for stop_pool

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/datapipeline/pool/stop',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_un_pause_pool(self):
        """Test case for un_pause_pool

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/datapipeline/pool/unpause',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
