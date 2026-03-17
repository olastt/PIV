import allure
from base.methods.products.products_methods import ProductsMethods


class ProductsStart:
    """Стартовые сценарии для товаров/услуг (Products, Categories)."""

    def __init__(self):
        self.products = ProductsMethods()

    def get_products(self, clinic_id=1, page_number=1, page_size=20):
        params = {"clinic_id": clinic_id, "page[number]": page_number, "page[size]": page_size}
        with allure.step("Запрос списка продуктов"):
            response = self.products.get_products(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_products_categories(self, params=None):
        with allure.step("Запрос категорий товаров"):
            response = self.products.get_products_categories(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_product_by_id(self, product_id=1, params=None):
        with allure.step("Запрос продукта по ID"):
            response = self.products.get_product_by_id(product_id, params or {})
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
