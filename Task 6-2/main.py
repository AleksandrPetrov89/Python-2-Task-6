import requests


def folder_creation(token, fold_name):
    """
    Создает папку с заданным именем в корневом каталоге Яндекс.Диска
    :param token: токен для работы с API Яндекс.Диска
    :param fold_name: имя создаваемой папки
    :return: ответ API Яндекс.Диска на запрос о создании папки
    """
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
               'Authorization': token}
    params = {'path': fold_name}
    response = requests.put(url, params=params, headers=headers)
    return response


if __name__ == '__main__':
    ya_disk_token = "токен Яндекс.Диска"
    folder_name = "Test"
    result = folder_creation(ya_disk_token, folder_name)
