import allure

from base.methods.phone_prefix.phone_prefix_methods import PhonePrefixMethods


class PhonePrefixStart:
    def __init__(self):
        self.phone_prefix = PhonePrefixMethods()

    def get_phone_prefix(self):
        with allure.step("GET /getPhonePrefix"):
            response = self.phone_prefix.get_phone_prefix()
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
