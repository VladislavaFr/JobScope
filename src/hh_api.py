import requests
from abc import ABC, abstractmethod


class BaseJobsAPI(ABC):
    """Абстрактный класс для работы с API вакансий"""

    @abstractmethod
    def get_vacancies(self, text: str, per_page: int = 10):
        pass


class HeadHunterAPI(BaseJobsAPI):
    """Реализация API для HeadHunter"""

    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        self.session = self._connect()

    def _connect(self):
        """Создаёт сессию requests"""
        return requests.Session()

    def get_vacancies(self, text: str, per_page: int = 10):
        """Возвращает список вакансий по запросу"""
        params = {"text": text, "per_page": per_page}
        response = self.session.get(self.BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("items", [])
