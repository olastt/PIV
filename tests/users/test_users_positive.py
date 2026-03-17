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
    @allure.title("GET /api/v2/users/{user_id}/allowedclinics — разрешённые клиники")
    def test_get_user_allowed_clinics(self, user_start):
        user_start.get_user_allowed_clinics(user_id=1)

    @pytest.mark.positive
    @allure.title("GET /api/v2/users/doctors — список врачей")
    def test_get_doctors(self, user_start):
        user_start.get_doctors(allow_limited="0")