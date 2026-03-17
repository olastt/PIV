import pytest

from base.methods.combomanuals.combomanuals_start import CombomanualsStart


@pytest.fixture
def combomanuals_start():
    """Фикстура для создания экземпляра CombomanualsStart."""
    start = CombomanualsStart()
    yield start
