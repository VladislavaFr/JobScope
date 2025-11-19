from src.utils import filter_vacancies, sort_vacancies_by_salary, get_top_vacancies
from src.vacancy import Vacancy


def test_filter_vacancies():
    vac1 = Vacancy("A", "link1", 100, "Python")
    vac2 = Vacancy("B", "link2", 200, "Java")
    filtered = filter_vacancies([vac1, vac2], "Python")
    assert filtered == [vac1]


def test_sort_vacancies_by_salary():
    vac1 = Vacancy("A", "link1", 100, "Desc")
    vac2 = Vacancy("B", "link2", 200, "Desc")
    sorted_list = sort_vacancies_by_salary([vac1, vac2])
    assert sorted_list[0] == vac2  # reverse=True по умолчанию


def test_get_top_vacancies():
    vac1 = Vacancy("A", "link1", 100, "Desc")
    vac2 = Vacancy("B", "link2", 200, "Desc")
    top = get_top_vacancies([vac2, vac1], 1)
    assert top == [vac2]
