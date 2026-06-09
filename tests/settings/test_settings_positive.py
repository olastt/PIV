import os

import allure
import pytest
from Library.MakeyIS import Test


class TestSettingsPositive:
    @pytest.mark.positive
    @pytest.mark.skipif(
        not os.getenv("ENABLE_REDIS_CLEAR_API_TEST"),
        reason="GET /api/v2/redis/clear is destructive; set ENABLE_REDIS_CLEAR_API_TEST=1 for manual run",
    )
    @allure.epic("Настройки")
    @allure.feature("GET /api/v2/redis/clear")
    @allure.title("Очистка Redis")
    @Test(run_test=True, group_name="Настройки", log=True)
    def test_get_redis_clear(self, common_start_for_settings):
        common_start_for_settings.get_redis_clear()
