import allure
import pytest
from Library.MakeyIS import Test


class TestCombomanualsPositive:

    @pytest.mark.positive
    @allure.epic('Combomanuals')
    @allure.feature('GET /api/v2/combomanuals/{id}')
    @allure.title('Справочник по ID')
    @Test(run_test=True, group_name="Combomanuals", log=True)
    def test_get_combomanuals_by_id(self, combomanuals_start):
        combomanuals_start.get_combomanuals_by_id()

    @pytest.mark.positive
    @allure.epic('Combomanuals')
    @allure.feature('GET /api/v2/combomanuals/vaccinationstypes')
    @allure.title('Типы вакцинаций')
    @Test(run_test=True, group_name="Combomanuals", log=True)
    def test_get_vaccination_types(self, combomanuals_start):
        combomanuals_start.get_vaccination_types()

    @pytest.mark.positive
    @allure.epic('Combomanuals')
    @allure.feature('GET /api/v2/combomanuals/reasonsofvisit')
    @allure.title('Причины обращения')
    @Test(run_test=True, group_name="Combomanuals", log=True)
    def test_get_reasons_of_visit(self, combomanuals_start):
        combomanuals_start.get_reasons_of_visit()

    @pytest.mark.positive
    @allure.epic('Combomanuals')
    @allure.feature('GET /api/v2/combomanuals/cities')
    @allure.title('Список городов')
    @Test(run_test=True, group_name="Combomanuals", log=True)
    def test_get_cities(self, combomanuals_start):
        combomanuals_start.get_cities()

    @pytest.mark.positive
    @allure.epic('Combomanuals')
    @allure.feature('GET /api/v2/combomanuals/typescities')
    @allure.title('Типы городов')
    @Test(run_test=True, group_name="Combomanuals", log=True)
    def test_get_types_cities(self, combomanuals_start):
        combomanuals_start.get_types_cities()

    @pytest.mark.positive
    @allure.epic('Combomanuals')
    @allure.feature('GET /api/v2/combomanuals/{city_id}/streets')
    @allure.title('Улицы города')
    @Test(run_test=True, group_name="Combomanuals", log=True)
    def test_get_streets_by_city(self, combomanuals_start):
        combomanuals_start.get_streets_by_city()

    @pytest.mark.positive
    @allure.epic('Combomanuals')
    @allure.feature('GET /api/v2/combomanuals/typesstreets')
    @allure.title('Типы улиц')
    @Test(run_test=True, group_name="Combomanuals", log=True)
    def test_get_types_streets(self, combomanuals_start):
        combomanuals_start.get_types_streets()

    @pytest.mark.positive
    @allure.epic('Combomanuals')
    @allure.feature('GET /api/v2/combomanuals/resultofvisit')
    @allure.title('Результаты визита (ResultOfVisitData)')
    def test_get_result_of_visit(self, combomanuals_start):
        combomanuals_start.get_result_of_visit()

    @pytest.mark.positive
    @allure.epic('Combomanuals')
    @allure.feature('POST /api/v2/combomanuals/streets')
    @allure.title('Создание улицы (createStreet)')
    def test_create_street(self, combomanuals_start):
        combomanuals_start.post_street()

    @pytest.mark.positive
    @allure.epic('Combomanuals')
    @allure.feature('POST /api/v2/combomanuals/cities')
    @allure.title('Создание города (createCity)')
    def test_create_city(self, combomanuals_start):
        combomanuals_start.post_city()
