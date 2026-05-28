import pytest
from tests.data.products_payloads import (
    default_create_product_category_payload,
    default_create_product_payload,
)

@pytest.fixture
def post_product_json_data():
    return default_create_product_payload()


@pytest.fixture
def post_categories_products_json_data():
    return default_create_product_category_payload()
