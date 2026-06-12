import allure
import pytest
from Library.MakeyIS import Test


class TestEventsPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("POST /event")
    @allure.title("Запись лога посещения экрана")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_post_event(self, events_start):
        events_start.post_event()
