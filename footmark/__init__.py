#
import logging
import logging.config
import os

from footmark.pyami.config import Config, FootmarkLoggingConfig, DefaultLoggingConfig

__version__ = '1.1.4'
Version = __version__  # for backware compatibility


def init_logging():
    try:
        Config().init_config()
        try:
            logging.config.fileConfig(os.path.expanduser(FootmarkLoggingConfig))
        except:
            logging.config.dictConfig(DefaultLoggingConfig)
    except:
        pass

init_logging()
log = logging.getLogger('footmark')


def connect_ecs(acs_access_key_id=None, acs_secret_access_key=None, **kwargs):
    """
    :type acs_access_key_id: string
    :param acs_access_key_id: Your Aliyun Access Key ID

    :type acs_secret_access_key: string
    :param acs_secret_access_key: Your Aliyun Secret Access Key

    :rtype: :class:`footmark.ecs.connection.ECSConnection`
    :return: A connection to Aliyun's ECS
    """
    from footmark.ecs.connection import ECSConnection
    return ECSConnection(acs_access_key_id, acs_secret_access_key, **kwargs)


def connect_slb(acs_access_key_id=None, acs_secret_access_key=None, **kwargs):
    """
    :type acs_access_key_id: string
    :param acs_access_key_id: Your Aliyun Access Key ID

    :type acs_secret_access_key: string
    :param acs_secret_access_key: Your Aliyun Secret Access Key

    :rtype: :class:`footmark.ecs.connection.ECSConnection`
    :return: A connection to Aliyun's SLB
    """
    from footmark.slb.connection import SLBConnection
    return SLBConnection(acs_access_key_id, acs_secret_access_key, **kwargs)


def connect_vpc(acs_access_key_id=None, acs_secret_access_key=None, **kwargs):
    """
    :type acs_access_key_id: string
    :param acs_access_key_id: Your Aliyun Access Key ID

    :type acs_secret_access_key: string
    :param acs_secret_access_key: Your Aliyun Secret Access Key

    :rtype: :class:`footmark.vpc.connection.ECSConnection`
    :return: A connection to Aliyun's VPC
    """
    from footmark.vpc.connection import VPCConnection
    return VPCConnection(acs_access_key_id, acs_secret_access_key, **kwargs)

