import allure
import pytest
from Library.MakeyIS import Test


class TestClinicsPositive:
    @pytest.mark.positive
    @allure.epic('Клиники')
    @allure.feature('GET /api/v2/clinics')
    @allure.title('Получение всех клиник')
    @Test(run_test=True, group_name="Клиники", log=True)
    def test_get_clinics(self, clinic_start):
        clinic_start.get_all_clinics()

    @pytest.mark.positive
    @allure.epic('Клиники')
    @allure.feature('GET /api/v2/properties')
    @allure.title('Получение настроек клиники')
    @Test(run_test=True, group_name="Клиники", log=True)
    def test_get_clinic_properties(self, clinic_start):
        clinic_start.get_clinic_properties()
