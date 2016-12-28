import logging
import requests
import sys
from .config import haste_config


def read_data(filename=None):
    if filename:
        with open(filename, 'r') as f:
            return f.read()

    # If trying to read from console:
    try:
        return sys.stdin.read()
    except KeyboardInterrupt:
        return ''


def upload(data):
    url = '{protocol}://{domain}/{path}'.format(**haste_config)
    try:
        response = requests.post(url, data=data)
    except requests.exceptions.RequestException as e:
        logging.error("Coudn't connect to hastebin:\n{}".format(e))
        return None

    try:
        return response.json()['key']
    except ValueError as e:
        logging.error("Couldn't parse response from hastebin:\n{}".format(response.content.decode()))
    except KeyError:
        message = response.json().get('message', response.content.decode())
        logging.error("Failed! Response from hastebin:\n{}".format(message))


def create_url(haste_key):
    if not haste_key:
        raise ValueError('Attempted to create an empty haste url')
    return '{protocol}://{domain}/{key}'.format(key=haste_key, **haste_config)
