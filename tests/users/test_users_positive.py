import os

import allure
import pytest

try:
    from Library.MakeyIS import Test
    HAS_MAKEYIS = True
except ImportError:
    HAS_MAKEYIS = False


def optional_test_decorator(func):
    """Декоратор Test из MakeyIS, если библиотека установлена."""
    if HAS_MAKEYIS:
        return Test(run_test=True, group_name="Пользователи", log=True)(func)
    return func


@allure.epic("API по Swagger")
@allure.feature("Users")
class TestUser:

    @pytest.mark.positive
    @allure.feature("GET /api/v2/users/{user_id}")
    @allure.title("Получение пользователя по ID")
    @optional_test_decorator
    def test_get_user_by_id(self, user_start):
        user_start.get_user_by_id()

    @pytest.mark.positive
    @allure.title("GET /api/v2/users/{user_id}/home — данные домашней страницы")
    def test_get_user_home(self, user_start):
        user_start.get_user_home(user_id=1)

    @pytest.mark.positive
    @allure.title("GET /api/v2/users/{user_id}/stores — склады пользователя")
    def test_get_user_stores(self, user_start):
        user_start.get_user_stores(user_id=1)

    @pytest.mark.positive
    @allure.title("GET /api/v2/users/{user_id}/schedules — расписание")
    def test_get_user_schedules(self, user_start):
        user_start.get_user_schedules(user_id=1)

    @pytest.mark.positive
    @allure.title("GET /api/v2/users/{user_id}/settings/payment — настройки оплат")
    def test_get_user_settings_payment(self, user_start):
        user_start.get_user_settings_payment(user_id=1)

    @pytest.mark.positive
    @allure.title("GET /api/v2/users/{user_id}/allowedclinics — разрешённые клиники (V2)")
    def test_get_user_allowed_clinics(self, user_start):
        user_start.get_user_allowed_clinics(user_id=1)

    @pytest.mark.positive
    @allure.title("PATCH /api/v2/users/{user_id} — обновление пользователя (nickname)")
    def test_patch_user(self, user_start):
        user_start.patch_user(user_id=1)

    @pytest.mark.positive
    @allure.title("PATCH /api/v2/users/settings/payment/{record_id}")
    def test_patch_user_settings_payment(self, user_start):
        user_start.patch_user_settings_payment(record_id=int(os.getenv("SETTINGS_PAYMENT_RECORD_ID", "0")))

    @pytest.mark.positive
    @allure.title("POST /api/v2/users/settings/payment/0 — создание настроек оплат")
    def test_post_user_settings_payment_create(self, user_start):
        user_start.post_user_settings_payment_create()

    @pytest.mark.positive
    @pytest.mark.skipif(
        not os.getenv("ENABLE_LOGOUT_API_TEST"),
        reason="POST logout отзывает токен; задайте ENABLE_LOGOUT_API_TEST=1 для ручного прогона",
    )
    @allure.title("POST /api/v2/users/{user_id}/logout")
    def test_post_user_logout(self, user_start):
        user_start.post_user_logout(user_id=1)

    @pytest.mark.positive
    @allure.title("GET /api/v2/users/doctors — список врачей")
    def test_get_doctors(self, user_start):
        user_start.get_doctors(allow_limited="0")