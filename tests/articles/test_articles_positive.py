import allure
import pytest
from Library.MakeyIS import Test


class TestArticlesPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /articles/lastThree")
    @allure.title("Просмотр последних трёх статей")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_last_three_articles(self, articles_start):
        articles_start.get_last_three_articles()

    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /articles")
    @allure.title("Список статей с пагинацией")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_articles(self, articles_start):
        articles_start.get_articles()
