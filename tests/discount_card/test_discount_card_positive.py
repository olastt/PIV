import allure
import pytest
from Library.MakeyIS import Test

from tests.helpers.piv_positive import assert_collection_count, assert_piv_success


class TestDiscountCardPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /discountCard")
    @allure.title("Просмотр скидочных карт клиента")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_discount_cards(self, discount_card_start):
        body = assert_piv_success(discount_card_start.get_discount_cards())
        groups = body["data"] if isinstance(body["data"], list) else [body["data"]]
        for group in groups:
            assert_collection_count(group, "card")
