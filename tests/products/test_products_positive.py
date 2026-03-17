# Тесты по Swagger: Products, Categories
import allure
import pytest


@allure.epic("API по Swagger")
@allure.feature("Products / Categories")
class TestProductsPositive:

    @pytest.mark.positive
    @allure.title("GET /api/v2/products — список продуктов")
    def test_get_products(self, products_start):
        products_start.get_products(clinic_id=1, page_number=1, page_size=20)

    @pytest.mark.positive
    @allure.title("GET /api/v2/products/categories — категории товаров")
    def test_get_products_categories(self, products_start):
        products_start.get_products_categories()

    @pytest.mark.positive
    @allure.title("GET /api/v2/products/{product_id} — продукт по ID")
    def test_get_product_by_id(self, products_start):
        products_start.get_product_by_id(product_id=1)
