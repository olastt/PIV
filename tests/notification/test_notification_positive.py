import allure
import pytest


@allure.epic("API по Swagger / Postman")
@allure.feature("Notification")
class TestNotificationPositive:

    # @pytest.mark.positive
    # @allure.title("POST /api/v2/notification/device — регистрация устройства")
    # def test_post_notification_device(self, notification_start):
    #     notification_start.post_notification_device()

    @pytest.mark.positive
    @allure.title("GET /api/v2/notification/settings — настройки уведомлений")
    def test_get_notification_settings(self, notification_start):
        notification_start.get_notification_settings()
    #
    # @pytest.mark.positive
    # @allure.title("PATCH /api/v2/notification/settings — обновление настроек")
    # def test_patch_notification_settings(self, notification_start):
    #     notification_start.patch_notification_settings()

    # @pytest.mark.positive
    # @allure.title("POST /api/v2/vetmanager-hook — webhook Vetmanager")
    # def test_post_vetmanager_hook(self, notification_start):
    #     notification_start.post_vetmanager_hook()
    #
    # @pytest.mark.positive
    # @allure.title("DELETE /api/v2/remove-notification/{id}")
    # def test_delete_remove_notification(self, notification_start):
    #     notification_start.delete_remove_notification()
