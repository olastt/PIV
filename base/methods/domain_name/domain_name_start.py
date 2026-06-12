import allure

from base.methods.domain_name.domain_name_methods import DomainNameMethods


class DomainNameStart:
    def __init__(self):
        self.domain_name = DomainNameMethods()

    def get_domain_name(self):
        with allure.step("GET /domainName"):
            response = self.domain_name.get_domain_name()
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
