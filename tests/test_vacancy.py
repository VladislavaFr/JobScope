import pytest
from src.vacancy import Vacancy


def test_vacancy_init():
    v = Vacancy("Python Dev", "link", 100000, "Desc")
    assert v.title == "Python Dev"
    assert v.salary == 100000


def test_vacancy_salary_validation():
    v = Vacancy("Python Dev", "link", None, "Desc")
    assert v.salary == 0


def test_vacancy_comparison():
    v1 = Vacancy("A", "link1", 100, "Desc")
    v2 = Vacancy("B", "link2", 200, "Desc")
    assert v1 < v2
    assert not v2 < v1


def test_cast_to_object_list():
    data = [{"title": "Python Dev", "url": "link", "salary": 100000, "description": "Desc"}]
    objects = Vacancy.cast_to_object_list(data)
    assert isinstance(objects[0], Vacancy)
