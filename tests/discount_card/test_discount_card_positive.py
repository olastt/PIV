import allure
import pytest
from Library.MakeyIS import Test


class TestDiscountCardPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /discountCard")
    @allure.title("Просмотр скидочных карт клиента")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_discount_cards(self, discount_card_start):
        discount_card_start.get_discount_cards()
