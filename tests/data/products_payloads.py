import os
from uuid import uuid4


def default_create_product_payload() -> dict:
    return {
        "product_data": {
            "is_service": 0,
            "title": f"pytest_product_{uuid4().hex[:8]}",
            "price": 100,
            "group_id": 69,
        },
        "clinic_id": int(os.getenv("CLINIC_ID", "1")),
        "user_id": int(os.getenv("USER_ID", "1")),
    }


def default_create_product_category_payload() -> dict:
    return {
        "category_data": {
            "title": f"pytest_category_{uuid4().hex[:8]}",
            "status": "active",
        }
    }
