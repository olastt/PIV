import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class ProductsMethods(ApiClient):
    """Методы для товаров/услуг (Products, Categories по Swagger / Postman)."""

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

    @allure.step("GET /api/v2/products/{product_id}/stockbalances - Остатки")
    def get_product_stockbalances(self, product_id, params: dict = None):
        endpoint = Url.GET_PRODUCT_STOCKBALANCES.replace("{product_id}", str(product_id))
        return self.get(endpoint, params=params)

    @allure.step("GET /api/v2/products/{product_id}/pricing/{qty} - Расчёт цены")
    def get_product_pricing(self, product_id, qty, params: dict = None):
        endpoint = (
            Url.GET_PRODUCT_PRICING.replace("{product_id}", str(product_id)).replace("{qty}", str(qty))
        )
        return self.get(endpoint, params=params or {})

    @allure.step("GET /api/v2/products/vaccines - Вакцины")
    def get_products_vaccines(self, params: dict = None):
        return self.get(Url.GET_PRODUCTS_VACCINES, params=params)

    @allure.step("GET /api/v2/categoriesproducts")
    def get_categories_products(self, params: dict = None):
        return self.get(Url.GET_CATEGORIES_PRODUCTS, params=params)

    @allure.step("GET /api/v2/products/categoriesproducts")
    def get_products_categories_products(self, params: dict = None):
        return self.get(Url.GET_PRODUCTS_CATEGORIES_PRODUCTS, params=params)

    @allure.step("POST /api/v2/products - Создание товара/услуги")
    def post_product(self, json_data: dict):
        return self.post(Url.POST_PRODUCTS, json_data=json_data)

    @allure.step("PATCH /api/v2/products/{product_id} - Обновление товара")
    def patch_product(self, product_id, json_data: dict):
        endpoint = Url.PATCH_PRODUCT.replace("{product_id}", str(product_id))
        return self.patch(endpoint, json_data=json_data)

    @allure.step("DELETE /api/v2/products - Удаление товаров")
    def delete_products(self, json_data: dict = None):
        return self.delete(Url.DELETE_PRODUCTS, json_data=json_data)

    @allure.step("DELETE /api/v2/categoriesproducts")
    def delete_categories_products(self, json_data: dict = None):
        return self.delete(Url.DELETE_CATEGORIES_PRODUCTS, json_data=json_data)

    @allure.step("POST /api/v2/categoriesproducts")
    def post_categories_products(self, json_data: dict):
        return self.post(Url.POST_CATEGORIES_PRODUCTS, json_data=json_data)

    @allure.step("PATCH /api/v2/categoriesproducts/{category_id}")
    def patch_categories_products(self, category_id: int, json_data: dict):
        endpoint = Url.PATCH_CATEGORIES_PRODUCTS.replace("{category_id}", str(category_id))
        return self.patch(endpoint, json_data=json_data)
