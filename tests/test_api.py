import pytest
from src.hh_api import HeadHunterAPI


def test_get_vacancies(monkeypatch):
    def fake_get(url, params):
        class FakeResponse:
            def raise_for_status(self): pass

            def json(self):
                return {"items": [
                    {"name": "Dev", "alternate_url": "url", "salary": None, "snippet": {"requirement": "desc"}}]}

        return FakeResponse()

    api = HeadHunterAPI()
    monkeypatch.setattr(api.session, "get", fake_get)

    data = api.get_vacancies("python")
    assert isinstance(data, list)
    assert data[0]["name"] == "Dev"
