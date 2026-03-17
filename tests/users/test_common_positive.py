# Тесты по Swagger: Properties, Checkversion, Clinics, Cassa, Tariff, Billing, Roles, Hospital, Combomanuals, Diagnoses
import allure
import pytest


@allure.epic("API по Swagger")
@allure.feature("Properties / Checkversion / Clinics / Cassa / Tariff / Billing / Roles / Hospital / Combomanuals / Diagnoses")
class TestCommonPositive:

    @pytest.mark.positive
    @allure.title("GET /api/v2/properties — настройки клиники")
    def test_get_properties(self, common_start):
        common_start.get_properties()

    @pytest.mark.positive
    @allure.title("GET /api/v2/checkversion — проверка версии приложения")
    def test_get_checkversion(self, common_start):
        common_start.get_checkversion()


    @pytest.mark.positive
    @allure.title("GET /api/v2/cassa/{user_id} — кассы пользователя")
    def test_get_cassa_by_user(self, common_start):
        common_start.get_cassa_by_user(user_id=1)

    @pytest.mark.positive
    @allure.title("GET /api/v2/tariff — данные тарифа")
    def test_get_tariff(self, common_start):
        common_start.get_tariff()

    @pytest.mark.positive
    @allure.title("GET /api/v2/billingurl — ссылка на биллинг")
    def test_get_billing_url(self, common_start):
        common_start.get_billing_url()

    @pytest.mark.positive
    @allure.title("GET /api/v2/roles/{id_role} — роль по ID")
    def test_get_role_by_id(self, common_start):
        common_start.get_role_by_id(id_role=1)

    @pytest.mark.positive
    @allure.title("GET /api/v2/hospital — данные стационара")
    def test_get_hospital(self, common_start):
        common_start.get_hospital()

    @pytest.mark.positive
    @allure.title("GET /api/v2/hospital/blocks — блоки стационара")
    def test_get_hospital_blocks(self, common_start):
        common_start.get_hospital_blocks()

    @pytest.mark.positive
    @allure.title("GET /api/v2/hospital/liststatuses — статусы стационара")
    def test_get_hospital_list_statuses(self, common_start):
        common_start.get_hospital_list_statuses()

    @pytest.mark.positive
    @allure.title("GET /api/v2/combomanuals/cities — список городов")
    def test_get_cities(self, common_start):
        common_start.get_cities()

    @pytest.mark.positive
    @allure.title("GET /api/v2/combomanuals/typescities — типы городов")
    def test_get_types_cities(self, common_start):
        common_start.get_types_cities()

    @pytest.mark.positive
    @allure.title("GET /api/v2/combomanuals/reasonsofvisit — причины обращения")
    def test_get_reasons_of_visit(self, common_start):
        common_start.get_reasons_of_visit()

    @pytest.mark.positive
    @allure.title("GET /api/v2/combomanuals/vaccinationstypes — типы вакцинаций")
    def test_get_vaccination_types(self, common_start):
        common_start.get_vaccination_types()

    @pytest.mark.positive
    @allure.title("GET /api/v2/diagnoses — список диагнозов")
    def test_get_diagnoses(self, common_start):
        common_start.get_diagnoses()
