import allure
import pytest

from base.piv_client import PivApiClient
from src.config.url import Url
from tests.helpers.piv_positive import assert_piv_success


COLLECTIONS = [
    (Url.GET_ADMISSIONS_BY_CLIENT_ID, "admission"),
    (Url.GET_RECOMENDATIONS_BY_CLIENT_ID, "recomendation"),
    (Url.GET_VACCINATIONS_BY_CLIENT_ID, "vaccination"),
    (Url.GET_DISCOUNT_CARDS, "card"),
]


@pytest.mark.positive
@allure.epic("PIV")
@allure.feature("Соответствие клиента телефону")
def test_phone_resolves_expected_client(primary_client):
    response = PivApiClient().get(Url.GET_CLIENT_BY_PHONE, params={"phone": primary_client["phone"]})
    response.assert_status_code(200)
    body = assert_piv_success(response)
    assert body["data"]["client_id"] == primary_client["id"], "Телефон разрешился в другого клиента"


@pytest.mark.positive
@allure.epic("PIV")
@allure.feature("Клиент без данных")
@pytest.mark.parametrize("endpoint,items_field", COLLECTIONS)
def test_existing_client_has_empty_collection(empty_client, endpoint, items_field):
    client = PivApiClient()
    # Positive control: отсутствие данных не должно маскировать неизвестного клиента.
    lookup = client.get(Url.GET_CLIENT_BY_PHONE, params={"phone": empty_client["phone"]})
    lookup.assert_status_code(200)
    assert assert_piv_success(lookup)["data"]["client_id"] == empty_client["id"], "Fixture не соответствует найденному клиенту"
    response = client.get(endpoint, params={"client_id": empty_client["id"]})
    response.assert_status_code(200)
    data = assert_piv_success(response)["data"]
    groups = data if isinstance(data, list) else [data]
    for group in groups:
        assert group["totalCount"] == 0, "Для клиента без данных ожидался totalCount=0"
        assert group[items_field] == [], "Для клиента без данных ожидалась пустая коллекция"


@pytest.mark.positive
@allure.epic("PIV")
@allure.feature("Общий доступ к клиникам домена")
def test_other_clinic_client_is_visible_with_shared_domain_key(shared_domain_client):
    response = PivApiClient().get(Url.GET_CLIENT_BY_PHONE, params={"phone": shared_domain_client["phone"]})
    response.assert_status_code(200)
    body = assert_piv_success(response)
    assert body["data"]["client_id"] == shared_domain_client["id"], "Общий ключ домена должен находить клиента другой клиники этого домена"
