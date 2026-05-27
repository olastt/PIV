import os
import re

import allure
import pytest

from base.main_request_class import ApiClient


SWAGGER_ENDPOINTS = [
    ("GET", "/api/v2/properties"),
    ("GET", "/api/v2/users/{user_id}/settings/payment"),
    ("GET", "/api/v2/checkversion"),
    ("PATCH", "/api/v2/users/settings/payment/{recordId}"),
    ("POST", "/api/v2/users/settings/payment/0"),
    ("GET", "/api/v2/redis/clear"),
    ("GET", "/api/v2/users/{user_id}"),
    ("PATCH", "/api/v2/users/{user_id}"),
    ("GET", "/api/v2/users/{user_id}/home"),
    ("GET", "/api/v2/users/{user_id}/stores"),
    ("GET", "/api/v2/users/{user_id}/schedules"),
    ("GET", "/api/v2/users/{user_id}/allowedclinics"),
    ("POST", "/api/v2/users/{user_id}/logout"),
    ("GET", "/api/v2/users/doctors"),
    ("GET", "/api/v2/hospital"),
    ("GET", "/api/v2/hospital/{recordId}"),
    ("PATCH", "/api/v2/hospital/{recordId}"),
    ("GET", "/api/v2/hospital/blocks"),
    ("GET", "/api/v2/hospital/liststatuses"),
    ("GET", "/api/v2/cassa/{user_id}"),
    ("GET", "/api/v2/tariff"),
    ("GET", "/api/v2/billingurl"),
    ("GET", "/api/v2/roles/{id_role}"),
    ("GET", "/api/v2/users/{user_id}/calls"),
    ("POST", "/api/v2/users/{user_id}/calls"),
    ("GET", "/api/v2/users/{user_id}/calls/{call_id}"),
    ("PATCH", "/api/v2/users/{user_id}/calls/{call_id}"),
    ("GET", "/api/v2/calls/search"),
    ("PATCH", "/api/v2/clients/{client_id}"),
    ("GET", "/api/v2/clients/{client_id}"),
    ("POST", "/api/v2/clients/combine"),
    ("GET", "/api/v2/clients/{client_id}/match/"),
    ("GET", "/api/v2/clients/search/"),
    ("GET", "/api/v2/clients/{client_id}/contacts"),
    ("GET", "/api/v2/clients/{client_id}/pets/{pet_id}"),
    ("PATCH", "/api/v2/clients/{client_id}/pets/{pet_id}"),
    ("GET", "/api/v2/clients/{client_id}/pets"),
    ("POST", "/api/v2/clients"),
    ("GET", "/api/v2/pets/types"),
    ("GET", "/api/v2/pets/genders"),
    ("GET", "/api/v2/pets/types/{type_id}/breeds"),
    ("GET", "/api/v2/pets/breeds"),
    ("POST", "/api/v1/clients/{client_id}/pets"),
    ("GET", "/api/v2/products"),
    ("POST", "/api/v2/products"),
    ("DELETE", "/api/v2/products"),
    ("PATCH", "/api/v2/products/{product_id}"),
    ("GET", "/api/v2/products/{product_id}"),
    ("GET", "/api/v2/products/{product_id}/stockbalances"),
    ("GET", "/api/v2/products/categories"),
    ("GET", "/api/v2/products/{product_id}/pricing/{qty}"),
    ("GET", "/api/v2/categoriesproducts"),
    ("DELETE", "/api/v2/categoriesproducts"),
    ("POST", "/api/v2/categoriesproducts"),
    ("GET", "/api/v2/products/categoriesproducts"),
    ("PATCH", "/api/v2/categoriesproducts/{category_id}"),
    ("POST", "/api/v2/notification/device"),
    ("GET", "/api/v2/notification/settings"),
    ("PATCH", "/api/v2/notification/settings"),
    ("POST", "/api/v2/vetmanager-hook"),
    ("DELETE", "/api/v2/remove-notification/{notification_id}"),
    ("GET", "/api/v2/clinics"),
    ("GET", "/api/v2/users/admission/{admission_id}"),
    ("GET", "/api/v2/users/{user_id}/admission"),
    ("POST", "/api/v2/users/16/admission"),
    ("PATCH", "/api/v2/users/{user_id}/admission/{admission_id}"),
    ("POST", "/api/v2/users/admission/180/confirm"),
    ("GET", "/api/v2/clients/{client_id}/invoices"),
    ("POST", "/api/v2/clients/{client_id}/invoices"),
    ("POST", "/api/v2/clients/{client_id}/payments"),
    ("GET", "/api/v2/clients/{client_id}/invoices/{invoice_id}/products"),
    ("GET", "/api/v2/medicalcards/vaccinations/{pet_id}"),
    ("POST", "/api/v2/medicalcards/{medicalcard_id}/vaccinations/{pet_id}"),
    ("PATCH", "/api/v2/medicalcards/{medicalcard_id}/vaccinations/{vaccination_id}"),
    ("PATCH", "/api/v1/medicalcards/vaccinations/{vaccination_id}"),
    ("GET", "/api/v2/products/vaccines"),
    ("GET", "/api/v2/clients/{client_id}/medicalcards"),
    ("POST", "/api/v2/clients/{client_id}/medicalcards"),
    ("GET", "/api/v2/clients/{client_id}/medicalcards/{medicalcard_id}"),
    ("GET", "/api/v2/clients/medicalcards/diagnoses"),
    ("GET", "/api/v2/medicalcards/texttemplates"),
    ("GET", "/api/v2/clients/{client_id}/medicalcards/history"),
    ("POST", "/api/v2/medicalcards/uploadfiles"),
    ("POST", "/api/v2/medicalcards/generate-llm"),
    ("PATCH", "/api/v2/clients/{client_id}/medicalcards/88"),
    ("GET", "/api/v2/combomanuals/{combomanuals_id}"),
    ("GET", "/api/v2/combomanuals/vaccinationstypes"),
    ("POST", "/api/v2/combomanuals/streets"),
    ("POST", "/api/v2/combomanuals/cities"),
    ("GET", "/api/v2/combomanuals/cities"),
    ("GET", "/api/v2/combomanuals/typesstreets"),
    ("GET", "/api/v2/combomanuals/{city_id}/streets"),
    ("GET", "/api/v2/combomanuals/typescities"),
    ("GET", "/api/v2/combomanuals/reasonsofvisit"),
    ("GET", "/api/v1/combomanuals/resultofvisit"),
    ("GET", "/api/v2/diagnoses"),
    ("POST", "/api/v2/diagnoses"),
    ("PATCH", "/api/v2/diagnoses/{diagnos_id}"),
    ("DELETE", "/api/v2/diagnoses/{diagnos_id}"),
    ("GET", "/api/v2/diagnoses/{diagnos_id}"),
]

PATH_PARAM_DEFAULTS = {
    "admission_id": "1",
    "call_id": "1",
    "category_id": "1",
    "city_id": "252",
    "client_id": os.getenv("CLIENT_ID", "1"),
    "combomanuals_id": "1",
    "diagnos_id": "1",
    "id_role": "1",
    "invoice_id": "1",
    "medicalcard_id": os.getenv("MEDICALCARD_ID", "1"),
    "notification_id": "1",
    "pet_id": os.getenv("PET_ID", "1"),
    "product_id": "1",
    "qty": "1",
    "recordId": "1",
    "type_id": "1",
    "user_id": os.getenv("USER_ID", "1"),
    "vaccination_id": "1",
}

MUTATING_METHODS = {"POST", "PATCH", "PUT", "DELETE"}
NEGATIVE_STATUS_CODES = [400, 401, 403, 404, 405, 409, 422, 520]
INVALID_AUTH_STATUS_CODES = [200, 401, 403, 404, 422, 520]
INVALID_PATH_CAN_RETURN_OK = {
    ("GET", "/api/v2/clients/{client_id}/invoices"),
}

DELETE_NOT_FOUND_CASES = [
    (
        "DELETE",
        "/api/v2/remove-notification/{notification_id}",
        {"notification_id": "5000000"},
        520,
        "удаление несуществующего уведомления по числовому id",
    ),
    (
        "DELETE",
        "/api/v2/diagnoses/{diagnos_id}",
        {"diagnos_id": "5000000"},
        520,
        "удаление несуществующего диагноза по числовому id",
    ),
]

DELETE_INVALID_TYPE_CASES = [
]

EMPTY_BODY_TITLES = {
    ("PATCH", "/api/v2/users/settings/payment/{recordId}"): "обновление настроек оплаты без обязательных данных",
    ("POST", "/api/v2/users/settings/payment/0"): "создание настроек оплаты без обязательных данных",
    ("PATCH", "/api/v2/users/{user_id}"): "обновление пользователя без данных пользователя",
    ("POST", "/api/v2/users/{user_id}/logout"): "logout пользователя без тела запроса",
    ("PATCH", "/api/v2/hospital/{recordId}"): "обновление стационара без данных записи",
    ("POST", "/api/v2/users/{user_id}/calls"): "создание прозвона без данных прозвона",
    ("PATCH", "/api/v2/users/{user_id}/calls/{call_id}"): "обновление прозвона без данных прозвона",
    ("PATCH", "/api/v2/clients/{client_id}"): "обновление клиента без данных клиента",
    ("POST", "/api/v2/clients/combine"): "объединение клиентов без combine_data",
    ("PATCH", "/api/v2/clients/{client_id}/pets/{pet_id}"): "обновление питомца без данных питомца",
    ("POST", "/api/v2/clients"): "создание клиента без обязательных данных клиента",
    ("POST", "/api/v1/clients/{client_id}/pets"): "создание питомца без обязательных данных питомца",
    ("POST", "/api/v2/products"): "создание продукта без обязательных данных продукта",
    ("DELETE", "/api/v2/products"): "удаление продукта без обязательного product_ids",
    ("PATCH", "/api/v2/products/{product_id}"): "обновление продукта без данных продукта",
    ("DELETE", "/api/v2/categoriesproducts"): "удаление категории продукта без обязательного category_ids",
    ("POST", "/api/v2/categoriesproducts"): "создание категории продукта без данных категории",
    ("PATCH", "/api/v2/categoriesproducts/{category_id}"): "обновление категории продукта без данных категории",
    ("POST", "/api/v2/notification/device"): "регистрация устройства без данных устройства",
    ("PATCH", "/api/v2/notification/settings"): "обновление настроек уведомлений без данных настроек",
    ("POST", "/api/v2/vetmanager-hook"): "вызов vetmanager-hook без списка уведомлений",
    ("DELETE", "/api/v2/remove-notification/{notification_id}"): "удаление уведомления без обязательных параметров",
    ("POST", "/api/v2/users/16/admission"): "создание приема без данных приема",
    ("PATCH", "/api/v2/users/{user_id}/admission/{admission_id}"): "обновление приема без данных приема",
    ("POST", "/api/v2/users/admission/180/confirm"): "подтверждение приема без данных подтверждения",
    ("POST", "/api/v2/clients/{client_id}/invoices"): "создание счета без данных счета",
    ("POST", "/api/v2/clients/{client_id}/payments"): "оплата счета без данных платежа",
    ("POST", "/api/v2/medicalcards/{medicalcard_id}/vaccinations/{pet_id}"): "создание вакцинации без данных вакцинации",
    ("PATCH", "/api/v2/medicalcards/{medicalcard_id}/vaccinations/{vaccination_id}"): "обновление вакцинации без данных вакцинации",
    ("PATCH", "/api/v1/medicalcards/vaccinations/{vaccination_id}"): "короткое обновление вакцинации без данных вакцинации",
    ("POST", "/api/v2/clients/{client_id}/medicalcards"): "создание медкарты без данных медкарты",
    ("POST", "/api/v2/medicalcards/uploadfiles"): "загрузка файлов медкарты без данных файла",
    ("POST", "/api/v2/medicalcards/generate-llm"): "генерация текста медкарты без prompt",
    ("PATCH", "/api/v2/clients/{client_id}/medicalcards/88"): "обновление медкарты без данных медкарты",
    ("POST", "/api/v2/combomanuals/streets"): "создание улицы без данных улицы",
    ("POST", "/api/v2/combomanuals/cities"): "создание города без данных города",
    ("POST", "/api/v2/diagnoses"): "создание диагноза без данных диагноза",
    ("PATCH", "/api/v2/diagnoses/{diagnos_id}"): "обновление диагноза без данных диагноза",
    ("DELETE", "/api/v2/diagnoses/{diagnos_id}"): "удаление диагноза без обязательных данных",
}


def _invalid_auth_title(method: str, path: str) -> str:
    return f"Неверная авторизация: {method} {path}"


def _invalid_path_title(method: str, path: str) -> str:
    return f"Невалидный path-параметр: {method} {path}"


def _empty_body_title(method: str, path: str) -> str:
    action = EMPTY_BODY_TITLES.get((method, path), "запрос без обязательного тела")
    return f"{action}: {method} {path}"


def _resolve_path(path: str, invalid_params: bool = False, overrides: dict = None) -> str:
    overrides = overrides or {}

    def replace(match):
        name = match.group(1)
        if name in overrides:
            return str(overrides[name])
        if invalid_params:
            return "not-an-id"
        return PATH_PARAM_DEFAULTS.get(name, "1")

    return re.sub(r"{([^{}]+)}", replace, path)


def _send(client: ApiClient, method: str, endpoint: str, headers=None, json_data=None, invalid_query=True):
    kwargs = {"headers": headers, "timeout": 30}
    if method == "GET":
        params = {"page[number]": "invalid", "page[size]": "-1"} if invalid_query else None
        return client.get(endpoint, params=params, **kwargs)
    if method == "POST":
        return client.post(endpoint, json_data=json_data if json_data is not None else {}, **kwargs)
    if method == "PATCH":
        return client.patch(endpoint, json_data=json_data if json_data is not None else {}, **kwargs)
    if method == "PUT":
        return client.put(endpoint, json_data=json_data if json_data is not None else {}, **kwargs)
    if method == "DELETE":
        if json_data is None:
            return client.delete(endpoint, **kwargs)
        return client.delete(endpoint, json_data=json_data, **kwargs)
    raise AssertionError(f"Unsupported method in Swagger test: {method}")


@pytest.mark.negative
@allure.epic("Swagger negative coverage")
@pytest.mark.parametrize(
    ("method", "path"),
    SWAGGER_ENDPOINTS,
    ids=[_invalid_auth_title(method, path) for method, path in SWAGGER_ENDPOINTS],
)
def test_swagger_endpoints_reject_invalid_authorization(method, path):
    allure.dynamic.title(_invalid_auth_title(method, path))
    client = ApiClient(api_key="pytest-invalid-token")
    headers = {"X-TOKEN": "pytest-invalid-token"}

    response = _send(client, method, _resolve_path(path), headers=headers, invalid_query=False)

    response.assert_status_code(INVALID_AUTH_STATUS_CODES)


@pytest.mark.negative
@allure.epic("Swagger negative coverage")
@pytest.mark.parametrize(
    ("method", "path"),
    [(method, path) for method, path in SWAGGER_ENDPOINTS if "{" in path],
    ids=[_invalid_path_title(method, path) for method, path in SWAGGER_ENDPOINTS if "{" in path],
)
def test_swagger_endpoints_reject_invalid_path_parameters(method, path):
    allure.dynamic.title(_invalid_path_title(method, path))
    client = ApiClient()

    response = _send(client, method, _resolve_path(path, invalid_params=True))

    expected_status_codes = NEGATIVE_STATUS_CODES.copy()
    if (method, path) in INVALID_PATH_CAN_RETURN_OK:
        expected_status_codes.append(200)
    response.assert_status_code(expected_status_codes)


@pytest.mark.negative
@allure.epic("Swagger negative coverage")
@pytest.mark.parametrize(
    ("method", "path"),
    [(method, path) for method, path in SWAGGER_ENDPOINTS if method in MUTATING_METHODS],
    ids=[_empty_body_title(method, path) for method, path in SWAGGER_ENDPOINTS if method in MUTATING_METHODS],
)
def test_swagger_mutating_endpoints_reject_empty_body(method, path):
    allure.dynamic.title(_empty_body_title(method, path))
    client = ApiClient()

    response = _send(client, method, _resolve_path(path), json_data={})

    response.assert_status_code(NEGATIVE_STATUS_CODES)


@pytest.mark.negative
@allure.epic("Swagger negative coverage")
@pytest.mark.parametrize(
    ("method", "path", "path_overrides", "expected_status", "case_title"),
    DELETE_NOT_FOUND_CASES,
    ids=[case_title for _, _, _, _, case_title in DELETE_NOT_FOUND_CASES],
)
def test_swagger_delete_endpoints_return_not_found_for_missing_numeric_id(
    method,
    path,
    path_overrides,
    expected_status,
    case_title,
):
    allure.dynamic.title(f"{case_title}: {method} {path}")
    client = ApiClient()

    response = _send(client, method, _resolve_path(path, overrides=path_overrides))

    response.assert_status_code(expected_status)
