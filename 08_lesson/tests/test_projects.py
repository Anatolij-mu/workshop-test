class TestProjects:
    def test_create_project_positive(self, projects_api, sample_project_data):
        """Позитивный тест создания проекта"""
        response = projects_api.create_project(sample_project_data)
        assert response.status_code == 201
        assert "id" in response.json()

    def test_create_project_negative_missing_required_field(
            self, projects_api, sample_project_data):
        """Негативный тест создания проекта - отсутствует обязательное поле"""
        invalid_data = sample_project_data.copy()
        del invalid_data["name"]
        response = projects_api.create_project(invalid_data)
        assert response.status_code == 400

    def test_get_project_positive(self, projects_api, sample_project_data):
        """Позитивный тест получения проекта"""
        create_response = projects_api.create_project(sample_project_data)
        project_id = create_response.json()["id"]

        response = projects_api.get_project(project_id)
        assert response.status_code == 200
        assert response.json()["id"] == project_id

    def test_get_project_negative_not_found(self, projects_api):
        """Негативный тест получения проекта - проект не найден"""
        response = projects_api.get_project("nonexistent_id")
        assert response.status_code == 404

    def test_update_project_positive(self, projects_api, sample_project_data):
        """Позитивный тест обновления проекта"""
        create_response = projects_api.create_project(sample_project_data)
        project_id = create_response.json()["id"]

        update_data = {"name": "Updated Project Name"}
        response = projects_api.update_project(project_id, update_data)
        assert response.status_code == 200
        assert response.json()["name"] == "Updated Project Name"

    def test_update_project_negative_invalid_data(
            self, projects_api, sample_project_data):
        """Негативный тест обновления проекта - неверные данные"""
        create_response = projects_api.create_project(sample_project_data)
        project_id = create_response.json()["id"]

        invalid_data = {"start_date": "invalid-date-format"}
        response = projects_api.update_project(project_id, invalid_data)
        assert response.status_code == 400
