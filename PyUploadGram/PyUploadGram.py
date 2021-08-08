import requests
from typing import Union
from json.decoder import JSONDecodeError


class UploadedFile:
    def __init__(self, resp: dict):
        self.url = f"{resp['url']}?raw"
        self.delete = resp['delete']

    @property
    def url_without_raw(self):
        return self.url.split('?')[0]

    def __repr__(self):
        return f"(UploadedFile: url={self.url}, delete={self.delete})"


class Session:
    _HOST = "https://api.uploadgram.me"

    def __init__(self,
                 proxies: dict = None,
                 headers: dict = None):
        if headers is None:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0)'}
        if proxies is None:
            proxies = {}
        self.s = requests.Session()
        self.s.headers = headers
        self.s.proxies = proxies
        self.uploaded_files = []

    def upload_file(self, filename: str, file: Union[str, bytes]) -> UploadedFile:
        if isinstance(file, str):
            if file.startswith("http"):
                b_file = self.s.get(file).content
            else:
                with open(file, 'rb') as f:
                    b_file = f.read()
        elif isinstance(file, bytes):
            b_file = file
        else:
            raise NotImplementedError

        files = {"file_upload": (filename, b_file, None)}
        resp = self.s.post(f"{self._HOST}/upload", files=files).json()
        if not bool(resp.get("ok")):
            raise Exception(resp)
        uploaded_file = UploadedFile(resp)
        self.uploaded_files.append(uploaded_file)
        return uploaded_file

    def delete_file(self, uploaded_file: UploadedFile) -> bool:
        try:
            response = self.s.get(f'{self._HOST}/delete/{uploaded_file.delete}').json()
        except JSONDecodeError:
            return False
        return response.get("ok", False)


def upload_file(filename: str, file: Union[str, bytes]) -> UploadedFile:
    return Session().upload_file(**locals())


def delete_file(uploaded_file: UploadedFile) -> None:
    Session().delete_file(**locals())
