from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.storage import JSONSaver
from src.utils import filter_vacancies, sort_vacancies_by_salary, get_top_vacancies


def user_interaction():
    """Простое взаимодействие с пользователем"""
    query = input("Введите поисковый запрос: ")
    top_n = int(input("Сколько вакансий показать? "))

    api = HeadHunterAPI()
    saver = JSONSaver()

    print("\nЗагружаем данные с hh.ru...\n")
    vacancies_raw = api.get_vacancies(query, per_page=top_n)
    vacancies = []

    for v in vacancies_raw:
        salary_info = v.get("salary") or {}
        salary = salary_info.get("from") or salary_info.get("to") or 0
        vacancy = Vacancy(
            title=v.get("name", "Без названия"),
            url=v.get("alternate_url", ""),
            salary=salary,
            description=v.get("snippet", {}).get("requirement", "") or "",
        )
        saver.add_vacancy(vacancy.to_dict())
        vacancies.append(vacancy)

    vacancies = sort_vacancies_by_salary(vacancies)
    top = get_top_vacancies(vacancies, top_n)

    print("\nТоп вакансий:")
    for v in top:
        print(f"{v.title} — {v.salary}₽ — {v.url}")
