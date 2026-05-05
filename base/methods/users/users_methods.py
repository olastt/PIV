import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class UserMethods(ApiClient):
    """Методы для пользователей (Users, Doctors по Swagger)"""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/users/{user_id} - Получение пользователя по ID")
    def get_user_by_id(self, user_id: int, params: dict = None):
        endpoint = Url.GET_USER_BY_ID.replace("{user_id}", str(user_id))
        return self.get(endpoint, params=params)

    @allure.step("PATCH /api/v2/users/{user_id} - Обновление пользователя")
    def patch_user(self, user_id: int, json_data: dict):
        endpoint = Url.PATCH_USER.replace("{user_id}", str(user_id))
        return self.patch(endpoint, json_data=json_data)

    @allure.step("GET /api/v2/users/{user_id}/home - Данные домашней страницы")
    def get_user_home(self, user_id: int, params: dict = None):
        endpoint = Url.GET_USER_HOME.replace("{user_id}", str(user_id))
        return self.get(endpoint, params=params)

    @allure.step("GET /api/v2/users/{user_id}/settings/payment - Настройки оплат")
    def get_user_settings_payment(self, user_id: int):
        endpoint = Url.GET_USER_SETTINGS_PAYMENT.replace("{user_id}", str(user_id))
        return self.get(endpoint)

    @allure.step("PATCH /api/v2/users/settings/payment/{record_id} - Обновление настроек оплат")
    def patch_user_settings_payment(self, record_id: int, json_data: dict):
        endpoint = Url.PATCH_USER_SETTINGS_PAYMENT.replace("{record_id}", str(record_id))
        return self.patch(endpoint, json_data=json_data)

    @allure.step("POST /api/v2/users/settings/payment/0 - Создание настроек оплат")
    def post_user_settings_payment_create(self, json_data: dict):
        return self.post(Url.POST_USER_SETTINGS_PAYMENT_CREATE, json_data=json_data)

    @allure.step("GET /api/v2/users/{user_id}/stores - Склады по пользователю")
    def get_user_stores(self, user_id: int):
        endpoint = Url.GET_USER_STORES.replace("{user_id}", str(user_id))
        return self.get(endpoint)

    @allure.step("GET /api/v2/users/{user_id}/schedules - Расписание пользователя")
    def get_user_schedules(self, user_id: int, params: dict = None):
        endpoint = Url.GET_USER_SCHEDULES.replace("{user_id}", str(user_id))
        return self.get(endpoint, params=params)

    @allure.step("GET /api/v1/users/{user_id}/allowedclinics - Разрешённые клиники")
    def get_user_allowed_clinics(self, user_id: int):
        endpoint = Url.GET_USER_ALLOWED_CLINICS.replace("{user_id}", str(user_id))
        return self.get(endpoint)

    @allure.step("POST /api/v2/users/{user_id}/logout - Выход")
    def post_user_logout(self, user_id: int, json_data: dict):
        endpoint = Url.POST_USER_LOGOUT.replace("{user_id}", str(user_id))
        return self.post(endpoint, json_data=json_data)

    @allure.step("GET /api/v2/users/doctors - Список врачей")
    def get_doctors(self, params: dict = None):
        return self.get(Url.GET_DOCTORS, params=params)

    # ==================== Admission ====================
    @allure.step("GET /api/v2/users/admission/{admission_id} - Приём по ID")
    def get_admission_by_id(self, admission_id: int):
        endpoint = Url.GET_ADMISSION_BY_ID.replace("{admission_id}", str(admission_id))
        return self.get(endpoint)

    @allure.step("GET /api/v2/users/{user_id}/admission - Приёмы пользователя")
    def get_admissions_by_user(self, user_id: int, params: dict):
        endpoint = Url.GET_ADMISSIONS_BY_USER.replace("{user_id}", str(user_id))
        return self.get(endpoint, params=params)

    # ==================== Calls ====================
    @allure.step("GET /api/v2/users/{user_id}/calls - Прозвоны пользователя")
    def get_user_calls(self, user_id: int, params: dict):
        endpoint = Url.GET_USER_CALLS.replace("{user_id}", str(user_id))
        return self.get(endpoint, params=params)

    @allure.step("GET /api/v2/calls/search - Поиск прозвонов")
    def get_calls_search(self, params: dict):
        return self.get(Url.GET_CALLS_SEARCH, params=params)

