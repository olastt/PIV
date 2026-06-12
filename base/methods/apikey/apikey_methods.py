import os

import allure

from base.piv_client import PivApiClient
from src.config.url import Url


class ApikeyMethods(PivApiClient):
    """byClinicCode вызывается с collection key (md5), не с clinic apiKey."""

    def __init__(self):
        collection_key = os.getenv("API_TOKEN_COLLECTION")
        super().__init__(api_key=collection_key)

    @allure.step("GET /apiKey/byClinicCode — apiKey клиники по коду")
    def get_api_key_by_clinic_code(self, code: str):
        return self.get(Url.GET_API_KEY_BY_CLINIC_CODE, params={"code": code})
