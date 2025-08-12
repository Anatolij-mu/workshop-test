import pytest
from api.projects import ProjectsAPI


@pytest.fixture(scope="session")
def base_url():
    return "https://yougile.com/api-v2"


@pytest.fixture(scope="session")
def token():
    return "oEatsWirqWHVtsiXJscqutN45Oe-S8Zsgv7p85PNs0bpZu2htBngviq42xqlCO+N"


@pytest.fixture(scope="session")
def projects_api(base_url, token):
    return ProjectsAPI(base_url, token)


@pytest.fixture
def test_project(projects_api):
    project_data = {"title": "TestProject"}
    response = projects_api.create_project(project_data)
    assert response.status_code == 201
    project = response.json()
    yield project["id"]
