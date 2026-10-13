import allure
import pytest
from Library.MakeyIS import Test

from tests.helpers.piv_positive import assert_articles_pagination, assert_json_body


class TestArticlesPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /articles/lastThree")
    @allure.title("Просмотр последних трёх статей")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_last_three_articles(self, articles_start):
        body = assert_json_body(articles_start.get_last_three_articles())
        assert len(body["articles"]) <= 3, "Вернулось больше трёх последних статей"
        ids = [item["id"] for item in body["articles"]]
        assert len(ids) == len(set(ids)), "Повторяющиеся id последних статей"

    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /articles")
    @allure.title("Список статей с пагинацией")
    @Test(run_test=True, group_name="PIV", log=True)
    @pytest.mark.parametrize("page,size", [(1, 10), (1, 1), (2, 1)])
    def test_get_articles(self, articles_start, page, size):
        response = articles_start.get_articles(page=page, size=size)
        assert_articles_pagination(response, page, size)
