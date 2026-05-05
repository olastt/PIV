import pytest

from base.methods.notification.notification_start import NotificationStart


@pytest.fixture
def notification_start():
    start = NotificationStart()
    yield start
