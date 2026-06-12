import allure

from base.piv_client import PivApiClient
from src.config.url import Url


class DiscountCardMethods(PivApiClient):
    @allure.step("GET /discountCard — скидочные карты клиента")
    def get_discount_cards(self, client_id: int):
        return self.get(Url.GET_DISCOUNT_CARDS, params={"client_id": client_id})
