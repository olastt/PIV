import pytest

from base.methods.roles.roles_start import RolesStart


@pytest.fixture
def roles_start():
    """Фикстура для создания экземпляра RolesStart."""
    start = RolesStart()
    yield start
