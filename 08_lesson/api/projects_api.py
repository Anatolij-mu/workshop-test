from .base_api import BaseAPI


class ProjectsAPI(BaseAPI):
    def create_project(self, project_data):
        """[POST] /api-v2/projects"""
        return self._request("POST", "/api-v2/projects", json=project_data)

    def get_project(self, project_id):
        """[GET] /api-v2/projects/{id}"""
        return self._request("GET", f"/api-v2/projects/{project_id}")

    def update_project(self, project_id, update_data):
        """[PUT] /api-v2/projects/{id}"""
        return self._request(
            "PUT", f"/api-v2/projects/{project_id}", json=update_data)
