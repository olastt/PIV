import pytest

from base.methods.pets.pets_start import PetsStart


@pytest.fixture
def pets_start():
    """Фикстура для создания экземпляра PetsStart."""
    start = PetsStart()
    yield start
