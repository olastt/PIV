import os

import allure
from base.methods.clients.clients_methods import ClientsMethods
from tests.data.clients_payloads import default_create_client_payload


class ClientsStart:
    """РЎС‚Р°СЂС‚РѕРІС‹Рµ СЃС†РµРЅР°СЂРёРё РґР»СЏ РєР»РёРµРЅС‚РѕРІ (Clients)."""

    def __init__(self):
        self.clients = ClientsMethods()

    def get_client_by_id(self, client_id=1):
        with allure.step("Р—Р°РїСЂРѕСЃ РєР»РёРµРЅС‚Р° РїРѕ ID"):
            response = self.clients.get_client_by_id(client_id)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response
    def get_clients_search(self, search_query="РўРµСЃС‚РѕРІРёС‡", page_number=1, page_size=20):
        params = {"search_query": search_query, "page[number]": page_number, "page[size]": page_size}
        with allure.step("РџРѕРёСЃРє РєР»РёРµРЅС‚РѕРІ"):
            response = self.clients.get_clients_search(params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_client_pets(self, client_id=1, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ РїРёС‚РѕРјС†РµРІ РєР»РёРµРЅС‚Р°"):
            response = self.clients.get_client_pets(client_id, params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def post_client(self):
        json_data = default_create_client_payload()
        with allure.step("РЎРѕР·РґР°РЅРёРµ РєР»РёРµРЅС‚Р°"):
            response = self.clients.post_client(json_data)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР°"):
            response.assert_status_code(200)
        return response

    def patch_client(self, client_id=1, json_data: dict = None):
        if json_data is None:
            json_data = {
                "client_data": {
                    "note": "pytest patch client",
                }
            }
        with allure.step("РћР±РЅРѕРІР»РµРЅРёРµ РєР»РёРµРЅС‚Р°"):
            response = self.clients.patch_client(client_id, json_data)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_client_match(self, client_id=1, client_data_cell_phone="+38(232)131-23-11",
                         client_data_first_name="РўРµСЃС‚", client_data_last_name="РўРµСЃС‚РѕРІ",
                         client_data_middle_name= "РўРµСЃС‚РѕРІРёС‡"):
        params = {
            "client_data[cell_phone]": client_data_cell_phone,
            "client_data[first_name]": client_data_first_name,
            "client_data[last_name]": client_data_last_name,
            "client_data[middle_name]": client_data_middle_name,
        }
        with allure.step("Р—Р°РїСЂРѕСЃ СЃРѕРїРѕСЃС‚Р°РІР»РµРЅРёСЏ РєР»РёРµРЅС‚Р°"):
            response = self.clients.get_client_match(client_id, params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_client_contacts(self, client_id=1, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ РєРѕРЅС‚Р°РєС‚РѕРІ РєР»РёРµРЅС‚Р°"):
            response = self.clients.get_client_contacts(client_id, params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_client_pet_by_id(self, client_id=1, pet_id=1, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ РїРёС‚РѕРјС†Р° РєР»РёРµРЅС‚Р° РїРѕ ID"):
            response = self.clients.get_client_pet_by_id(client_id, pet_id, params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response
