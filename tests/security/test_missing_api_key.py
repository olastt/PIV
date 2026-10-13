import os

import allure
import pytest

from base.piv_client import PivApiClient
from src.config.url import Url
from tests.helpers.access import assert_access_denied


@pytest.mark.negative
@allure.epic("PIV")
@allure.feature("Авторизация без X-API-KEY")
@pytest.mark.parametrize("endpoint,parameter", [
    (Url.GET_API_KEY_BY_CLINIC_CODE, "code"),
    (Url.GET_CLIENT_BY_PHONE, "phone"),
    (Url.GET_PHONE_PREFIX, None),
    (Url.GET_DOMAIN_NAME, None),
    (Url.GET_ADMISSIONS_BY_CLIENT_ID, "client_id"),
    (Url.GET_RECOMENDATIONS_BY_CLIENT_ID, "client_id"),
    (Url.GET_VACCINATIONS_BY_CLIENT_ID, "client_id"),
    (Url.GET_CLINICS, None),
    (Url.GET_LAST_THREE_ARTICLES, None),
    (Url.GET_ARTICLES, "pagination"),
    (Url.GET_DISCOUNT_CARDS, "client_id"),
])
def test_missing_api_key_denies_access(endpoint, parameter):
    values = {"code": os.getenv("CLINIC_CODE"), "phone": os.getenv("CLIENT_PHONE"), "client_id": os.getenv("CLIENT_ID")}
    if parameter == "pagination":
        params = {"page": 1, "size": 1}
    elif parameter:
        assert values[parameter], f"Для изолированной проверки авторизации нужен {parameter}"
        params = {parameter: values[parameter]}
    else:
        params = None
    # None подставляет ключ из окружения; пустая строка явно отключает его.
    response = PivApiClient(api_key="").get(endpoint, params=params)
    assert "X-API-KEY" not in response.response.request.headers, "Запрос неожиданно содержит API key"
    assert_access_denied(response)
