import allure

from base.piv_client import PivApiClient
from src.config.url import Url


class EventsMethods(PivApiClient):
    @allure.step("POST /event — лог посещения экрана")
    def post_event(self, json_data: dict = None, params: dict = None):
        return self.post(Url.POST_EVENT, json_data=json_data, params=params)
