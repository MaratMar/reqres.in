import requests

""" Методы для тестирования API """


class Reqres_api():

    @staticmethod
    def get_request(url):
        return requests.get(url)

    @staticmethod
    def post_request(url, json_body):
        return requests.post(url, json_body)

    @staticmethod
    def put_request(url, json_body):
        return requests.put(url, json_body)

    @staticmethod
    def patch_request(url, json_body):
        return requests.patch(url, json_body)

    @staticmethod
    def delete_request(url):
        return requests.delete(url)
