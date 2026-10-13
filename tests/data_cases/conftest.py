import json
import os
from pathlib import Path

import pytest


def pytest_addoption(parser):
    parser.addoption("--qa-client-data", help="JSON с подтверждёнными QA-клиентами")


@pytest.fixture(scope="module")
def qa_client_data(request):
    filename = request.config.getoption("--qa-client-data", default=None) or os.getenv("PIV_QA_DATA_FILE")
    if not filename:
        pytest.skip("Нужен PIV_QA_DATA_FILE с подтверждёнными тестовыми клиентами")
    path = Path(filename)
    assert path.is_file(), "PIV_QA_DATA_FILE не найден"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(data, dict), "Тестовые данные должны быть JSON-объектом"
    return data


@pytest.fixture
def primary_client(qa_client_data):
    client = qa_client_data.get("primary_client")
    if client is None:
        pytest.skip("Не задана подтверждённая пара телефона и ID клиента")
    assert isinstance(client, dict), "primary_client должен быть объектом"
    assert type(client.get("id")) is int and client["id"] > 0, "Нужен положительный ID primary_client"
    assert isinstance(client.get("phone"), str) and client["phone"], "Нужен телефон primary_client"
    assert str(client.get("clinic_code")) == os.getenv("CLINIC_CODE"), "Клиент должен принадлежать основной клинике"
    return client


@pytest.fixture
def empty_client(qa_client_data):
    client = qa_client_data.get("empty_client")
    if client is None:
        pytest.skip("Не задан существующий клиент без данных")
    assert isinstance(client, dict), "empty_client должен быть объектом"
    assert type(client.get("id")) is int and client["id"] > 0, "Нужен положительный ID empty_client"
    assert isinstance(client.get("phone"), str) and client["phone"], "Нужен телефон empty_client"
    assert client.get("confirmed_empty") is True, "Пустые данные должны быть подтверждены в ВМ"
    assert str(client.get("clinic_code")) == os.getenv("CLINIC_CODE"), "Пустой клиент должен принадлежать основной клинике"
    return client


@pytest.fixture
def populated_client(qa_client_data):
    client = qa_client_data.get("populated_client")
    if client is None:
        pytest.skip("Не задан подтверждённый клиент с данными")
    assert isinstance(client, dict), "populated_client должен быть объектом"
    assert type(client.get("id")) is int and client["id"] > 0, "Нужен положительный ID populated_client"
    assert str(client.get("clinic_code")) == os.getenv("CLINIC_CODE"), "Нужен общий код доступа текущего домена"
    return client


@pytest.fixture
def shared_domain_client(qa_client_data):
    client = qa_client_data.get("shared_domain_client")
    if client is None:
        pytest.skip("Не задан клиент другой клиники того же домена с общим кодом доступа")
    assert isinstance(client, dict), "shared_domain_client должен быть объектом"
    assert type(client.get("id")) is int and client["id"] > 0, "Нужен положительный ID shared_domain_client"
    assert isinstance(client.get("phone"), str) and client["phone"], "Нужен телефон shared_domain_client"
    assert str(client.get("clinic_code")) == os.getenv("CLINIC_CODE"), "Код доступа должен быть общим для домена"
    assert client.get("confirmed_other_clinic_same_domain") is True, "Нужно подтвердить другую клинику того же домена"
    return client
