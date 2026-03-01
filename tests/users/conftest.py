import pytest
from base.methods.users.users_start import UserStart


@pytest.fixture
def user_start():
    start = UserStart()
    yield start
