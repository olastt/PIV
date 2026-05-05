import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class CommonMethods(ApiClient):
    """Методы для Properties, Checkversion, Clinics, Cassa, Tariff, Billing, Roles, Hospital (Swagger)"""

    def __init__(self):
        super().__init__()

    # ==================== Checkversion ====================
    @allure.step("GET /api/v2/checkversion - Проверка версии приложения")
    def get_checkversion(self, params: dict = None):
        return self.get(Url.GET_CHECKVERSION, params=params)

    # ==================== Clinics ====================
    @allure.step("GET /api/v2/clinics - Список клиник")
    def get_clinics(self, params: dict = None):
        return self.get(Url.GET_CLINICS, params=params)

    @allure.step("GET /api/v2/properties - Настройки клиники")
    def get_properties(self, params: dict = None):
        return self.get(Url.GET_PROPERTIES, params=params)

    @allure.step("GET /api/v2/redis/clear - Очистка Redis (служебный)")
    def get_redis_clear(self, params: dict = None):
        return self.get(Url.GET_REDIS_CLEAR, params=params)

    # ==================== Cassa ====================
    @allure.step("GET /api/v2/cassa/{user_id} - Кассы пользователя")
    def get_cassa_by_user(self, user_id: int):
        endpoint = Url.GET_CASSA_BY_USER.replace("{user_id}", str(user_id))
        return self.get(endpoint)

    # ==================== Tariff ====================
    @allure.step("GET /api/v2/tariff - Данные тарифа")
    def get_tariff(self, params: dict = None):
        return self.get(Url.GET_TARIFF, params=params)

    # ==================== Billing ====================
    @allure.step("GET /api/v2/billingurl - Ссылка на биллинг")
    def get_billing_url(self, params: dict = None):
        return self.get(Url.GET_BILLING_URL, params=params)

    # ==================== Roles ====================
    @allure.step("GET /api/v2/roles/{id_role} - Роль по ID")
    def get_role_by_id(self, id_role: int):
        endpoint = Url.GET_ROLE_BY_ID.replace("{id_role}", str(id_role))
        return self.get(endpoint)

    # ==================== Hospital ====================
    @allure.step("GET /api/v2/hospital - Данные стационара")
    def get_hospital(self, params: dict = None):
        return self.get(Url.GET_HOSPITAL, params=params)

    @allure.step("GET /api/v2/hospital/blocks - Блоки стационара")
    def get_hospital_blocks(self, params: dict = None):
        return self.get(Url.GET_HOSPITAL_BLOCKS, params=params)

    @allure.step("GET /api/v2/hospital/liststatuses - Статусы стационара")
    def get_hospital_list_statuses(self, params: dict = None):
        return self.get(Url.GET_HOSPITAL_LIST_STATUSES, params=params)

    @allure.step("GET /api/v2/hospital/{recordId} - Запись стационара по ID")
    def get_hospital_by_id(self, record_id: int):
        endpoint = Url.GET_HOSPITAL_BY_ID.replace("{recordId}", str(record_id))
        return self.get(endpoint)

    # ==================== Combomanuals ====================
    @allure.step("GET /api/v2/combomanuals/{id} - Данные справочника")
    def get_combomanuals_by_id(self, combomanuals_id: int):
        endpoint = Url.GET_COMBOMANUALS_BY_ID.replace("{combomanuals_id}", str(combomanuals_id))
        return self.get(endpoint)

    @allure.step("GET /api/v2/combomanuals/vaccinationstypes - Типы вакцинаций")
    def get_vaccination_types(self, params: dict = None):
        return self.get(Url.GET_VACCINATION_TYPES, params=params)

    @allure.step("GET /api/v2/combomanuals/reasonsofvisit - Причины обращения")
    def get_reasons_of_visit(self, params: dict = None):
        return self.get(Url.GET_REASONS_OF_VISIT, params=params)

    @allure.step("GET /api/v2/combomanuals/cities - Список городов")
    def get_cities(self, params: dict = None):
        return self.get(Url.GET_CITIES, params=params)

    @allure.step("GET /api/v2/combomanuals/typescities - Типы городов")
    def get_types_cities(self, params: dict = None):
        return self.get(Url.GET_TYPES_CITIES, params=params)

    @allure.step("GET /api/v2/combomanuals/{city_id}/streets - Улицы города")
    def get_streets_by_city(self, city_id: int, params: dict = None):
        endpoint = Url.GET_STREETS_BY_CITY.replace("{city_id}", str(city_id))
        return self.get(endpoint, params=params)

    @allure.step("GET /api/v2/combomanuals/typesstreets - Типы улиц")
    def get_types_streets(self, params: dict = None):
        return self.get(Url.GET_TYPES_STREETS, params=params)

    # ==================== Diagnoses ====================
    @allure.step("GET /api/v2/diagnoses - Список диагнозов")
    def get_diagnoses(self, params: dict = None):
        return self.get(Url.GET_DIAGNOSES, params=params)

    @allure.step("GET /api/v2/diagnoses/{diagnos_id} - Диагноз по ID")
    def get_diagnos_by_id(self, diagnos_id: int):
        endpoint = Url.GET_DIAGNOS_BY_ID.replace("{diagnos_id}", str(diagnos_id))
        return self.get(endpoint)

    @allure.step("GET /api/v2/clients/medicalcards/diagnoses - Диагнозы для медкарт")
    def get_medicalcards_diagnoses(self, params: dict = None):
        return self.get(Url.GET_DIAGNOSES_FOR_MEDICALCARDS, params=params)
