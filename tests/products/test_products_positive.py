import allure
import pytest
from Library.MakeyIS import Test


class TestProductsPositive:
    @pytest.mark.positive
    @allure.feature("GET /api/v2/products")
    @Test(run_test=True, group_name="Products", log=True)
    def test_get_products(self, products_start):
        products_start.get_products(clinic_id=1, page_number=1, page_size=20)

    @pytest.mark.positive
    @allure.feature("GET /api/v2/products/categories")
    @Test(run_test=True, group_name="Products", log=True)
    def test_get_products_categories(self, products_start):
        products_start.get_products_categories()

    @pytest.mark.positive
    @allure.feature("GET /api/v2/products/{product_id}")
    @Test(run_test=True, group_name="Products", log=True)
    def test_get_product_by_id(self, products_start):
        products_start.get_product_by_id(product_id=1)

    @pytest.mark.positive
    @allure.feature("GET /api/v2/products/{product_id}/stockbalances")
    @Test(run_test=True, group_name="Products", log=True)
    def test_get_product_stockbalances(self, products_start):
        products_start.get_product_stockbalances(product_id=1)

    @pytest.mark.positive
    @allure.feature("GET /api/v2/products/{product_id}/pricing/{qty}")
    @Test(run_test=True, group_name="Products", log=True)
    def test_get_product_pricing(self, products_start):
        products_start.get_product_pricing()

    @pytest.mark.positive
    @allure.feature("GET /api/v2/products/vaccines")
    @Test(run_test=True, group_name="Products", log=True)
    def test_get_products_vaccines(self, products_start):
        products_start.get_products_vaccines()

    @pytest.mark.positive
    @allure.feature("GET /api/v2/categoriesproducts")
    @Test(run_test=True, group_name="Products", log=True)
    def test_get_categories_products(self, products_start):
        products_start.get_categories_products()

    @pytest.mark.positive
    @allure.feature("GET /api/v2/products/categoriesproducts")
    @Test(run_test=True, group_name="Products", log=True)
    def test_get_products_categories_products(self, products_start):
        products_start.get_products_categories_products()

    @pytest.mark.positive
    @allure.feature("POST /api/v2/products")
    @Test(run_test=True, group_name="Products", log=True)
    def test_post_product(self, products_start, post_product_json_data):
        products_start.post_product(json_data=post_product_json_data)

    @pytest.mark.positive
    @allure.feature("PATCH /api/v2/products/{product_id}")
    @Test(run_test=True, group_name="Products", log=True)
    def test_patch_product(self, products_start):
        products_start.patch_product(product_id=1)

    @pytest.mark.positive
    @allure.feature("DELETE /api/v2/products")
    @Test(run_test=True, group_name="Products", log=True)
    def test_delete_products(self, products_start):
        products_start.delete_products()

    @pytest.mark.positive
    @allure.feature("POST /api/v2/categoriesproducts")
    @Test(run_test=True, group_name="Products", log=True)
    def test_post_categories_products(self, products_start, post_categories_products_json_data):
        products_start.post_categories_products(json_data=post_categories_products_json_data)

    @pytest.mark.positive
    @allure.feature("PATCH /api/v2/categoriesproducts/{category_id}")
    @Test(run_test=True, group_name="Products", log=True)
    def test_patch_categories_products(self, products_start):
        products_start.patch_categories_products(category_id=1)

    @pytest.mark.positive
    @allure.feature("DELETE /api/v2/categoriesproducts")
    @Test(run_test=True, group_name="Products", log=True)
    def test_delete_categories_products(self, products_start):
        products_start.delete_categories_products()
