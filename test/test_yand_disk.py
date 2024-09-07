import pytest
import requests
from unittest.mock import patch, Mock
from hw_test.yandex_API import create_folder

YANDEX_DISK_TOKEN = ""

@pytest.fixture
def mock_headers():
    return {
        'Authorization': f'OAuth {YANDEX_DISK_TOKEN}'
    }

@pytest.fixture
def mock_create_folder_response():
    mock_response = Mock()
    mock_response.status_code = 201  # Код ответа, когда папка успешно создана
    return mock_response

@pytest.fixture
def mock_list_files_response():
    mock_response = Mock()
    mock_response.status_code = 200  # Код ответа, когда запрос на список файлов успешен
    mock_response.json.return_value = {
        '_embedded': {
            'items': [{'name': 'test_folder', 'type': 'dir'}]
        }
    }
    return mock_response

def test_create_folder_success(mock_headers, mock_create_folder_response):
    with patch('requests.put', return_value=mock_create_folder_response):
        response = create_folder('/test_folder')
        assert response.status_code == 201

def test_create_folder_failure(mock_headers):
    mock_response = Mock()
    mock_response.status_code = 400  # Код ответа для ошибки
    with patch('requests.put', return_value=mock_response):
        response = create_folder('/test_folder')
        assert response.status_code == 400

def test_folder_appears_in_list(mock_headers, mock_create_folder_response, mock_list_files_response):
    # Создаем папку
    with patch('requests.put', return_value=mock_create_folder_response):
        create_folder('/test_folder')

    # Проверяем список файлов
    with patch('requests.get', return_value=mock_list_files_response):
        response = requests.get(f'https://cloud-api.yandex.net:443/v1/disk/resources?path=/')
        assert response.status_code == 200
        files_list = response.json()['_embedded']['items']
        assert any(file['name'] == 'test_folder' for file in files_list)
