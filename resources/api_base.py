import requests

class ApiBase():
    BASE_URL = "https://petstore.swagger.io/v2"

    def get(self, path, params=None, headers=None):
        url = self.BASE_URL + path
        response = requests.get(url, params=params, headers=headers)
        return response

    def post(self, path, params=None, json=None, data=None, headers=None):
        url = self.BASE_URL + path
        response = requests.post(url, params=params, json=json, data=data, headers=headers)
        return response

    def put(self, path, params=None, json=None, headers=None):
        url = self.BASE_URL + path
        response = requests.put(url, params=params, json=json, headers=headers)
        return response

    def delete(self, path, params=None, headers=None):
        url = self.BASE_URL + path
        response = requests.delete(url, params=params, headers=headers)
        return response