import allure
from base.methods.common.common_methods import CommonMethods


class CommonStart:
    """РЎС‚Р°СЂС‚РѕРІС‹Рµ СЃС†РµРЅР°СЂРёРё РґР»СЏ Properties, Checkversion, Clinics, Cassa, Tariff, Hospital Рё РґСЂ."""

    def __init__(self):
        self.common = CommonMethods()

    def get_properties(self, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ РЅР°СЃС‚СЂРѕРµРє РєР»РёРЅРёРєРё (properties)"):
            response = self.common.get_properties(params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_checkversion(self, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ РїСЂРѕРІРµСЂРєРё РІРµСЂСЃРёРё"):
            response = self.common.get_checkversion(params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_clinics(self, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ СЃРїРёСЃРєР° РєР»РёРЅРёРє"):
            response = self.common.get_clinics(params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_cassa_by_user(self, user_id=1):
        with allure.step("Р—Р°РїСЂРѕСЃ РєР°СЃСЃ РїРѕР»СЊР·РѕРІР°С‚РµР»СЏ"):
            response = self.common.get_cassa_by_user(user_id)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_tariff(self, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ С‚Р°СЂРёС„Р°"):
            response = self.common.get_tariff(params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_billing_url(self, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ СЃСЃС‹Р»РєРё РЅР° Р±РёР»Р»РёРЅРі"):
            response = self.common.get_billing_url(params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_role_by_id(self, id_role=1):
        with allure.step("Р—Р°РїСЂРѕСЃ СЂРѕР»Рё РїРѕ ID"):
            response = self.common.get_role_by_id(id_role)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_hospital(self, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ РґР°РЅРЅС‹С… СЃС‚Р°С†РёРѕРЅР°СЂР°"):
            response = self.common.get_hospital(params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_hospital_blocks(self, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ Р±Р»РѕРєРѕРІ СЃС‚Р°С†РёРѕРЅР°СЂР°"):
            response = self.common.get_hospital_blocks(params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_hospital_list_statuses(self, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ СЃС‚Р°С‚СѓСЃРѕРІ СЃС‚Р°С†РёРѕРЅР°СЂР°"):
            response = self.common.get_hospital_list_statuses(params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_cities(self, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ СЃРїРёСЃРєР° РіРѕСЂРѕРґРѕРІ"):
            response = self.common.get_cities(params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_types_cities(self, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ С‚РёРїРѕРІ РіРѕСЂРѕРґРѕРІ"):
            response = self.common.get_types_cities(params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_reasons_of_visit(self, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ РїСЂРёС‡РёРЅ РѕР±СЂР°С‰РµРЅРёСЏ"):
            response = self.common.get_reasons_of_visit(params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_vaccination_types(self, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ С‚РёРїРѕРІ РІР°РєС†РёРЅР°С†РёР№"):
            response = self.common.get_vaccination_types(params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_diagnoses(self, params=None):
        with allure.step("Р—Р°РїСЂРѕСЃ СЃРїРёСЃРєР° РґРёР°РіРЅРѕР·РѕРІ"):
            response = self.common.get_diagnoses(params=params)
        with allure.step("РџСЂРѕРІРµСЂРєР° СЃС‚Р°С‚СѓСЃ РєРѕРґР° 200"):
            response.assert_status_code(200)
        return response

    def get_redis_clear(self, params=None):
        with allure.step("GET /api/v2/redis/clear"):
            response = self.common.get_redis_clear(params=params)
        with allure.step("Check status code 200"):
            response.assert_status_code(200)
        return response
