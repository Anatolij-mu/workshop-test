import pytest
from api.projects_api import ProjectsAPI


@pytest.fixture
def projects_api():
    return ProjectsAPI()


@pytest.fixture
def sample_project_data():
    return {
        "name": "Test Project",
        "description": "This is a test project",
        "start_date": "2023-01-01",
        "end_date": "2023-12-31"
    }
