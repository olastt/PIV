import os
from uuid import uuid4

import pytest

@pytest.fixture
def post_product_json_data():
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
        "category_data": {
            "title": f"pytest_category_{uuid4().hex[:8]}",
            "status": "active",
        }
    }
