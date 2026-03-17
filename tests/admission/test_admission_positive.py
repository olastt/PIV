import allure
import pytest
from Library.MakeyIS import Test


class TestAdmissionPositive:
    @pytest.mark.positive
    @allure.epic('Приемы')
    @allure.feature('GET /api/v2/users/admission/{admission_id}')
    @allure.title('Получение приема по ID')
    @Test(run_test=True, group_name="Приемы", log=True)
    def test_get_admission_by_id(self, admission_start):
        admission_start.get_admission_by_id(admission_id=1)
    #
    # @pytest.mark.positive
    # @allure.title("GET /api/v2/users/{user_id}/admission — приёмы пользователя")
    # def test_get_admissions_by_user(self, admission_start):
    #     admission_start.get_admissions_by_user(user_id=1416)
