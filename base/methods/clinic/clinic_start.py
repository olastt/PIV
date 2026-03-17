import allure
from base.methods.clinic.clinic_methods import ClinicMethods


class ClinicStart:
    """Стартовые сценарии для клиник (Clinics, Properties)."""

    def __init__(self):
        self.clinic = ClinicMethods()

    def get_all_clinics(self, params=None):
        with allure.step("Запрос списка клиник"):
            response = self.clinic.get_all_clinics()
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_clinic_properties(self, params=None):
        with allure.step("Запрос настроек клиники (properties)"):
            response = self.clinic.get_clinic_properties()
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
