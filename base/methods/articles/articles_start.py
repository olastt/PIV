import allure

from base.methods.articles.articles_methods import ArticlesMethods


class ArticlesStart:
    def __init__(self):
        self.articles = ArticlesMethods()

    def get_last_three_articles(self):
        with allure.step("GET /articles/lastThree"):
            response = self.articles.get_last_three_articles()
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_articles(self, page=1, size=10):
        with allure.step("GET /articles"):
            response = self.articles.get_articles(page=page, size=size)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
