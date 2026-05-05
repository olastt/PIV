import os

import allure
import pytest


# @allure.epic("API по Postman (Settings)")
# @allure.feature("Служебные настройки")
# class TestSettingsPositive:

    # @pytest.mark.positive
    # @pytest.mark.skipif(
    #     not os.getenv("ENABLE_REDIS_CLEAR_TEST"),
    #     reason="GET /api/v2/redis/clear — включите ENABLE_REDIS_CLEAR_TEST=1 для явного прогона",
    # )
    # @allure.title("GET /api/v2/redis/clear — очистка Redis")
    # def test_get_redis_clear(self, common_start_for_settings):
    #     common_start_for_settings.get_redis_clear()
