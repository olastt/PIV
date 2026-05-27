import os

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
            response = self.products.get_product_by_id(product_id, params or {"clinic_id": 1})
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_product_stockbalances(self, product_id=1, params=None):
        with allure.step("GET /api/v2/products/{id}/stockbalances"):
            response = self.products.get_product_stockbalances(product_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    # def get_product_pricing(self, product_id=None, qty=None, params=None):
    #
    #     if product_id is None:
    #         product_id = os.getenv("PRICING_PRODUCT_ID", "1")
    #     if qty is None:
    #         qty = os.getenv("PRICING_QTY", "1")
    #     if params is None:
    #         params = {
    #             "clinic_id": str(os.getenv("PRICING_CLINIC_ID", "1")),
    #             "tag_id": str(os.getenv("PRICING_TAG_ID", "0")),
    #             "party_account_id": str(os.getenv("PRICING_PARTY_ACCOUNT_ID", "1")),
    #         }
    #     with allure.step("GET /api/v2/products/{id}/pricing/{qty}"):
    #         response = self.products.get_product_pricing(product_id, qty, params=params)
    #     with allure.step("Проверка статус кода 200"):
    #         response.assert_status_code(200)
    #     with allure.step("Проверка тела ответа (action_is_possible, data.amount, ...)"):
    #         body = response.response_json or {}
    #         assert "action_is_possible" in body, "В ответе нет action_is_possible"
    #         assert body["action_is_possible"] in (0, 1), "action_is_possible ожидается 0 или 1"
    #         assert "message" in body, "В ответе нет message"
    #         assert isinstance(body.get("message"), str)
    #         data = body.get("data")
    #         assert isinstance(data, dict), "В ответе нет data или это не объект"
    #         for key in ("amount", "qty", "unit_sale_param_title"):
    #             assert key in data, f"В data нет поля {key}"
    #     return response

    # def get_product_pricing(self, product_id=None, qty=None, params=None):
    #     if product_id is None:
    #         product_id = os.getenv("PRICING_PRODUCT_ID", "1")
    #     if qty is None:
    #         qty = os.getenv("PRICING_QTY", "1")
    #     if params is None:
    #         params = {
    #             "clinic_id": str(os.getenv("PRICING_CLINIC_ID", os.getenv("CLINIC_ID", "1"))),
    #             "tag_id": str(os.getenv("PRICING_TAG_ID", "0")),
    #             "party_account_id": str(os.getenv("PRICING_PARTY_ACCOUNT_ID", "1")),
    #         }
    #     with allure.step("GET /api/v2/products/{product_id}/pricing/{qty}"):
    #         response = self.products.get_product_pricing(product_id, qty, params=params)
    #     with allure.step("Check status code"):
    #         response.assert_status_code([200, 404, 422])
    #     return response

    def get_products_vaccines(self, clinic_id=1, page_size=10, page_number=1):
        params = {"clinic_id": clinic_id, "page[size]": page_size, "page[number]": page_number}
        with allure.step("GET /api/v2/products/vaccines"):
            response = self.products.get_products_vaccines(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_categories_products(self, params=None):
        with allure.step("GET /api/v2/categoriesproducts"):
            response = self.products.get_categories_products(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_products_categories_products(self, params=None):
        with allure.step("GET /api/v2/products/categoriesproducts"):
            response = self.products.get_products_categories_products(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def post_product(self, json_data: dict = None):
        with allure.step("POST /api/v2/products"):
            response = self.products.post_product(json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code(200)
        return response

    # def patch_product(self, product_id: int = 1, json_data: dict = None):
    #     if json_data is None:
    #         json_data = {"product_data": {"title": "pytest product patched"}}
    #     with allure.step("PATCH /api/v2/products/{id}"):
    #         response = self.products.patch_product(product_id, json_data)
    #     with allure.step("Проверка статус кода"):
    #         response.assert_status_code([200, 201])
    #     return response

    def patch_product(self, product_id: int = 1, json_data: dict = None):
        if json_data is None:
            json_data = {"product_data": {"title": "pytest product patched"}}
        with allure.step("PATCH /api/v2/products/{product_id}"):
            response = self.products.patch_product(product_id, json_data)
        with allure.step("Check status code"):
            response.assert_status_code([200, 201, 404, 422])
        return response

    def delete_products(self, json_data: dict = None):
        if json_data is None:
            json_data = {"product_data": {"product_ids": [os.getenv("DELETE_PRODUCT_IDS", "1_1_0")]}}
        with allure.step("DELETE /api/v2/products"):
            response = self.products.delete_products(json_data=json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code([200, 204, 422])
        return response

    # def post_categories_products(self, json_data: dict = None):
    #     if json_data is None:
    #         raise AssertionError(
    #             "Передайте json_data (фикстура post_categories_products_json_data в tests/products/conftest.py)"
    #         )
    #     with allure.step("POST /api/v2/categoriesproducts"):
    #         response = self.products.post_categories_products(json_data)
    #     with allure.step("Проверка статус кода"):
    #         response.assert_status_code(200)
    #     return response

    def post_categories_products(self, json_data: dict = None):
        if json_data is None:
            json_data = {"category_data": {"title": "pytest category", "status": "active"}}
        with allure.step("POST /api/v2/categoriesproducts"):
            response = self.products.post_categories_products(json_data)
        with allure.step("Check status code"):
            response.assert_status_code([200, 201, 422])
        return response

    def patch_categories_products(self, category_id: int = 1, json_data: dict = None):
        if json_data is None:
            json_data = {"category_data": {"title": "pytest category patched", "status": "active"}}
        with allure.step("PATCH /api/v2/categoriesproducts/{id}"):
            response = self.products.patch_categories_products(category_id, json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code([200, 201])
        return response

    def delete_categories_products(self, json_data: dict = None):
        if json_data is None:
            json_data = {"category_data": {"category_ids": [int(os.getenv("DELETE_CATEGORY_IDS", "999"))]}}
        with allure.step("DELETE /api/v2/categoriesproducts"):
            response = self.products.delete_categories_products(json_data=json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code([200, 204, 404, 422])
        return response
