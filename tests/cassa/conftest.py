import pytest

from base.methods.cassa.cassa_start import CassaStart


@pytest.fixture
def cassa_start():
    """Фикстура для создания экземпляра CassaStart."""
    start = CassaStart()
    yield start
