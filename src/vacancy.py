class Vacancy:
    """Класс для представления вакансии"""

    slots = ("title", "url", "salary", "description")

    def __init__(self, title: str, url: str, salary: int | None, description: str):
        self.title = self._validate_str(title, "title")
        self.url = self._validate_str(url, "url")
        self.salary = self._validate_salary(salary)
        self.description = self._validate_str(description, "description")

    def _validate_str(self, value, name):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name} must be a non-empty string")
        return value.strip()

    def _validate_salary(self, value):
        if value is None:
            return 0
        if not isinstance(value, (int, float)):
            raise ValueError("salary must be a number or None")
        return int(value)

    # ------------------- Магические методы -------------------

    def __str__(self):
        return f"{self.title} ({self.salary})"

    def __repr__(self):
        return f"Vacancy(title={self.title!r}, salary={self.salary!r})"

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    # ------------------- Методы -------------------

    def to_dict(self):
        return {
            "title": self.title,
            "url": self.url,
            "salary": self.salary,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data.get("title", ""),
            url=data.get("url", ""),
            salary=data.get("salary", 0),
            description=data.get("description", ""),
        )

    @classmethod
    def cast_to_object_list(cls, vacancies_data: list[dict]):
        return [cls.from_dict(v) for v in vacancies_data]
