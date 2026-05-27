import allure
import pytest
from Library.MakeyIS import Test


class TestNotificationPositive:
    # @pytest.mark.positive
    # @allure.feature("POST /api/v2/notification/device")
    # @Test(run_test=True, group_name="Notification", log=True)
    # def test_post_notification_device(self, notification_start):
    #     notification_start.post_notification_device()

    @pytest.mark.positive
    @allure.feature("GET /api/v2/notification/settings")
    @Test(run_test=True, group_name="Notification", log=True)
    def test_get_notification_settings(self, notification_start):
        notification_start.get_notification_settings()

    @pytest.mark.positive
    @allure.feature("PATCH /api/v2/notification/settings")
    @Test(run_test=True, group_name="Notification", log=True)
    def test_patch_notification_settings(self, notification_start):
        notification_start.patch_notification_settings()

    # @pytest.mark.positive
    # @allure.feature("POST /api/v2/vetmanager-hook")
    # @Test(run_test=True, group_name="Notification", log=True)
    # def test_post_vetmanager_hook(self, notification_start):
    #     notification_start.post_vetmanager_hook()

    @pytest.mark.positive
    @allure.feature("DELETE /api/v2/remove-notification/{notification_id}")
    @Test(run_test=True, group_name="Notification", log=True)
    def test_delete_remove_notification(self, notification_start):
        notification_start.delete_remove_notification(notification_id=1)
