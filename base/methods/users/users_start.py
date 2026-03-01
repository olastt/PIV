import allure
from dotenv import load_dotenv
from base.methods.users.users_methods import UserMethods
# from src.validators.admission_validator import AdmissionValidator

load_dotenv()


class UserStart:
    def __init__(self):
        self.users = UserMethods()
        # self.validator = AdmissionValidator()

    def get_user_by_id(self, user_id: int = 1):
        with allure.step("Отправка запроса"):
            response = self.users.get_user_by_id(user_id)
            print(response)
        with allure.step("Проверка статус кода 200 GET /rest/api/admission/"):
            response.assert_status_code(200)
            # self.validator.attach_text("Статус код: 200 - Список приёмов получен")
        # with allure.step("Валидация структуры и данных"):
        #     self.validator.validate_get_all_admissions(response.response_json)
        return response