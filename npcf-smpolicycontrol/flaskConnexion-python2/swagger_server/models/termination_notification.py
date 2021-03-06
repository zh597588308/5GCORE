# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.policy_association_release_cause import PolicyAssociationReleaseCause  # noqa: F401,E501
from swagger_server.models.uri import Uri  # noqa: F401,E501
from swagger_server import util


class TerminationNotification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, resource_uri=None, cause=None):  # noqa: E501
        """TerminationNotification - a model defined in Swagger

        :param resource_uri: The resource_uri of this TerminationNotification.  # noqa: E501
        :type resource_uri: Uri
        :param cause: The cause of this TerminationNotification.  # noqa: E501
        :type cause: PolicyAssociationReleaseCause
        """
        self.swagger_types = {
            'resource_uri': Uri,
            'cause': PolicyAssociationReleaseCause
        }

        self.attribute_map = {
            'resource_uri': 'resourceUri',
            'cause': 'cause'
        }
        self._resource_uri = resource_uri
        self._cause = cause

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TerminationNotification of this TerminationNotification.  # noqa: E501
        :rtype: TerminationNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resource_uri(self):
        """Gets the resource_uri of this TerminationNotification.


        :return: The resource_uri of this TerminationNotification.
        :rtype: Uri
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this TerminationNotification.


        :param resource_uri: The resource_uri of this TerminationNotification.
        :type resource_uri: Uri
        """
        if resource_uri is None:
            raise ValueError("Invalid value for `resource_uri`, must not be `None`")  # noqa: E501

        self._resource_uri = resource_uri

    @property
    def cause(self):
        """Gets the cause of this TerminationNotification.


        :return: The cause of this TerminationNotification.
        :rtype: PolicyAssociationReleaseCause
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this TerminationNotification.


        :param cause: The cause of this TerminationNotification.
        :type cause: PolicyAssociationReleaseCause
        """
        if cause is None:
            raise ValueError("Invalid value for `cause`, must not be `None`")  # noqa: E501

        self._cause = cause
