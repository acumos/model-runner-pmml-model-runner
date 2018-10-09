#ACUMOS
#================================================================================
#Copyright Â© 2018 AT&T Intellectual Property. All rights reserved.
#================================================================================
#This Acumos software file is distributed by AT&Tunder the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#This file is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and 
#limitations under the License.

# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.data_pipeline_service_data_source import DataPipelineServiceDataSource  # noqa: E501
from swagger_server.models.data_pipeline_service_data_source_pool import DataPipelineServiceDataSourcePool  # noqa: E501
from swagger_server.models.data_pipeline_service_empty import DataPipelineServiceEmpty  # noqa: E501
from swagger_server.models.data_pipeline_service_extract import DataPipelineServiceExtract  # noqa: E501
from swagger_server.models.data_pipeline_service_id_metrics import DataPipelineServiceIdMetrics  # noqa: E501
from swagger_server.models.data_pipeline_service_identifier import DataPipelineServiceIdentifier  # noqa: E501
from swagger_server.models.data_pipeline_service_objects import DataPipelineServiceObjects  # noqa: E501
from swagger_server.models.data_pipeline_service_pools import DataPipelineServicePools  # noqa: E501
from swagger_server.models.data_pipeline_service_processor_payload import DataPipelineServiceProcessorPayload  # noqa: E501
from swagger_server.models.data_pipeline_service_processor_topic import DataPipelineServiceProcessorTopic  # noqa: E501
from swagger_server.models.data_pipeline_service_state import DataPipelineServiceState  # noqa: E501
from swagger_server.models.data_pipeline_service_topic import DataPipelineServiceTopic  # noqa: E501
from swagger_server.models.data_pipeline_service_topic_data_source import DataPipelineServiceTopicDataSource  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDataPipelineServiceController(BaseTestCase):
    """DataPipelineServiceController integration test stubs"""

    def test_archive_processor(self):
        """Test case for archive_processor

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/processor/{uuid}/archive'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_associate_processor_to_sink_topic(self):
        """Test case for associate_processor_to_sink_topic

        
        """
        body = DataPipelineServiceProcessorTopic()
        response = self.client.open(
            '/v1/processor/topic',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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

    def test_create_processor(self):
        """Test case for create_processor

        
        """
        body = DataPipelineServiceProcessorPayload()
        response = self.client.open(
            '/v1/processor/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_topic(self):
        """Test case for create_topic

        
        """
        body = DataPipelineServiceTopic()
        response = self.client.open(
            '/v1/topic/create',
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
            '/v1/pipeline/{uuid}/delete'.format(uuid='uuid_example'),
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
            '/v1/datapipeline/{uuid}/pool/delete'.format(uuid='uuid_example'),
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
        query_string = [('type', 'READ_DATASOURCE'),
                        ('name', 'name_example')]
        response = self.client.open(
            '/v1/datapipeline/{uuid}/pool/objects/list'.format(uuid='uuid_example'),
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
            '/v1/pipeline/{uuid}/pause'.format(uuid='uuid_example'),
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
            '/v1/datapipeline/{uuid}/pool/pause'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pause_processor(self):
        """Test case for pause_processor

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/processor/{uuid}/pause'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_re_start_processor(self):
        """Test case for re_start_processor

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/processor/{uuid}/restart'.format(uuid='uuid_example'),
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

    def test_register_topic_for_data_source(self):
        """Test case for register_topic_for_data_source

        
        """
        body = DataPipelineServiceTopicDataSource()
        response = self.client.open(
            '/v1/topic/datasource/register',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_restore_pipeline_snapshot(self):
        """Test case for restore_pipeline_snapshot

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/pipeline/{uuid}/restore'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_metrics(self):
        """Test case for retrieve_metrics

        
        """
        query_string = [('ident_uuid', 'ident_uuid_example'),
                        ('ident_type', 'READ_DATASOURCE'),
                        ('ident_name', 'ident_name_example')]
        response = self.client.open(
            '/v1/Identifier/metrics',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_run_pipeline(self):
        """Test case for run_pipeline

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/pipeline/{uuid}/run'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_run_processor(self):
        """Test case for run_processor

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/processor/{uuid}/run'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sample_data_source(self):
        """Test case for sample_data_source

        
        """
        query_string = [('type', 'READ_DATASOURCE'),
                        ('name', 'name_example')]
        response = self.client.open(
            '/v1/datasource/{uuid}/sample'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sample_topic(self):
        """Test case for sample_topic

        
        """
        query_string = [('type', 'READ_DATASOURCE'),
                        ('name', 'name_example')]
        response = self.client.open(
            '/v1/topic/{uuid}/sample'.format(uuid='uuid_example'),
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

    def test_snapshot_pipeline(self):
        """Test case for snapshot_pipeline

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/pipeline/{uuid}/snapshot'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_start_pool(self):
        """Test case for start_pool

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/datapipeline/{uuid}/pool/start'.format(uuid='uuid_example'),
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
            '/v1/pipeline/{uuid}/stop'.format(uuid='uuid_example'),
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
            '/v1/datapipeline/{uuid}/pool/stop'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_stop_processor(self):
        """Test case for stop_processor

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/processor/{uuid}/stop'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_un_pause_pipeline(self):
        """Test case for un_pause_pipeline

        
        """
        body = DataPipelineServiceIdentifier()
        response = self.client.open(
            '/v1/pipeline/{uuid}/unpause'.format(uuid='uuid_example'),
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
            '/v1/datapipeline/{uuid}/pool/unpause'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_metrics(self):
        """Test case for update_metrics

        -------------- Metrics ---------------
        """
        body = DataPipelineServiceIdMetrics()
        response = self.client.open(
            '/v1/Identifier/metrics',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
