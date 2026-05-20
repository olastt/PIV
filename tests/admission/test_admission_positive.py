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
        admission_start.get_admission_by_id()

    @pytest.mark.positive
    @allure.epic('Приемы')
    @allure.feature('GET /api/v2/users/{user_id}/admission')
    @allure.title("Приёмы пользователя")
    @pytest.mark.parametrize(
        "filter_status",
        [
            "save",
            "accepted",
            "delayed",
            "deleted",
            "directed",
            "in_treatment",
            "not_approved",
            "not_confirmed",
        ],
    )
    @Test(run_test=True, group_name="Приемы", log=True)
    def test_get_admissions_by_user(self, admission_start, filter_status):
        admission_start.get_admissions_by_user(filter_status=filter_status)

    @pytest.mark.positive
    @allure.epic('Приемы')
    @allure.feature('POST /api/v2/users/{user_id}/admission')
    @allure.title('Создание приёма')
    @Test(run_test=True, group_name="Приемы", log=True)
    def test_create_admission(self, admission_start):
        admission_start.create_admission()
    #
    # @pytest.mark.positive
    # @allure.epic('Приемы')
    # @allure.feature('PATCH /api/v2/users/{user_id}/admission/{admission_id}')
    # @allure.title('Обновление приёма')
    # @Test(run_test=True, group_name="Приемы", log=True)
    # def test_patch_admission(self, admission_start):
    #     admission_start.patch_admission()
    #
    # @pytest.mark.positive
    # @allure.epic('Приемы')
    # @allure.feature('POST /api/v2/users/admission/{admission_id}/confirm')
    # @allure.title('Подтверждение приёма')
    # @Test(run_test=True, group_name="Приемы", log=True)
    # def test_confirm_admission(self, admission_start):
    #     admission_start.confirm_admission()
