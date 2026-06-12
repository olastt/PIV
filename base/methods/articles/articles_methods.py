import allure

from base.piv_client import PivApiClient
from src.config.url import Url


class ArticlesMethods(PivApiClient):
    @allure.step("GET /articles/lastThree — последние три статьи")
    def get_last_three_articles(self):
        return self.get(Url.GET_LAST_THREE_ARTICLES)

    @allure.step("GET /articles — список статей с пагинацией")
    def get_articles(self, page: int = 1, size: int = 10):
        return self.get(Url.GET_ARTICLES, params={"page": page, "size": size})
