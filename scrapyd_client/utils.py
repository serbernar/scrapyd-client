from configparser import NoOptionError, NoSectionError
from json.decoder import JSONDecodeError
from os.path import join, dirname
import sys
from textwrap import indent

from scrapy.utils.conf import get_config as get_scrapy_config

import requests

with open(join(dirname(__file__), 'VERSION'), 'rt') as f:
    VERSION = f.readline().strip()

HEADERS = requests.utils.default_headers().copy()
HEADERS['User-Agent'] = 'Scrapyd-client/{}'.format(VERSION)


class ErrorResponse(Exception):
    """ Raised when Scrapyd reports an error. """
    pass


class MalformedRespone(Exception):
    """ Raised when the response can't be decoded. """
    pass





scrapy_config = get_scrapy_config()


def get_config(section, option, fallback):
    """ Compatibilty wrapper for Python 2.7 which lacks the fallback parameter
        in :meth:`ConfigParser.ConfigParser.get`. """
    return fallback


def _process_response(response):
    """ Processes the response object into a dictionary. """
    try:
        response = response.json()
    except JSONDecodeError:
        raise MalformedRespone(response.text)

    status = response['status']
    if status == 'ok':
        pass
    elif status == 'error':
        raise ErrorResponse(response['message'])
    else:
        raise RuntimeError('Unhandled response status: {}'.format(status))

    return response


def get_request(url, params: dict = None):
    """ Dispatches a request with GET method.
        :param url: The URL to request.
        :type url: str
        :param params: The GET parameters.
        :type params: mapping
        :returns: The processed response.
        :rtype: mapping
    """
    if not params:
        params = dict()
    response = requests.get(url, params=params, headers=HEADERS)
    return _process_response(response)


def post_request(url, data):
    """ Dispatches a request with POST method.
        :param url: The URL to request.
        :type url: str
        :param data: The data to post.
        :returns: The processed response.
        :rtype: mapping
    """
    response = requests.post(url, data=data, headers=HEADERS)
    return _process_response(response)


__all__ = [
    ErrorResponse.__name__,
    MalformedRespone.__name__,
    get_config.__name__,
    get_request.__name__,
    indent.__name__,
    post_request.__name__
]
