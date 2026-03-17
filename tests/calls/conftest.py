import pytest

from base.methods.calls.calls_start import CallsStart


@pytest.fixture
def calls_start():
    """Фикстура для создания экземпляра CallsStart."""
    start = CallsStart()
    yield start
