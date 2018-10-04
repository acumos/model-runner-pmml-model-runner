import connexion
import six

from swagger_server.models.data_pipeline_service_empty import DataPipelineServiceEmpty  # noqa: E501
from swagger_server.models.data_pipeline_service_identifier import DataPipelineServiceIdentifier  # noqa: E501
from swagger_server.models.data_pipeline_service_pools import DataPipelineServicePools  # noqa: E501
from swagger_server.models.data_pipeline_service_state import DataPipelineServiceState  # noqa: E501
from swagger_server import util


def create_pool(body):  # noqa: E501
    """------------------- DATA PIPELINE POOLS ----------------

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DataPipelineServiceIdentifier
    """
    if connexion.request.is_json:
        body = DataPipelineServiceIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_pool(body):  # noqa: E501
    """delete_pool

     # noqa: E501

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


def shutdown():  # noqa: E501
    """SHUTDOWN SERVICE

     # noqa: E501


    :rtype: DataPipelineServiceEmpty
    """
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
