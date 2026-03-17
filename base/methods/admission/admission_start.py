import allure
from base.methods.admission.admission_methods import AdmissionMethods


class AdmissionStart:
    """Стартовые сценарии для Admission."""

    def __init__(self):
        self.admission = AdmissionMethods()

    def get_admission_by_id(self, admission_id=1, params=None):
        with allure.step("Запрос приёма по ID"):
            response = self.admission.get_admission_by_id(admission_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    # def get_admissions_by_user(self, user_id=1416, params=None):
    #     with allure.step("Запрос приёмов пользователя"):
    #         response = self.admission.get_admissions_by_user(user_id, params=params)
    #     with allure.step("Проверка статус кода 200"):
    #         response.assert_status_code(200)
    #     return response
