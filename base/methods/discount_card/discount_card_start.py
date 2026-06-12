import os

import allure

from base.methods.discount_card.discount_card_methods import DiscountCardMethods


class DiscountCardStart:
    def __init__(self):
        self.discount_card = DiscountCardMethods()

    def get_discount_cards(self, client_id=None):
        client_id = client_id or int(os.getenv("CLIENT_ID", "6"))
        with allure.step("GET /discountCard"):
            response = self.discount_card.get_discount_cards(client_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
