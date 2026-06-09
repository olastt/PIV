import allure
import pytest
from Library.MakeyIS import Test


class TestNotificationPositive:
    @pytest.mark.positive
    @allure.epic("Уведомления")
    @allure.feature("GET /api/v2/notification/settings")
    @allure.title("Получение настроек уведомлений")
    @Test(run_test=True, group_name="Уведомления", log=True)
    def test_get_notification_settings(self, notification_start):
        notification_start.get_notification_settings()

    @pytest.mark.positive
    @allure.epic("Уведомления")
    @allure.feature("PATCH /api/v2/notification/settings")
    @allure.title("Обновление настроек уведомлений")
    @Test(run_test=True, group_name="Уведомления", log=True)
    def test_patch_notification_settings(self, notification_start):
        notification_start.patch_notification_settings()

    @pytest.mark.positive
    @allure.epic("Уведомления")
    @allure.feature("DELETE /api/v2/remove-notification/{notification_id}")
    @allure.title("Удаление уведомления")
    @Test(run_test=True, group_name="Уведомления", log=True)
    def test_delete_remove_notification(self, notification_start):
        notification_start.delete_remove_notification(notification_id=1)
