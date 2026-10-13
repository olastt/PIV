import allure
import pytest

from base.piv_client import PivApiClient
from src.config.url import Url
from tests.helpers.client_records import collection_records, assert_reference_records
from tests.helpers.piv_positive import assert_piv_success


COLLECTIONS = [
    (Url.GET_ADMISSIONS_BY_CLIENT_ID, "admission", ("admission_id",)),
    (Url.GET_RECOMENDATIONS_BY_CLIENT_ID, "recomendation", ("id",)),
    (Url.GET_VACCINATIONS_BY_CLIENT_ID, "vaccination", ("medcard_id", "vaccine_id", "vaccination_date")),
    (Url.GET_DISCOUNT_CARDS, "card", ("id",)),
]


def get_collection(client, client_id, endpoint, items_field):
    response = client.get(endpoint, params={"client_id": client_id})
    response.assert_status_code(200)
    body = assert_piv_success(response)
    return body, collection_records(body, items_field)


@pytest.mark.positive
@allure.epic("PIV")
@allure.feature("Клиент с данными")
def test_populated_client_has_data(populated_client):
    client = PivApiClient()
    counts = [len(get_collection(client, populated_client["id"], endpoint, field)[1])
              for endpoint, field, _ in COLLECTIONS]
    assert any(counts), "У подтверждённого клиента с данными все проверенные коллекции пустые"


@pytest.mark.positive
@allure.epic("PIV")
@allure.feature("Смена клиента в запросах")
@pytest.mark.parametrize("endpoint,items_field", [(endpoint, field) for endpoint, field, _ in COLLECTIONS])
def test_switch_populated_empty_populated_client(populated_client, empty_client, endpoint, items_field):
    assert populated_client["id"] != empty_client["id"], "Для проверки нужны два разных клиента"
    client = PivApiClient()
    _, initial = get_collection(client, populated_client["id"], endpoint, items_field)
    if not initial:
        assert items_field not in populated_client.get("nonempty_collections", []), "Подтверждённые записи клиента отсутствуют в ответе"
        pytest.skip("У клиента с данными этот endpoint пустой: смена непустого ответа на пустой непроверяема")
    body, empty = get_collection(client, empty_client["id"], endpoint, items_field)
    assert empty == [], "После смены client_id пустому клиенту вернулись записи"
    data = body["data"]
    groups = data if isinstance(data, list) else [data]
    for group in groups:
        assert group["totalCount"] == 0, "Пустому клиенту вернулся ненулевой totalCount"
    _, restored = get_collection(client, populated_client["id"], endpoint, items_field)
    assert restored, "После возврата к клиенту с данными вернулась пустая коллекция"
    # Не требуем равенства live снимков: содержимое на production может меняться.


@pytest.mark.positive
@allure.epic("PIV")
@allure.feature("Сверка записей с ВМ")
@pytest.mark.parametrize("endpoint,items_field,identity_fields", COLLECTIONS)
def test_client_records_match_vm_reference(populated_client, endpoint, items_field, identity_fields):
    references = populated_client.get("expected", {})
    assert isinstance(references, dict), "expected должен быть объектом"
    reference = references.get(items_field)
    if reference is None:
        pytest.skip("Нужны ID и значения записей, независимо подтверждённые в ВМ")
    assert isinstance(reference, dict), "Эталон коллекции должен быть объектом"
    assert reference.get("confirmed_in_vm") is True, "Эталон должен быть подтверждён в ВМ"
    records = reference.get("records")
    assert isinstance(records, list) and records, "Нужен непустой список эталонных записей"
    assert type(reference.get("complete", False)) is bool, "complete должен быть boolean"
    for record in records:
        assert isinstance(record, dict) and set(record) - set(identity_fields), "Кроме ID нужно хотя бы одно ожидаемое значение поля"
    _, actual = get_collection(PivApiClient(), populated_client["id"], endpoint, items_field)
    assert_reference_records(actual, records, identity_fields, complete=reference.get("complete", False))
