import os
import pytest
from src.storage import JSONSaver

def test_jsonsaver_add_and_get(tmp_path):
    file = tmp_path / "vacancies.json"
    saver = JSONSaver(str(file))

    vacancy = {"title": "Python Dev", "url": "url", "salary": 100, "description": "desc"}
    saver.add_vacancy(vacancy)

    data = saver.get_all_vacancies()
    assert data[0]["title"] == "Python Dev"

def test_delete_vacancy(tmp_path):
    file = tmp_path / "vacancies.json"
    saver = JSONSaver(str(file))

    vacancy = {"title": "ToDelete", "url": "url", "salary": 50, "description": "desc"}
    saver.add_vacancy(vacancy)

    saver.delete_vacancy("ToDelete")
    assert saver.get_all_vacancies() == []

def test_no_duplicate_add(tmp_path):
    file = tmp_path / "vacancies.json"
    saver = JSONSaver(str(file))

    vacancy = {"title": "Dup", "url": "url", "salary": 10, "description": "desc"}
    saver.add_vacancy(vacancy)
    saver.add_vacancy(vacancy)

    data = saver.get_all_vacancies()
    assert len(data) == 1
