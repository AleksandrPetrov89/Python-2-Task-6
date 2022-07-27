import pytest
import requests
from main import folder_creation


class TestsFolderCreation:

    token = "токен Яндекс.Диска"

    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
               'Authorization': token}

    fixture = ["Test1", "Test2"]

    # Проверяем, что директорий с таким именем в корневом каталоге Яндекс.Диска нет
    @pytest.mark.parametrize("folder_name", fixture)
    def test_folder_creation_before_creation_status_code_404(self, folder_name):
        params = {"path": folder_name}
        assert requests.get(self.url, params=params, headers=self.headers).status_code == 404

    fixture = [
        ("Test1", 201, 1),
        ("Test2", 201, 1),
        ("Test1", 409, 0),
        ("Test2", 409, 0),
    ]

    # Тест на код ответа и увеличение количества элементов в корневом каталоге Яндекс.Диска
    @pytest.mark.parametrize("folder_name, status_code, counter", fixture)
    def test_folder_creation(self, folder_name, status_code, counter):
        params = {"path": "disk:/"}
        response = dict(requests.get(self.url, params=params, headers=self.headers).json())
        amount = len(response["_embedded"]["items"])
        assert folder_creation(self.token, folder_name).status_code == status_code
        response = dict(requests.get(self.url, params=params, headers=self.headers).json())
        assert len(response["_embedded"]["items"]) == amount + counter

    fixture = [
        ("Test1", 200),
        ("Test2", 200),
        ("Test3", 404),
        ("Test4", 404),
    ]

    # Проверяем, что запрос метаинформации о тестируемых директориях возвращает код 200
    @pytest.mark.parametrize("folder_name, status_code", fixture)
    def test_folder_creation_after_creation(self, folder_name, status_code):
        params = {"path": folder_name}
        assert requests.get(self.url, params=params, headers=self.headers).status_code == status_code

    fixture = ["Test1", "Test2"]

    # Проверяем, что папки с указанными именами в корневом каталоге Яндекс.Диска теперь есть и удаляем их
    @pytest.mark.parametrize("folder_name", fixture)
    def test_folder_creation_after_creation_folder_name(self, folder_name):
        params = {"path": folder_name}
        response = dict(requests.get(self.url, params=params, headers=self.headers).json())
        assert response["name"] == folder_name
        params = {"path": folder_name, "permanently": "true"}
        requests.delete(self.url, params=params, headers=self.headers)
