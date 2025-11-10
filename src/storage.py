import json
import os
from abc import ABC, abstractmethod


class BaseStorage(ABC):
    """Абстрактный класс для работы с хранилищем вакансий"""

    @abstractmethod
    def add_vacancy(self, vacancy: dict): ...
    @abstractmethod
    def get_all_vacancies(self): ...
    @abstractmethod
    def delete_vacancy(self, title: str): ...


class JSONSaver(BaseStorage):
    """Хранит вакансии в JSON файле"""

    def __init__(self, filename="data/vacancies.json"):
        self.filename = filename
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump([], f)

    def add_vacancy(self, vacancy: dict):
        data = self.get_all_vacancies()
        if vacancy not in data:
            data.append(vacancy)
            self._write(data)

    def get_all_vacancies(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            return json.load(f)

    def delete_vacancy(self, title: str):
        data = self.get_all_vacancies()
        new_data = [v for v in data if v.get("title") != title]
        self._write(new_data)

    def _write(self, data):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
