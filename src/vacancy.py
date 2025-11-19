from typing import List, Dict


class Vacancy:
    """Класс для представления вакансии"""

    slots = ("title", "url", "salary", "description")

    def __init__(self, title: str, url: str, salary: int, description: str) -> None:
        """
        Инициализация вакансии

        Args:
            title (str): название вакансии
            url (str): ссылка на вакансию
            salary (int): зарплата
            description (str): описание вакансии
        """
        self.title: str = title
        self.url: str = url
        self.salary: int = self._validate_salary(salary)
        self.description: str = description

    def _validate_salary(self, salary: int) -> int:
        """
        Валидирует зарплату. Если None или <0, возвращает 0

        Args:
            salary (int): зарплата

        Returns:
            int: валидированная зарплата
        """
        if salary is None or salary < 0:
            return 0
        return salary

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнение по зарплате"""
        return self.salary < other.salary

    def __eq__(self, other: "Vacancy") -> bool:
        """Сравнение по зарплате и названию"""
        return self.salary == other.salary and self.title == other.title

    def __repr__(self) -> str:
        return f"Vacancy(title='{self.title}', salary={self.salary})"

    def __str__(self) -> str:
        return f"{self.title} — {self.salary} — {self.url}"

    def to_dict(self) -> Dict:
        """Преобразует объект вакансии в словарь"""
        return {
            "title": self.title,
            "url": self.url,
            "salary": self.salary,
            "description": self.description
        }

    @staticmethod
    def cast_to_object_list(data: List[Dict]) -> List["Vacancy"]:
        """Преобразует список словарей в список объектов Vacancy"""
        return [
            Vacancy(
                title=item.get("title") or item.get("name") or "Нет названия",
                url=item.get("url") or item.get("alternate_url") or "",
                salary=item.get("salary") or 0,
                description=item.get("description") or item.get("snippet", {}).get("requirement", "")
            )
            for item in data
        ]
