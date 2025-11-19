from typing import List
from .vacancy import Vacancy


def filter_vacancies(vacancies: List[Vacancy], keyword: str) -> List[Vacancy]:
    """Фильтрует вакансии по ключевому слову в описании"""
    return [v for v in vacancies if keyword.lower() in v.description.lower()]


def sort_vacancies_by_salary(vacancies: List[Vacancy], reverse: bool = True) -> List[Vacancy]:
    """Сортирует вакансии по зарплате"""
    return sorted(vacancies, reverse=reverse)


def get_top_vacancies(vacancies: List[Vacancy], n: int) -> List[Vacancy]:
    """Возвращает топ N вакансий"""
    return vacancies[:n]
