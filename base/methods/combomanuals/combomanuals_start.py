import allure
from base.methods.combomanuals.combomanuals_methods import CombomanualsMethods
from src.utils.fakers import random_city


class CombomanualsStart:
    """Стартовые сценарии для Combomanuals."""

    def __init__(self):
        self.combomanuals = CombomanualsMethods()

    def get_combomanuals_by_id(self, combomanuals_id=1, params=None):
        with allure.step("Запрос справочника по ID"):
            response = self.combomanuals.get_combomanuals_by_id(combomanuals_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_vaccination_types(self, params=None):
        with allure.step("Запрос типов вакцинаций"):
            response = self.combomanuals.get_vaccination_types(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_reasons_of_visit(self, params=None):
        with allure.step("Запрос причин обращения"):
            response = self.combomanuals.get_reasons_of_visit(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_result_of_visit(self, params=None):
        with allure.step("Запрос результатов визита"):
            response = self.combomanuals.get_result_of_visit(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_cities(self, params=None):
        with allure.step("Запрос списка городов"):
            response = self.combomanuals.get_cities(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_types_cities(self, params=None):
        with allure.step("Запрос типов городов"):
            response = self.combomanuals.get_types_cities(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_streets_by_city(self, city_id=252, page_number=1, page_size=20):
        params = {
            "page[number]": page_number,
            "page[size]": page_size
        }
        with allure.step("Запрос улиц города"):
            response = self.combomanuals.get_streets_by_city(city_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_types_streets(self, params=None):
        with allure.step("Запрос типов улиц"):
            response = self.combomanuals.get_types_streets(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def post_street(self):
        json_data = {
            "street_data": {
                "title": "Test Street",
                "type": 1,
                "city_id": 252,
            }
        }
        with allure.step("Создание улицы (createStreet)"):
            response = self.combomanuals.post_street(json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code(200)
        return response

    def post_city(self):
        json_data = {
            "city_data": {
                "title": random_city(),
                "type_id": 252,
            }
        }
        with allure.step("Создание города (createCity)"):
            response = self.combomanuals.post_city(json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code(200)
        return response
