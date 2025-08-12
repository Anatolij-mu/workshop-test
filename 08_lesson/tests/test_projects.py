def test_create_project_positive(projects_api):
    data = {"title": "New Project"}
    response = projects_api.create_project(data)
    assert response.status_code == 201
    assert "id" in response.json()


def test_get_project_positive(projects_api, test_project):
    response = projects_api.get_project(test_project)
    assert response.status_code == 200
    assert response.json()["id"] == test_project


def test_update_project_positive(projects_api, test_project):
    new_title = "Updated_TestProject"

    update_response = projects_api.update_project(
        test_project,
        {"title": new_title}
    )
    assert update_response.status_code == 200
    updated_project = projects_api.get_project(test_project).json()
    assert updated_project["title"] == new_title


def test_create_project_negative(projects_api):
    data = {}
    response = projects_api.create_project(data)
    assert response.status_code == 400


def test_get_project_negative(projects_api):
    response = projects_api.get_project("invalid_project_id")
    assert response.status_code == 404


def test_update_project_negative(projects_api):
    data = {"title": "Valid Title"}
    response = projects_api.update_project("invalid_project_id", data)
    assert response.status_code == 404
