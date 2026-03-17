import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class ProductsMethods(ApiClient):
    """Методы для товаров/услуг (Products, Categories по Swagger)"""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/products - Список продуктов")
    def get_products(self, params: dict):
        return self.get(Url.GET_PRODUCTS, params=params)

    @allure.step("GET /api/v2/products/categories - Категории товаров")
    def get_products_categories(self, params: dict = None):
        return self.get(Url.GET_PRODUCTS_CATEGORIES, params=params)

    @allure.step("GET /api/v2/products/{product_id} - Продукт по ID")
    def get_product_by_id(self, product_id, params: dict = None):
        endpoint = Url.GET_PRODUCT_BY_ID.replace("{product_id}", str(product_id))
        return self.get(endpoint, params=params or {})
