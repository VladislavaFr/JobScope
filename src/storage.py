from abc import ABC, abstractmethod
from typing import List, Dict
import json
import os


class FileAbstract(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_vacancy(self, vacancy: Dict) -> None:
        pass

    @abstractmethod
    def get_all_vacancies(self) -> List[Dict]:
        pass

    @abstractmethod
    def delete_vacancy(self, title: str) -> None:
        pass


class JSONSaver(FileAbstract):
    """Класс для работы с JSON-файлом вакансий"""

    def __init__(self, filename: str = "data/vacancies.json") -> None:
        """
        Инициализация с приватным именем файла

        Args:
            filename (str): путь к JSON-файлу
        """
        self.__filename: str = filename
        if not os.path.exists(os.path.dirname(self.__filename)):
            os.makedirs(os.path.dirname(self.__filename))

    def add_vacancy(self, vacancy: Dict) -> None:
        """Добавляет вакансию в JSON, без дубликатов"""
        data = self.get_all_vacancies()
        if all(v["title"] != vacancy["title"] for v in data):
            data.append(vacancy)
            with open(self.__filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

    def get_all_vacancies(self) -> List[Dict]:
        """Возвращает все вакансии из JSON"""
        if not os.path.exists(self.__filename):
            return []
        with open(self.__filename, "r", encoding="utf-8") as f:
            return json.load(f)

    def delete_vacancy(self, title: str) -> None:
        """Удаляет вакансию по названию"""
        data = self.get_all_vacancies()
        data = [v for v in data if v["title"] != title]
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
