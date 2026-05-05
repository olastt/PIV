import os
from uuid import uuid4

import pytest

from base.methods.products.products_start import ProductsStart


@pytest.fixture
def post_product_json_data():
    """Тело POST /api/v2/products."""
    random_title = f"pytest_product_{uuid4().hex[:8]}"
    return {
        "product_data": {
            "is_service": 0,
            "title": random_title,
            "price": 100,
            "group_id": 69,
        },
        "clinic_id": int(os.getenv("CLINIC_ID", "1")),
        "user_id": int(os.getenv("USER_ID", "1")),
    }


@pytest.fixture
def post_categories_products_json_data():
    return {
        "product_data": {
            "is_service": 0,
            "title": "чаппи3",
            "price": 500,
            "group_id": 69,
        },
        "clinic_id": 1,
        "user_id": 1,
    }


@pytest.fixture
def products_start():
    """Фикстура для создания экземпляра ProductsStart."""
    start = ProductsStart()
    yield start
