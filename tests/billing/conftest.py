import pytest

from base.methods.billing.billing_start import BillingStart


@pytest.fixture
def billing_start():
    """Фикстура для создания экземпляра BillingStart."""
    start = BillingStart()
    yield start
