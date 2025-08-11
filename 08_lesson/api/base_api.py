import requests
import os


class BaseAPI:
    def __init__(self):
        self.base_url = "https://api.example.com"
        self.token = os.getenv("API_TOKEN")

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def _request(self, method, endpoint, json=None, params=None):
        url = f"{self.base_url}{endpoint}"
        headers = self._get_headers()

        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=json,
            params=params
        )

        return response
