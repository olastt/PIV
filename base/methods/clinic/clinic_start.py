import allure

from base.methods.clinic.clinic_methods import ClinicsMethods


class ClinicStart:
    def __init__(self):
        self.clinic = ClinicsMethods()

    def get_clinics(self):
        with allure.step("GET /clinics"):
            response = self.clinic.get_clinics()
            print(response)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
