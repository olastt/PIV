import os
import re

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
INVALID_PATH_EXCLUDED_CASES = {
    ("DELETE", "/api/v2/remove-notification/{notification_id}"),
    ("DELETE", "/api/v2/diagnoses/{diagnos_id}"),
}

DELETE_NOT_FOUND_CASES = [
    (
        "DELETE",
        "/api/v2/remove-notification/{notification_id}",
        {"notification_id": "5000000"},
        520,
        "СѓРґР°Р»РµРЅРёРµ РЅРµСЃСѓС‰РµСЃС‚РІСѓСЋС‰РµРіРѕ СѓРІРµРґРѕРјР»РµРЅРёСЏ РїРѕ С‡РёСЃР»РѕРІРѕРјСѓ id",
    ),
    (
        "DELETE",
        "/api/v2/diagnoses/{diagnos_id}",
        {"diagnos_id": "5000000"},
        520,
        "СѓРґР°Р»РµРЅРёРµ РЅРµСЃСѓС‰РµСЃС‚РІСѓСЋС‰РµРіРѕ РґРёР°РіРЅРѕР·Р° РїРѕ С‡РёСЃР»РѕРІРѕРјСѓ id",
    ),
]

EMPTY_BODY_TITLES = {
    ("PATCH", "/api/v2/users/settings/payment/{recordId}"): "РѕР±РЅРѕРІР»РµРЅРёРµ РЅР°СЃС‚СЂРѕРµРє РѕРїР»Р°С‚С‹ Р±РµР· РѕР±СЏР·Р°С‚РµР»СЊРЅС‹С… РґР°РЅРЅС‹С…",
    ("POST", "/api/v2/users/settings/payment/0"): "СЃРѕР·РґР°РЅРёРµ РЅР°СЃС‚СЂРѕРµРє РѕРїР»Р°С‚С‹ Р±РµР· РѕР±СЏР·Р°С‚РµР»СЊРЅС‹С… РґР°РЅРЅС‹С…",
    ("PATCH", "/api/v2/users/{user_id}"): "РѕР±РЅРѕРІР»РµРЅРёРµ РїРѕР»СЊР·РѕРІР°С‚РµР»СЏ Р±РµР· РґР°РЅРЅС‹С… РїРѕР»СЊР·РѕРІР°С‚РµР»СЏ",
    ("POST", "/api/v2/users/{user_id}/logout"): "logout РїРѕР»СЊР·РѕРІР°С‚РµР»СЏ Р±РµР· С‚РµР»Р° Р·Р°РїСЂРѕСЃР°",
    ("PATCH", "/api/v2/hospital/{recordId}"): "РѕР±РЅРѕРІР»РµРЅРёРµ СЃС‚Р°С†РёРѕРЅР°СЂР° Р±РµР· РґР°РЅРЅС‹С… Р·Р°РїРёСЃРё",
    ("POST", "/api/v2/users/{user_id}/calls"): "СЃРѕР·РґР°РЅРёРµ РїСЂРѕР·РІРѕРЅР° Р±РµР· РґР°РЅРЅС‹С… РїСЂРѕР·РІРѕРЅР°",
    ("PATCH", "/api/v2/users/{user_id}/calls/{call_id}"): "РѕР±РЅРѕРІР»РµРЅРёРµ РїСЂРѕР·РІРѕРЅР° Р±РµР· РґР°РЅРЅС‹С… РїСЂРѕР·РІРѕРЅР°",
    ("PATCH", "/api/v2/clients/{client_id}"): "РѕР±РЅРѕРІР»РµРЅРёРµ РєР»РёРµРЅС‚Р° Р±РµР· РґР°РЅРЅС‹С… РєР»РёРµРЅС‚Р°",
    ("POST", "/api/v2/clients/combine"): "РѕР±СЉРµРґРёРЅРµРЅРёРµ РєР»РёРµРЅС‚РѕРІ Р±РµР· combine_data",
    ("PATCH", "/api/v2/clients/{client_id}/pets/{pet_id}"): "РѕР±РЅРѕРІР»РµРЅРёРµ РїРёС‚РѕРјС†Р° Р±РµР· РґР°РЅРЅС‹С… РїРёС‚РѕРјС†Р°",
    ("POST", "/api/v2/clients"): "СЃРѕР·РґР°РЅРёРµ РєР»РёРµРЅС‚Р° Р±РµР· РѕР±СЏР·Р°С‚РµР»СЊРЅС‹С… РґР°РЅРЅС‹С… РєР»РёРµРЅС‚Р°",
    ("POST", "/api/v1/clients/{client_id}/pets"): "СЃРѕР·РґР°РЅРёРµ РїРёС‚РѕРјС†Р° Р±РµР· РѕР±СЏР·Р°С‚РµР»СЊРЅС‹С… РґР°РЅРЅС‹С… РїРёС‚РѕРјС†Р°",
    ("POST", "/api/v2/products"): "СЃРѕР·РґР°РЅРёРµ РїСЂРѕРґСѓРєС‚Р° Р±РµР· РѕР±СЏР·Р°С‚РµР»СЊРЅС‹С… РґР°РЅРЅС‹С… РїСЂРѕРґСѓРєС‚Р°",
    ("DELETE", "/api/v2/products"): "СѓРґР°Р»РµРЅРёРµ РїСЂРѕРґСѓРєС‚Р° Р±РµР· РѕР±СЏР·Р°С‚РµР»СЊРЅРѕРіРѕ product_ids",
    ("PATCH", "/api/v2/products/{product_id}"): "РѕР±РЅРѕРІР»РµРЅРёРµ РїСЂРѕРґСѓРєС‚Р° Р±РµР· РґР°РЅРЅС‹С… РїСЂРѕРґСѓРєС‚Р°",
    ("DELETE", "/api/v2/categoriesproducts"): "СѓРґР°Р»РµРЅРёРµ РєР°С‚РµРіРѕСЂРёРё РїСЂРѕРґСѓРєС‚Р° Р±РµР· РѕР±СЏР·Р°С‚РµР»СЊРЅРѕРіРѕ category_ids",
    ("POST", "/api/v2/categoriesproducts"): "СЃРѕР·РґР°РЅРёРµ РєР°С‚РµРіРѕСЂРёРё РїСЂРѕРґСѓРєС‚Р° Р±РµР· РґР°РЅРЅС‹С… РєР°С‚РµРіРѕСЂРёРё",
    ("PATCH", "/api/v2/categoriesproducts/{category_id}"): "РѕР±РЅРѕРІР»РµРЅРёРµ РєР°С‚РµРіРѕСЂРёРё РїСЂРѕРґСѓРєС‚Р° Р±РµР· РґР°РЅРЅС‹С… РєР°С‚РµРіРѕСЂРёРё",
    ("POST", "/api/v2/notification/device"): "СЂРµРіРёСЃС‚СЂР°С†РёСЏ СѓСЃС‚СЂРѕР№СЃС‚РІР° Р±РµР· РґР°РЅРЅС‹С… СѓСЃС‚СЂРѕР№СЃС‚РІР°",
    ("PATCH", "/api/v2/notification/settings"): "РѕР±РЅРѕРІР»РµРЅРёРµ РЅР°СЃС‚СЂРѕРµРє СѓРІРµРґРѕРјР»РµРЅРёР№ Р±РµР· РґР°РЅРЅС‹С… РЅР°СЃС‚СЂРѕРµРє",
    ("POST", "/api/v2/vetmanager-hook"): "РІС‹Р·РѕРІ vetmanager-hook Р±РµР· СЃРїРёСЃРєР° СѓРІРµРґРѕРјР»РµРЅРёР№",
    ("DELETE", "/api/v2/remove-notification/{notification_id}"): "СѓРґР°Р»РµРЅРёРµ СѓРІРµРґРѕРјР»РµРЅРёСЏ Р±РµР· РѕР±СЏР·Р°С‚РµР»СЊРЅС‹С… РїР°СЂР°РјРµС‚СЂРѕРІ",
    ("POST", "/api/v2/users/16/admission"): "СЃРѕР·РґР°РЅРёРµ РїСЂРёРµРјР° Р±РµР· РґР°РЅРЅС‹С… РїСЂРёРµРјР°",
    ("PATCH", "/api/v2/users/{user_id}/admission/{admission_id}"): "РѕР±РЅРѕРІР»РµРЅРёРµ РїСЂРёРµРјР° Р±РµР· РґР°РЅРЅС‹С… РїСЂРёРµРјР°",
    ("POST", "/api/v2/users/admission/180/confirm"): "РїРѕРґС‚РІРµСЂР¶РґРµРЅРёРµ РїСЂРёРµРјР° Р±РµР· РґР°РЅРЅС‹С… РїРѕРґС‚РІРµСЂР¶РґРµРЅРёСЏ",
    ("POST", "/api/v2/clients/{client_id}/invoices"): "СЃРѕР·РґР°РЅРёРµ СЃС‡РµС‚Р° Р±РµР· РґР°РЅРЅС‹С… СЃС‡РµС‚Р°",
    ("POST", "/api/v2/clients/{client_id}/payments"): "РѕРїР»Р°С‚Р° СЃС‡РµС‚Р° Р±РµР· РґР°РЅРЅС‹С… РїР»Р°С‚РµР¶Р°",
    ("POST", "/api/v2/medicalcards/{medicalcard_id}/vaccinations/{pet_id}"): "СЃРѕР·РґР°РЅРёРµ РІР°РєС†РёРЅР°С†РёРё Р±РµР· РґР°РЅРЅС‹С… РІР°РєС†РёРЅР°С†РёРё",
    ("PATCH", "/api/v2/medicalcards/{medicalcard_id}/vaccinations/{vaccination_id}"): "РѕР±РЅРѕРІР»РµРЅРёРµ РІР°РєС†РёРЅР°С†РёРё Р±РµР· РґР°РЅРЅС‹С… РІР°РєС†РёРЅР°С†РёРё",
    ("PATCH", "/api/v1/medicalcards/vaccinations/{vaccination_id}"): "РєРѕСЂРѕС‚РєРѕРµ РѕР±РЅРѕРІР»РµРЅРёРµ РІР°РєС†РёРЅР°С†РёРё Р±РµР· РґР°РЅРЅС‹С… РІР°РєС†РёРЅР°С†РёРё",
    ("POST", "/api/v2/clients/{client_id}/medicalcards"): "СЃРѕР·РґР°РЅРёРµ РјРµРґРєР°СЂС‚С‹ Р±РµР· РґР°РЅРЅС‹С… РјРµРґРєР°СЂС‚С‹",
    ("POST", "/api/v2/medicalcards/uploadfiles"): "Р·Р°РіСЂСѓР·РєР° С„Р°Р№Р»РѕРІ РјРµРґРєР°СЂС‚С‹ Р±РµР· РґР°РЅРЅС‹С… С„Р°Р№Р»Р°",
    ("POST", "/api/v2/medicalcards/generate-llm"): "РіРµРЅРµСЂР°С†РёСЏ С‚РµРєСЃС‚Р° РјРµРґРєР°СЂС‚С‹ Р±РµР· prompt",
    ("PATCH", "/api/v2/clients/{client_id}/medicalcards/88"): "РѕР±РЅРѕРІР»РµРЅРёРµ РјРµРґРєР°СЂС‚С‹ Р±РµР· РґР°РЅРЅС‹С… РјРµРґРєР°СЂС‚С‹",
    ("POST", "/api/v2/combomanuals/streets"): "СЃРѕР·РґР°РЅРёРµ СѓР»РёС†С‹ Р±РµР· РґР°РЅРЅС‹С… СѓР»РёС†С‹",
    ("POST", "/api/v2/combomanuals/cities"): "СЃРѕР·РґР°РЅРёРµ РіРѕСЂРѕРґР° Р±РµР· РґР°РЅРЅС‹С… РіРѕСЂРѕРґР°",
    ("POST", "/api/v2/diagnoses"): "СЃРѕР·РґР°РЅРёРµ РґРёР°РіРЅРѕР·Р° Р±РµР· РґР°РЅРЅС‹С… РґРёР°РіРЅРѕР·Р°",
    ("PATCH", "/api/v2/diagnoses/{diagnos_id}"): "РѕР±РЅРѕРІР»РµРЅРёРµ РґРёР°РіРЅРѕР·Р° Р±РµР· РґР°РЅРЅС‹С… РґРёР°РіРЅРѕР·Р°",
    ("DELETE", "/api/v2/diagnoses/{diagnos_id}"): "СѓРґР°Р»РµРЅРёРµ РґРёР°РіРЅРѕР·Р° Р±РµР· РѕР±СЏР·Р°С‚РµР»СЊРЅС‹С… РґР°РЅРЅС‹С…",
}


def _invalid_auth_title(method: str, path: str) -> str:
    return f"РќРµРІРµСЂРЅР°СЏ Р°РІС‚РѕСЂРёР·Р°С†РёСЏ: {method} {path}"


def _invalid_path_title(method: str, path: str) -> str:
    return f"РќРµРІР°Р»РёРґРЅС‹Р№ path-РїР°СЂР°РјРµС‚СЂ: {method} {path}"


def _empty_body_title(method: str, path: str) -> str:
    action = EMPTY_BODY_TITLES.get((method, path), "Р·Р°РїСЂРѕСЃ Р±РµР· РѕР±СЏР·Р°С‚РµР»СЊРЅРѕРіРѕ С‚РµР»Р°")
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


