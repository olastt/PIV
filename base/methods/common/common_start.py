import allure
from base.methods.common.common_methods import CommonMethods


class CommonStart:
    """Стартовые сценарии для Properties, Checkversion, Clinics, Cassa, Tariff, Hospital и др."""

    def __init__(self):
        self.common = CommonMethods()

    def get_properties(self, params=None):
        with allure.step("Запрос настроек клиники (properties)"):
            response = self.common.get_properties(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_checkversion(self, params=None):
        with allure.step("Запрос проверки версии"):
            response = self.common.get_checkversion(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_clinics(self, params=None):
        with allure.step("Запрос списка клиник"):
            response = self.common.get_clinics(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_cassa_by_user(self, user_id=1):
        with allure.step("Запрос касс пользователя"):
            response = self.common.get_cassa_by_user(user_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_tariff(self, params=None):
        with allure.step("Запрос тарифа"):
            response = self.common.get_tariff(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_billing_url(self, params=None):
        with allure.step("Запрос ссылки на биллинг"):
            response = self.common.get_billing_url(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_role_by_id(self, id_role=1):
        with allure.step("Запрос роли по ID"):
            response = self.common.get_role_by_id(id_role)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_hospital(self, params=None):
        with allure.step("Запрос данных стационара"):
            response = self.common.get_hospital(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_hospital_blocks(self, params=None):
        with allure.step("Запрос блоков стационара"):
            response = self.common.get_hospital_blocks(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_hospital_list_statuses(self, params=None):
        with allure.step("Запрос статусов стационара"):
            response = self.common.get_hospital_list_statuses(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_cities(self, params=None):
        with allure.step("Запрос списка городов"):
            response = self.common.get_cities(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_types_cities(self, params=None):
        with allure.step("Запрос типов городов"):
            response = self.common.get_types_cities(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_reasons_of_visit(self, params=None):
        with allure.step("Запрос причин обращения"):
            response = self.common.get_reasons_of_visit(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_vaccination_types(self, params=None):
        with allure.step("Запрос типов вакцинаций"):
            response = self.common.get_vaccination_types(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_diagnoses(self, params=None):
        with allure.step("Запрос списка диагнозов"):
            response = self.common.get_diagnoses(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    # def get_redis_clear(self, params=None):
    #     with allure.step("GET /api/v2/redis/clear — очистка Redis"):
    #         response = self.common.get_redis_clear(params=params)
    #     with allure.step("Проверка статус кода 200"):
    #         response.assert_status_code(200)
    #     return response
