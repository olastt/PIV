import allure

from base.piv_client import PivApiClient
from src.config.url import Url


class DomainNameMethods(PivApiClient):
    @allure.step("GET /domainName — доменное имя клиники")
    def get_domain_name(self):
        return self.get(Url.GET_DOMAIN_NAME)
