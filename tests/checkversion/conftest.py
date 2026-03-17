import pytest

from base.methods.checkversion.checkversion_start import CheckversionStart


@pytest.fixture
def checkversion_start():
    """Фикстура для создания экземпляра CheckversionStart."""
    start = CheckversionStart()
    yield start
