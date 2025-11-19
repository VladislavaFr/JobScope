import pytest
import os
from src.storage import JSONSaver


@pytest.fixture
def json_saver(tmp_path):
    file_path = tmp_path / "vacancies.json"
    return JSONSaver(str(file_path))


def test_filename_private(json_saver):
    assert hasattr(json_saver, "_JSONSaver__filename")


def test_add_get_delete(json_saver):
    vacancy = {"title": "Python Dev", "url": "link", "salary": 100000, "description": "Desc"}

    json_saver.add_vacancy(vacancy)
    data = json_saver.get_all_vacancies()
    assert data[0]["title"] == "Python Dev"

    json_saver.delete_vacancy("Python Dev")
    data = json_saver.get_all_vacancies()
    assert data == []
