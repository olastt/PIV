import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class CombomanualsMethods(ApiClient):
    """Методы для справочников (Combomanuals)."""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/combomanuals/{combomanuals_id} - Данные справочника по ID")
    def get_combomanuals_by_id(self, combomanuals_id: int, params: dict = None):
        endpoint = Url.GET_COMBOMANUALS_BY_ID.replace("{combomanuals_id}", str(combomanuals_id))
        return self.get(endpoint, params=params)

    @allure.step("GET /api/v2/combomanuals/vaccinationstypes - Типы вакцинаций")
    def get_vaccination_types(self, params: dict = None):
        return self.get(Url.GET_VACCINATION_TYPES, params=params)

    @allure.step("GET /api/v2/combomanuals/reasonsofvisit - Причины обращения")
    def get_reasons_of_visit(self, params: dict = None):
        return self.get(Url.GET_REASONS_OF_VISIT, params=params)

    @allure.step("GET /api/v2/combomanuals/resultofvisit - Результаты визита (ResultOfVisitData)")
    def get_result_of_visit(self, params: dict = None):
        return self.get(Url.GET_RESULT_OF_VISIT, params=params)

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

    @allure.step("POST /api/v2/combomanuals/streets - Создание улицы (createStreet)")
    def post_street(self, json_data: dict):
        return self.post(Url.POST_STREETS, json_data=json_data)

    @allure.step("POST /api/v2/combomanuals/cities - Создание города (createCity)")
    def post_city(self, json_data: dict):
        return self.post(Url.POST_CITIES, json_data=json_data)
