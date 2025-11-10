from src.vacancy import Vacancy


def filter_vacancies(vacancies: list[Vacancy], keyword: str):
    """Фильтрует вакансии по ключевому слову в описании"""
    return [v for v in vacancies if keyword.lower() in v.description.lower()]


def sort_vacancies_by_salary(vacancies: list[Vacancy], reverse=True):
    """Сортировка по зарплате"""
    return sorted(vacancies, key=lambda v: v.salary, reverse=reverse)


def get_top_vacancies(vacancies: list[Vacancy], top_n: int):
    """Возвращает топ N вакансий"""
    return vacancies[:top_n]
