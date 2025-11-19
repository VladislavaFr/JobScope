from typing import List
from .hh_api import HeadHunterAPI
from .vacancy import Vacancy
from .storage import JSONSaver
from .utils import filter_vacancies, sort_vacancies_by_salary, get_top_vacancies


def user_interaction() -> None:
    """Функция взаимодействия с пользователем через консоль"""
    api = HeadHunterAPI()
    saver = JSONSaver()

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода: "))
    filter_word = input("Введите ключевое слово для фильтрации вакансий: ")

    raw_vacancies = api.get_vacancies(search_query, per_page=50)
    vacancies_list: List[Vacancy] = Vacancy.cast_to_object_list(raw_vacancies)

    # Сохраняем вакансии в файл
    for v in vacancies_list:
        saver.add_vacancy(v.to_dict())

    # Фильтрация и сортировка
    filtered = filter_vacancies(vacancies_list, filter_word)
    sorted_v = sort_vacancies_by_salary(filtered)
    top = get_top_vacancies(sorted_v, top_n)

    print("\nТоп вакансий:")
    for v in top:
        print(v)
