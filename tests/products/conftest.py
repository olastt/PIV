import pytest

from base.methods.products.products_start import ProductsStart


@pytest.fixture
def products_start():
    """Фикстура для создания экземпляра ProductsStart."""
    start = ProductsStart()
    yield start
