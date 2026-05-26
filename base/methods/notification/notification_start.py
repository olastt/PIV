import os

import allure
from base.methods.notification.notification_methods import NotificationMethods


class NotificationStart:
    def __init__(self):
        self.notification = NotificationMethods()

    # def post_notification_device(self, json_data: dict = None):
    #     domain = os.getenv("DOMAIN", "test")
    #     if json_data is None:
    #         json_data = {
    #             "device_data": {
    #                 "user_id": int(os.getenv("USER_ID", "1")),
    #                 "device_id": "pytest-device-id",
    #                 "device_token": None,
    #                 "platform": "android",
    #                 "clinic_id": int(os.getenv("CLINIC_ID", "1")),
    #                 "domain_name": domain,
    #             }
    #         }
    #     with allure.step("POST /api/v2/notification/device"):
    #         response = self.notification.post_notification_device(json_data)
    #     with allure.step("Check status code"):
    #         response.assert_status_code([200, 201, 422])
    #     return response

    def get_notification_settings(self, clinic_id: int = None, user_id: int = None):
        clinic_id = clinic_id or int(os.getenv("CLINIC_ID", "1"))
        user_id = user_id or int(os.getenv("USER_ID", "1"))
        params = {"clinic_id": clinic_id, "user_id": user_id}
        with allure.step("GET /api/v2/notification/settings"):
            response = self.notification.get_notification_settings(params=params)
        with allure.step("Check status code 200"):
            response.assert_status_code(200)
        return response

    def post_vetmanager_hook(self, json_data: dict = None):
        if json_data is None:
            json_data = {"list_notifications": "[]"}
        with allure.step("POST /api/v2/vetmanager-hook"):
            response = self.notification.post_vetmanager_hook(json_data)
        with allure.step("Check status code"):
            response.assert_status_code([200, 201, 204, 422])
        return response

    def delete_remove_notification(self, notification_id: int = 1):
        clinic_id = int(os.getenv("CLINIC_ID", "1"))
        user_id = int(os.getenv("USER_ID", "1"))
        domain = os.getenv("DOMAIN", "")
        params = {"user_id": user_id, "clinic_id": clinic_id, "domain_name": domain}
        with allure.step("DELETE /api/v2/remove-notification/{notification_id}"):
            response = self.notification.delete_remove_notification(notification_id, params=params)
        with allure.step("Check status code"):
            response.assert_status_code([200, 204, 404, 422])
        return response

    def patch_notification_settings(self, json_data: dict = None):
        if json_data is None:
            json_data = {
                "clinic_id": int(os.getenv("CLINIC_ID", "1")),
                "user_id": int(os.getenv("USER_ID", "1")),
                "notification_settings_data": {
                    "change_doctor_schedule": 0,
                    "new_pending_admissins": 1,
                    "reminder_of_calling": 1,
                    "register_new_client": 1,
                    "end_of_tariff_plan": 1,
                    "create_admissin": 0,
                    "admissin_change": 0,
                    "confirmation_admission": 0,
                },
            }
        with allure.step("PATCH /api/v2/notification/settings"):
            response = self.notification.patch_notification_settings(json_data)
        with allure.step("Check status code"):
            response.assert_status_code([200, 422])
        return response
