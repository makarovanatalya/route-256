import requests

from superhero_api_test_framework.settings import HEADERS, URL


class ApiClient:

    def get_by_id(self, id):

        response = requests.get(
            url=f'{URL}{id}',
            headers=HEADERS,
        )
        return response

    def get_by_powerstats(self, id):

        response = requests.get(
            url=f'{URL}{id}/powerstats',
            headers=HEADERS,
        )
        return response



