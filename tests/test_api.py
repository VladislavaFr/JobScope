import pytest
from src.hh_api import HeadHunterAPI
from unittest.mock import patch


@pytest.fixture
def hh_api():
    return HeadHunterAPI()


def test_base_url_private(hh_api):
    # Проверяем, что атрибут __base_url приватный
    assert hasattr(hh_api, "_HeadHunterAPI__base_url")


@patch("src.hh_api.requests.get")
def test_get_vacancies(mock_get, hh_api):
    mock_get.return_value.json.return_value = {"items": [{"title": "Python Dev", "url": "link"}]}
    mock_get.return_value.raise_for_status = lambda: None

    result = hh_api.get_vacancies("Python")
    assert isinstance(result, list)
    assert result[0]["title"] == "Python Dev"
