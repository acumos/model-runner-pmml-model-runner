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

import connexion
import six

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
from swagger_server import util


def archive_processor(uuid, body):  # noqa: E501
    """archive_processor

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def associate_processor_to_sink_topic(body):  # noqa: E501
    """associate_processor_to_sink_topic

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceProcessorTopic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_pipeline(body):  # noqa: E501
    """create_pipeline

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_pool(body):  # noqa: E501
    """Create A datapipeline Pool for a set of pipelines . Pipelines are always associated with a pool. A pool can have 0 or more pipelines

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_processor(body):  # noqa: E501
    """create_processor

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceProcessorPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_topic(body):  # noqa: E501
    """create_topic

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceTopic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_pipeline(uuid, body):  # noqa: E501
    """delete_pipeline

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceState
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_pool(uuid, body):  # noqa: E501
    """Delete A Data Pipeline pool , To delete a pool, all pipelines in the pool must be deleted

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceState
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def list_all_pools():  # noqa: E501
    """list_all_pools

     # noqa: E501


    :rtype: DataPipelineServicePools
    """
    return 'do some magic!'


def list_objects_in_pool(uuid, type=None, name=None):  # noqa: E501
    """list_objects_in_pool

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param type: 
    :type type: str
    :param name: 
    :type name: str

    :rtype: DataPipelineServiceObjects
    """
    return 'do some magic!'


def pause_pipeline(uuid, body):  # noqa: E501
    """pause_pipeline

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceState
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def pause_pool(uuid, body):  # noqa: E501
    """pause_pool

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceState
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def pause_processor(uuid, body):  # noqa: E501
    """pause_processor

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def re_start_processor(uuid, body):  # noqa: E501
    """re_start_processor

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def register_data_source(body):  # noqa: E501
    """register_data_source

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceDataSource.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def register_data_source_to_pool(body):  # noqa: E501
    """register_data_source_to_pool

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceDataSourcePool.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def register_topic_for_data_source(body):  # noqa: E501
    """register_topic_for_data_source

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceTopicDataSource.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def restore_pipeline_snapshot(uuid, body):  # noqa: E501
    """restore_pipeline_snapshot

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def retrieve_metrics(ident_uuid=None, ident_type=None, ident_name=None):  # noqa: E501
    """retrieve_metrics

     # noqa: E501

    :param ident_uuid: 
    :type ident_uuid: str
    :param ident_type: 
    :type ident_type: str
    :param ident_name: 
    :type ident_name: str

    :rtype: DataPipelineServiceIdentifier
    """
    return 'do some magic!'


def run_pipeline(uuid, body):  # noqa: E501
    """run_pipeline

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceState
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def run_processor(uuid, body):  # noqa: E501
    """run_processor

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def sample_data_source(uuid, type=None, name=None):  # noqa: E501
    """sample_data_source

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param type: 
    :type type: str
    :param name: 
    :type name: str

    :rtype: DataPipelineServiceExtract
    """
    return 'do some magic!'


def sample_topic(uuid, type=None, name=None):  # noqa: E501
    """sample_topic

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param type: 
    :type type: str
    :param name: 
    :type name: str

    :rtype: DataPipelineServiceExtract
    """
    return 'do some magic!'


def shutdown():  # noqa: E501
    """SHUTDOWN SERVICE

     # noqa: E501


    :rtype: DataPipelineServiceEmpty
    """
    return 'do some magic!'


def snapshot_pipeline(uuid, body):  # noqa: E501
    """snapshot_pipeline

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def start_pool(uuid, body):  # noqa: E501
    """start_pool

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceState
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def startup():  # noqa: E501
    """START SERVICE

     # noqa: E501


    :rtype: DataPipelineServiceState
    """
    return 'do some magic!'


def status():  # noqa: E501
    """CHECK STATUS OF SERVICE HEALTH

     # noqa: E501


    :rtype: DataPipelineServiceState
    """
    return 'do some magic!'


def stop_pipeline(uuid, body):  # noqa: E501
    """stop_pipeline

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceState
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def stop_pool(uuid, body):  # noqa: E501
    """stop_pool

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceState
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def stop_processor(uuid, body):  # noqa: E501
    """stop_processor

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def un_pause_pipeline(uuid, body):  # noqa: E501
    """un_pause_pipeline

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceState
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def un_pause_pool(uuid, body):  # noqa: E501
    """un_pause_pool

     # noqa: E501

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceState
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_metrics(body):  # noqa: E501
    """-------------- Metrics ---------------

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdMetrics.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
