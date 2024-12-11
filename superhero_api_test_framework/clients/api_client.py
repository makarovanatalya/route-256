import requests

from superhero_api_test_framework.settings import HEADERS, URL


class ApiClient:

    def _send_get_response(self, endpoint):
        return requests.get(
            url=f'{URL}{endpoint}',
            headers=HEADERS,
        )

    def get_by_id(self, id):
        return self._send_get_response(id)

    def get_by_powerstats(self, id):
        return self._send_get_response(f'{id}/powerstats')
