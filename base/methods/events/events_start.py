import allure

from base.methods.events.events_methods import EventsMethods


class EventsStart:
    def __init__(self):
        self.events = EventsMethods()

    def post_event(self, device_id=1, title="Визиты", json_data=None, params=None):
        if params is None:
            params = {"device_id": device_id, "title": title}
        if json_data is None:
            json_data = {"device_id": device_id, "title": title}
        with allure.step("POST /event"):
            response = self.events.post_event(json_data=json_data, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
