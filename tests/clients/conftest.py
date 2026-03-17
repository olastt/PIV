import pytest

from base.methods.clients.clients_start import ClientsStart


@pytest.fixture
def clients_start():
    """Фикстура для создания экземпляра ClientsStart."""
    start = ClientsStart()
    yield start
