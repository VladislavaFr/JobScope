from src.vacancy import Vacancy
from src.utils import filter_vacancies, sort_vacancies_by_salary, get_top_vacancies

def test_filter_vacancies():
    v = [Vacancy("A", "url", 10, "Python developer")]
    result = filter_vacancies(v, "python")
    assert len(result) == 1

def test_sort_vacancies_by_salary():
    v1 = Vacancy("A", "url", 10, "desc")
    v2 = Vacancy("B", "url", 20, "desc")
    sorted_v = sort_vacancies_by_salary([v1, v2])
    assert sorted_v[0].salary == 20
    assert sorted_v[1].salary == 10

def test_get_top_vacancies():
    v = [Vacancy("A", "url", 10, "desc"), Vacancy("B", "url", 20, "desc")]
    top = get_top_vacancies(v, 1)
    assert len(top) == 1
    assert top[0].title == "B"
