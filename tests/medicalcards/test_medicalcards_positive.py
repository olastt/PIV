import allure
import pytest
from Library.MakeyIS import Test


class TestMedicalcardsPositive:
    @pytest.mark.positive
    @allure.epic("Медкарты")
    @allure.feature("GET /api/v2/clients/medicalcards/diagnoses")
    @allure.title("Получение диагнозов для медкарт")
    @Test(run_test=True, group_name="Медкарты", log=True)
    def test_get_medicalcards_diagnoses(self, medicalcards_start):
        medicalcards_start.get_medicalcards_diagnoses()

    @pytest.mark.positive
    @allure.epic("Медкарты")
    @allure.feature("GET /api/v2/medicalcards/vaccinations/{pet_id}")
    @allure.title("Получение вакцинаций питомца")
    @Test(run_test=True, group_name="Медкарты", log=True)
    def test_get_vaccinations_by_pet(self, medicalcards_start):
        medicalcards_start.get_vaccinations_by_pet()

    @pytest.mark.positive
    @allure.epic("Медкарты")
    @allure.feature("GET /api/v2/clients/{client_id}/medicalcards")
    @allure.title("Получение медкарт клиента")
    @Test(run_test=True, group_name="Медкарты", log=True)
    def test_get_medicalcards_by_client(self, medicalcards_start):
        medicalcards_start.get_medicalcards_by_client()

    @pytest.mark.positive
    @allure.epic("Медкарты")
    @allure.feature("GET /api/v2/clients/{client_id}/medicalcards/{medicalcard_id}")
    @allure.title("Получение медкарты клиента по ID")
    @Test(run_test=True, group_name="Медкарты", log=True)
    def test_get_medicalcard_by_client(self, medicalcards_start):
        medicalcards_start.get_medicalcard_by_client()

    @pytest.mark.positive
    @allure.epic("Медкарты")
    @allure.feature("GET /api/v2/medicalcards/texttemplates")
    @allure.title("Получение текстовых шаблонов медкарт")
    @Test(run_test=True, group_name="Медкарты", log=True)
    def test_get_medicalcard_text_templates(self, medicalcards_start):
        medicalcards_start.get_medicalcard_text_templates()

    @pytest.mark.positive
    @allure.epic("Медкарты")
    @allure.feature("GET /api/v2/clients/{client_id}/medicalcards/history")
    @allure.title("Получение истории медкарт клиента")
    @Test(run_test=True, group_name="Медкарты", log=True)
    def test_get_medicalcards_history(self, medicalcards_start):
        medicalcards_start.get_medicalcards_history()

    @pytest.mark.positive
    @allure.epic("Медкарты")
    @allure.feature("POST /api/v2/medicalcards/uploadfiles")
    @allure.title("Загрузка файлов медкарты")
    @Test(run_test=True, group_name="Медкарты", log=True)
    def test_post_medicalcards_uploadfiles(self, medicalcards_start):
        medicalcards_start.post_medicalcards_uploadfiles()

    @pytest.mark.positive
    @allure.epic("Медкарты")
    @allure.feature("POST /api/v2/medicalcards/generate-llm")
    @allure.title("Генерация текста медкарты")
    @Test(run_test=True, group_name="Медкарты", log=True)
    def test_post_medicalcards_generate_llm(self, medicalcards_start):
        medicalcards_start.post_medicalcards_generate_llm()

    @pytest.mark.positive
    @allure.epic("Медкарты")
    @allure.feature("POST /api/v2/clients/{client_id}/medicalcards")
    @allure.title("Создание медкарты")
    @Test(run_test=True, group_name="Медкарты", log=True)
    def test_post_create_medicalcard(self, medicalcards_start):
        medicalcards_start.post_create_medicalcard()

    @pytest.mark.positive
    @allure.epic("Медкарты")
    @allure.feature("PATCH /api/v2/clients/{client_id}/medicalcards/{medicalcard_id}")
    @allure.title("Обновление медкарты")
    @Test(run_test=True, group_name="Медкарты", log=True)
    def test_patch_medicalcard(self, medicalcards_start):
        medicalcards_start.patch_medicalcard()

    @pytest.mark.positive
    @allure.epic("Медкарты")
    @allure.feature("POST /api/v2/medicalcards/{medicalcard_id}/vaccinations/{pet_id}")
    @allure.title("Создание вакцинации")
    @Test(run_test=True, group_name="Медкарты", log=True)
    def test_post_medicalcard_vaccination(self, medicalcards_start, post_medicalcard_vaccination_json_data):
        medicalcards_start.post_medicalcard_vaccination(
            json_data=post_medicalcard_vaccination_json_data
        )

    @pytest.mark.positive
    @allure.epic("Медкарты")
    @allure.feature("PATCH /api/v2/medicalcards/{medicalcard_id}/vaccinations/{vaccination_id}")
    @allure.title("Обновление вакцинации")
    @Test(run_test=True, group_name="Медкарты", log=True)
    def test_patch_medicalcard_vaccination(
        self,
        medicalcards_start,
        post_medicalcard_vaccination_json_data,
        patch_medicalcard_vaccination_json_data,
    ):
        medicalcards_start.patch_medicalcard_vaccination(
            create_json_data=post_medicalcard_vaccination_json_data,
            json_data=patch_medicalcard_vaccination_json_data,
        )
