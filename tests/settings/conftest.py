import pytest

from base.methods.common.common_start import CommonStart


@pytest.fixture
def common_start_for_settings():
    start = CommonStart()
    yield start
