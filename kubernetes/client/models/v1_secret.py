# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.0-beta.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1Secret(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, data=None, metadata=None, string_data=None, type=None):
        """
        V1Secret - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data': 'dict(str, str)',
            'metadata': 'V1ObjectMeta',
            'string_data': 'dict(str, str)',
            'type': 'str'
        }

        self.attribute_map = {
            'data': 'data',
            'metadata': 'metadata',
            'string_data': 'stringData',
            'type': 'type'
        }

        self._data = data
        self._metadata = metadata
        self._string_data = string_data
        self._type = type


    @property
    def data(self):
        """
        Gets the data of this V1Secret.
        Data contains the secret data. Each key must be a valid DNS_SUBDOMAIN or leading dot followed by valid DNS_SUBDOMAIN. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4

        :return: The data of this V1Secret.
        :rtype: dict(str, str)
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this V1Secret.
        Data contains the secret data. Each key must be a valid DNS_SUBDOMAIN or leading dot followed by valid DNS_SUBDOMAIN. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4

        :param data: The data of this V1Secret.
        :type: dict(str, str)
        """

        self._data = data

    @property
    def metadata(self):
        """
        Gets the metadata of this V1Secret.
        Standard object's metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :return: The metadata of this V1Secret.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1Secret.
        Standard object's metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :param metadata: The metadata of this V1Secret.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def string_data(self):
        """
        Gets the string_data of this V1Secret.
        stringData allows specifying non-binary secret data in string form. It is provided as a write-only convenience method. All keys and values are merged into the data field on write, overwriting any existing values. It is never output when reading from the API.

        :return: The string_data of this V1Secret.
        :rtype: dict(str, str)
        """
        return self._string_data

    @string_data.setter
    def string_data(self, string_data):
        """
        Sets the string_data of this V1Secret.
        stringData allows specifying non-binary secret data in string form. It is provided as a write-only convenience method. All keys and values are merged into the data field on write, overwriting any existing values. It is never output when reading from the API.

        :param string_data: The string_data of this V1Secret.
        :type: dict(str, str)
        """

        self._string_data = string_data

    @property
    def type(self):
        """
        Gets the type of this V1Secret.
        Used to facilitate programmatic handling of secret data.

        :return: The type of this V1Secret.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1Secret.
        Used to facilitate programmatic handling of secret data.

        :param type: The type of this V1Secret.
        :type: str
        """

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
