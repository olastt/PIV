import os

import allure
import pytest
from Library.MakeyIS import Test


class TestUser:
    @pytest.mark.positive
    @allure.epic("Пользователи")
    @allure.feature("GET /api/v2/users/{user_id}")
    @allure.title("Получение пользователя по ID")
    @Test(run_test=True, group_name="Пользователи", log=True)
    def test_get_user_by_id(self, user_start):
        user_start.get_user_by_id()

    @pytest.mark.positive
    @allure.epic("Пользователи")
    @allure.feature("GET /api/v2/users/{user_id}/home")
    @allure.title("Получение данных домашней страницы пользователя")
    @Test(run_test=True, group_name="Пользователи", log=True)
    def test_get_user_home(self, user_start):
        user_start.get_user_home(user_id=1)

    @pytest.mark.positive
    @allure.epic("Пользователи")
    @allure.feature("GET /api/v2/users/{user_id}/stores")
    @allure.title("Получение складов пользователя")
    @Test(run_test=True, group_name="Пользователи", log=True)
    def test_get_user_stores(self, user_start):
        user_start.get_user_stores(user_id=1)

    @pytest.mark.positive
    @allure.epic("Пользователи")
    @allure.feature("GET /api/v2/users/{user_id}/schedules")
    @allure.title("Получение расписания пользователя")
    @Test(run_test=True, group_name="Пользователи", log=True)
    def test_get_user_schedules(self, user_start):
        user_start.get_user_schedules(user_id=1)

    @pytest.mark.positive
    @allure.epic("Пользователи")
    @allure.feature("GET /api/v2/users/{user_id}/settings/payment")
    @allure.title("Получение настроек оплат пользователя")
    @Test(run_test=True, group_name="Пользователи", log=True)
    def test_get_user_settings_payment(self, user_start):
        user_start.get_user_settings_payment(user_id=1)

    @pytest.mark.positive
    @allure.epic("Пользователи")
    @allure.feature("GET /api/v2/users/{user_id}/allowedclinics")
    @allure.title("Получение разрешённых клиник пользователя")
    @Test(run_test=True, group_name="Пользователи", log=True)
    def test_get_user_allowed_clinics(self, user_start):
        user_start.get_user_allowed_clinics(user_id=1)

    @pytest.mark.positive
    @allure.epic("Пользователи")
    @allure.feature("PATCH /api/v2/users/{user_id}")
    @allure.title("Обновление пользователя")
    @Test(run_test=True, group_name="Пользователи", log=True)
    def test_patch_user(self, user_start):
        user_start.patch_user(user_id=1)

    @pytest.mark.positive
    @allure.epic("Пользователи")
    @allure.feature("PATCH /api/v2/users/settings/payment/{record_id}")
    @allure.title("Обновление настроек оплат пользователя")
    @Test(run_test=True, group_name="Пользователи", log=True)
    def test_patch_user_settings_payment(self, user_start):
        user_start.patch_user_settings_payment(record_id=int(os.getenv("SETTINGS_PAYMENT_RECORD_ID", "0")))

    @pytest.mark.positive
    @allure.epic("Пользователи")
    @allure.feature("POST /api/v2/users/settings/payment/0")
    @allure.title("Создание настроек оплат пользователя")
    @Test(run_test=True, group_name="Пользователи", log=True)
    def test_post_user_settings_payment_create(self, user_start):
        user_start.post_user_settings_payment_create()

    @pytest.mark.positive
    @pytest.mark.skipif(
        not os.getenv("ENABLE_LOGOUT_API_TEST"),
        reason="POST logout отзывает токен; задайте ENABLE_LOGOUT_API_TEST=1 для ручного прогона",
    )
    @allure.epic("Пользователи")
    @allure.feature("POST /api/v2/users/{user_id}/logout")
    @allure.title("Выход пользователя из системы")
    @Test(run_test=True, group_name="Пользователи", log=True)
    def test_post_user_logout(self, user_start):
        user_start.post_user_logout(user_id=1)

    @pytest.mark.positive
    @allure.epic("Пользователи")
    @allure.feature("GET /api/v2/users/doctors")
    @allure.title("Получение списка врачей")
    @Test(run_test=True, group_name="Пользователи", log=True)
    def test_get_doctors(self, user_start):
        user_start.get_doctors(allow_limited="0")
