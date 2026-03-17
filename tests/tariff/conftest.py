import pytest

from base.methods.tariff.tariff_start import TariffStart


@pytest.fixture
def tariff_start():
    """Фикстура для создания экземпляра TariffStart."""
    start = TariffStart()
    yield start
