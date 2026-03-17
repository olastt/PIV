import allure
from dotenv import load_dotenv
from base.methods.users.users_methods import UserMethods

load_dotenv()


class UserStart:
    def __init__(self):
        self.users = UserMethods()

    def get_user_by_id(self, user_id: int = 1):
        with allure.step("Отправка запроса GET /api/v2/users/{user_id}"):
            response = self.users.get_user_by_id(user_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_user_home(self, user_id: int = 1, clinic_id: str = None):
        params = {"clinic_id": clinic_id} if clinic_id else None
        with allure.step("Запрос данных домашней страницы"):
            response = self.users.get_user_home(user_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_user_stores(self, user_id: int = 1):
        with allure.step("Запрос складов пользователя"):
            response = self.users.get_user_stores(user_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_user_allowed_clinics(self, user_id: int = 1):
        with allure.step("Запрос разрешённых клиник"):
            response = self.users.get_user_allowed_clinics(user_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_doctors(self, allow_limited: str = "0"):
        params = {"allow_limited": allow_limited}
        with allure.step("Запрос списка врачей"):
            response = self.users.get_doctors(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response