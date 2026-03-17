import allure
import pytest


@allure.epic("API по Swagger")
@allure.feature("Combomanuals")
class TestCombomanualsPositive:
    @pytest.mark.positive
    @allure.title("GET /api/v2/combomanuals/{id} — справочник по ID")
    def test_get_combomanuals_by_id(self, combomanuals_start):
        combomanuals_start.get_combomanuals_by_id(combomanuals_id=1)

    @pytest.mark.positive
    @allure.title("GET /api/v2/combomanuals/vaccinationstypes — типы вакцинаций")
    def test_get_vaccination_types(self, combomanuals_start):
        combomanuals_start.get_vaccination_types()

    @pytest.mark.positive
    @allure.title("GET /api/v2/combomanuals/reasonsofvisit — причины обращения")
    def test_get_reasons_of_visit(self, combomanuals_start):
        combomanuals_start.get_reasons_of_visit()

    @pytest.mark.positive
    @allure.title("GET /api/v2/combomanuals/cities — список городов")
    def test_get_cities(self, combomanuals_start):
        combomanuals_start.get_cities()

    @pytest.mark.positive
    @allure.title("GET /api/v2/combomanuals/typescities — типы городов")
    def test_get_types_cities(self, combomanuals_start):
        combomanuals_start.get_types_cities()

    @pytest.mark.positive
    @allure.title("GET /api/v2/combomanuals/{city_id}/streets — улицы города")
    def test_get_streets_by_city(self, combomanuals_start):
        combomanuals_start.get_streets_by_city(city_id=1)

    @pytest.mark.positive
    @allure.title("GET /api/v2/combomanuals/typesstreets — типы улиц")
    def test_get_types_streets(self, combomanuals_start):
        combomanuals_start.get_types_streets()
