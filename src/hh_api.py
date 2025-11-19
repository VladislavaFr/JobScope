from abc import ABC, abstractmethod
import requests
from typing import List, Dict


class APIAbstract(ABC):
    """Абстрактный класс для работы с API сервисов вакансий"""

    @abstractmethod
    def _connect(self) -> requests.Response:
        """Метод подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, text: str, per_page: int = 20) -> List[Dict]:
        """Получение вакансий по ключевому слову"""
        pass


class HeadHunterAPI(APIAbstract):
    """Класс для работы с API HeadHunter.ru"""

    def __init__(self) -> None:
        """Инициализация базового URL для HH API"""
        self.__base_url: str = "https://api.hh.ru/vacancies"

    def _connect(self) -> requests.Response:
        """Подключение к базовому URL HH API"""
        response: requests.Response = requests.get(self.__base_url)
        response.raise_for_status()
        return response

    def get_vacancies(self, text: str, per_page: int = 20) -> List[Dict]:
        """
        Получение вакансий по ключевому слову text.

        Args:
            text (str): ключевое слово для поиска вакансий
            per_page (int): количество вакансий на страницу

        Returns:
            List[Dict]: список вакансий в формате словарей
        """
        params: Dict = {"text": text, "per_page": per_page}
        response: requests.Response = requests.get(self.__base_url, params=params)
        response.raise_for_status()
        return response.json().get("items", [])
