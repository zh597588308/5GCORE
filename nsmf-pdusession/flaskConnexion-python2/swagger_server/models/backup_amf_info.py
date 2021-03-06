# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.amf_name import AmfName  # noqa: F401,E501
from swagger_server.models.guami import Guami  # noqa: F401,E501
from swagger_server import util


class BackupAmfInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, backup_amf=None, guami_list=None):  # noqa: E501
        """BackupAmfInfo - a model defined in Swagger

        :param backup_amf: The backup_amf of this BackupAmfInfo.  # noqa: E501
        :type backup_amf: AmfName
        :param guami_list: The guami_list of this BackupAmfInfo.  # noqa: E501
        :type guami_list: List[Guami]
        """
        self.swagger_types = {
            'backup_amf': AmfName,
            'guami_list': List[Guami]
        }

        self.attribute_map = {
            'backup_amf': 'backupAmf',
            'guami_list': 'guamiList'
        }
        self._backup_amf = backup_amf
        self._guami_list = guami_list

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BackupAmfInfo of this BackupAmfInfo.  # noqa: E501
        :rtype: BackupAmfInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def backup_amf(self):
        """Gets the backup_amf of this BackupAmfInfo.


        :return: The backup_amf of this BackupAmfInfo.
        :rtype: AmfName
        """
        return self._backup_amf

    @backup_amf.setter
    def backup_amf(self, backup_amf):
        """Sets the backup_amf of this BackupAmfInfo.


        :param backup_amf: The backup_amf of this BackupAmfInfo.
        :type backup_amf: AmfName
        """
        if backup_amf is None:
            raise ValueError("Invalid value for `backup_amf`, must not be `None`")  # noqa: E501

        self._backup_amf = backup_amf

    @property
    def guami_list(self):
        """Gets the guami_list of this BackupAmfInfo.


        :return: The guami_list of this BackupAmfInfo.
        :rtype: List[Guami]
        """
        return self._guami_list

    @guami_list.setter
    def guami_list(self, guami_list):
        """Sets the guami_list of this BackupAmfInfo.


        :param guami_list: The guami_list of this BackupAmfInfo.
        :type guami_list: List[Guami]
        """

        self._guami_list = guami_list
