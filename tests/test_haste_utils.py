import pytest
import requests
from hastebin_client.utils import create_url, read_data, upload
from unittest import mock


def test_create_url():
    assert create_url('key') == 'https://hastebin.com/key'
    with pytest.raises(ValueError):
        create_url(None)


def test_read_data_stdin():
    with mock.patch('sys.stdin.read', mock.Mock(return_value='data')) as mock_read:
        result = read_data()
        mock_read.assert_called_once_with()
    assert result == 'data'


def test_read_data_stdin_abort():
    with mock.patch('sys.stdin.read', mock.Mock(side_effect=KeyboardInterrupt)):
        result = read_data()
    assert result == ''


def test_read_data_file():
    with mock.patch('builtins.open', mock.mock_open(read_data='data')) as mock_open:
        result = read_data('file')
        mock_open.assert_called_once_with('file', 'r')
    assert result == 'data'


def test_upload():
    with mock.patch('requests.post') as post_function:
        post_function.return_value.json.return_value = {'key': 'lonely-ranger'}
        result = upload('test data')
    assert result == 'lonely-ranger'


def test_upload_timeout():
    post_mock = mock.Mock(side_effect=requests.exceptions.Timeout('Request timed out!'))
    with mock.patch('requests.post', post_mock):
        result = upload('test data')
    assert result is None


def test_upload_error():
    with mock.patch('requests.post') as post_function:
        post_function.return_value.json.side_effect = ValueError('Invalid JSON')
        result = upload('test data')
    assert result is None


def test_upload_too_big():
    with mock.patch('requests.post') as post_function:
        post_function.return_value.json.return_value = {'message': 'Document exceeds maximum length.'}
        result = upload('test data')
    assert result is None

