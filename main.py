import requests
from config import TOKEN #указать свой токен внутри файла config
from config import URL


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        upload_url = URL
        filename = file_path.split('\\', )[-1]
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
        params = {"path": f"{filename}", "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params).json()
        href = response.get("href", "")
        download_request = requests.put(href, data=open(file_path, 'rb'))
        download_request.raise_for_status()
        if download_request.status_code == 201:
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {download_request.status_code}"


if __name__ == '__main__':
    path_to_file = ... #необходимо указать путь до загружаемого файла
    token = TOKEN
    uploader = YaUploader(token)
    print(f"Загружаем файл {path_to_file.split('/', )[-1]} на Яндекс.Диск")
    result = uploader.upload(path_to_file)
    print(result)
