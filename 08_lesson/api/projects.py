import requests


class ProjectsAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, data):
        response = requests.post(
            f"{self.base_url}/projects",
            json=data,
            headers=self.headers
        )
        return response

    def get_project(self, project_id):
        response = requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
        return response

    def update_project(self, project_id, data):
        response = requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=data,
            headers=self.headers
        )
        return response
