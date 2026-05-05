import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class NotificationMethods(ApiClient):
    """Уведомления и webhooks (Postman: Notification)."""

    def __init__(self):
        super().__init__()

    @allure.step("POST /api/v2/notification/device")
    def post_notification_device(self, json_data: dict):
        return self.post(Url.POST_NOTIFICATION_DEVICE, json_data=json_data)

    @allure.step("GET /api/v2/notification/settings")
    def get_notification_settings(self, params: dict = None):
        return self.get(Url.GET_NOTIFICATION_SETTINGS, params=params)

    @allure.step("POST /api/v2/vetmanager-hook")
    def post_vetmanager_hook(self, json_data: dict = None):
        return self.post(Url.POST_VETMANAGER_HOOK, json_data=json_data or {})

    @allure.step("DELETE /api/v2/remove-notification/{notification_id}")
    def delete_remove_notification(self, notification_id: int, params: dict = None):
        endpoint = Url.DELETE_REMOVE_NOTIFICATION.replace("{notification_id}", str(notification_id))
        return self.delete(endpoint, params=params)

    @allure.step("PATCH /api/v2/notification/settings")
    def patch_notification_settings(self, json_data: dict):
        return self.patch(Url.PATCH_NOTIFICATION_SETTINGS, json_data=json_data)
