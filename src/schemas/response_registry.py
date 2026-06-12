from urllib.parse import urlparse

from src.schemas.piv.get_admissions import GetAdmissionsResponse
from src.schemas.piv.get_api_key_by_clinic_code import GetApiKeyByClinicCodeResponse
from src.schemas.piv.get_articles import GetArticlesResponse
from src.schemas.piv.get_client_by_phone import GetClientByPhoneResponse
from src.schemas.piv.get_clinics import GetClinicsFlatResponse, GetClinicsResponse
from src.schemas.piv.get_discount_card import GetDiscountCardListResponse, GetDiscountCardResponse
from src.schemas.piv.get_domain_name import GetDomainNameResponse
from src.schemas.piv.get_last_three_articles import GetLastThreeArticlesResponse
from src.schemas.piv.get_phone_prefix import GetPhonePrefixResponse
from src.schemas.piv.get_recomendations import GetRecomendationsResponse
from src.schemas.piv.get_sms_check import GetSmsCheckResponse
from src.schemas.piv.get_vaccinations import GetVaccinationsResponse
from src.schemas.piv.post_event import PostEventResponse
from src.schemas.piv.post_get_token import GetTokenResponse
from src.schemas.piv.post_sms_send import PostSendSmsResponse

PIV_RESPONSE_SCHEMAS = {
    "/apiKey/byClinicCode": GetApiKeyByClinicCodeResponse,
    "/clients/clientByPhone": GetClientByPhoneResponse,
    "/getPhonePrefix": GetPhonePrefixResponse,
    "/sms/send": PostSendSmsResponse,
    "/sms/check": GetSmsCheckResponse,
    "/domainName": GetDomainNameResponse,
    "/admissions": GetAdmissionsResponse,
    "/medicalCards/recomendations": GetRecomendationsResponse,
    "/medicalCards/vaccinations": GetVaccinationsResponse,
    "/clinics": (GetClinicsResponse, GetClinicsFlatResponse),
    "/articles/lastThree": GetLastThreeArticlesResponse,
    "/articles": GetArticlesResponse,
    "/event": PostEventResponse,
    "/discountCard": (GetDiscountCardResponse, GetDiscountCardListResponse),
    "/token_auth.php": GetTokenResponse,
}


def _normalize_path(url) -> str:
    path = urlparse(str(url)).path.rstrip("/") or "/"
    for prefix in ("/api/v2", "/api/v1"):
        if path.startswith(prefix):
            path = path[len(prefix):] or "/"
            break
    return path


def schema_for_response(response):
    path = _normalize_path(response.url)
    schema = PIV_RESPONSE_SCHEMAS.get(path)
    if schema is None:
        return None
    if isinstance(schema, tuple):
        body = response.json() if response.content else {}
        data = body.get("data") if isinstance(body, dict) else None
        if isinstance(data, list):
            return schema[1]
        if isinstance(data, dict) and "clinics" in data:
            return schema[0]
        if isinstance(data, dict) and "card" in data:
            return schema[0]
        if isinstance(data, dict) and "id" in data and "title" in data and "address" in data:
            return schema[1]
        return schema[0]
    return schema
