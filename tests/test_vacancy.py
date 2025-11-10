import pytest
from src.vacancy import Vacancy

def test_vacancy_init_and_to_dict():
    v = Vacancy("Python Dev", "http://example.com", 100000, "Разработка")
    assert v.to_dict()["title"] == "Python Dev"
    assert isinstance(str(v), str)
    assert repr(v) == f"Vacancy(title='Python Dev', salary=100000)"

def test_vacancy_comparison():
    v1 = Vacancy("A", "url1", 100, "desc")
    v2 = Vacancy("B", "url2", 200, "desc")
    assert v1 < v2
    assert not (v2 < v1)
    assert v1 != v2

def test_cast_to_object_list():
    data = [{"title": "A", "url": "U", "salary": 10, "description": "D"}]
    objs = Vacancy.cast_to_object_list(data)
    assert isinstance(objs[0], Vacancy)
    assert objs[0].title == "A"
