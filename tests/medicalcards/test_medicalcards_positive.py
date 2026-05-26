import allure
import pytest
from Library.MakeyIS import Test


class TestMedicalcardsPositive:
    @pytest.mark.positive
    @allure.feature("GET /api/v2/clients/medicalcards/diagnoses")
    @Test(run_test=True, group_name="Medicalcards", log=True)
    def test_get_medicalcards_diagnoses(self, medicalcards_start):
        medicalcards_start.get_medicalcards_diagnoses()

    @pytest.mark.positive
    @allure.feature("GET /api/v2/medicalcards/vaccinations/{pet_id}")
    @Test(run_test=True, group_name="Medicalcards", log=True)
    def test_get_vaccinations_by_pet(self, medicalcards_start):
        medicalcards_start.get_vaccinations_by_pet()

    @pytest.mark.positive
    @allure.feature("GET /api/v2/clients/{client_id}/medicalcards")
    @Test(run_test=True, group_name="Medicalcards", log=True)
    def test_get_medicalcards_by_client(self, medicalcards_start):
        medicalcards_start.get_medicalcards_by_client()

    @pytest.mark.positive
    @allure.feature("GET /api/v2/clients/{client_id}/medicalcards/{medicalcard_id}")
    @Test(run_test=True, group_name="Medicalcards", log=True)
    def test_get_medicalcard_by_client(self, medicalcards_start):
        medicalcards_start.get_medicalcard_by_client()

    @pytest.mark.positive
    @allure.feature("GET /api/v2/medicalcards/texttemplates")
    @Test(run_test=True, group_name="Medicalcards", log=True)
    def test_get_medicalcard_text_templates(self, medicalcards_start):
        medicalcards_start.get_medicalcard_text_templates()

    @pytest.mark.positive
    @allure.feature("GET /api/v2/clients/{client_id}/medicalcards/history")
    @Test(run_test=True, group_name="Medicalcards", log=True)
    def test_get_medicalcards_history(self, medicalcards_start):
        medicalcards_start.get_medicalcards_history()

    @pytest.mark.positive
    @allure.feature("POST /api/v2/medicalcards/uploadfiles")
    @Test(run_test=True, group_name="Medicalcards", log=True)
    def test_post_medicalcards_uploadfiles(self, medicalcards_start):
        medicalcards_start.post_medicalcards_uploadfiles()

    @pytest.mark.positive
    @allure.feature("POST /api/v2/medicalcards/generate-llm")
    @Test(run_test=True, group_name="Medicalcards", log=True)
    def test_post_medicalcards_generate_llm(self, medicalcards_start):
        medicalcards_start.post_medicalcards_generate_llm()

    @pytest.mark.positive
    @allure.feature("POST /api/v2/clients/{client_id}/medicalcards")
    @Test(run_test=True, group_name="Medicalcards", log=True)
    def test_post_create_medicalcard(self, medicalcards_start):
        medicalcards_start.post_create_medicalcard()

    @pytest.mark.positive
    @allure.feature("PATCH /api/v2/clients/{client_id}/medicalcards/{medicalcard_id}")
    @Test(run_test=True, group_name="Medicalcards", log=True)
    def test_patch_medicalcard(self, medicalcards_start):
        medicalcards_start.patch_medicalcard()

    @pytest.mark.positive
    @allure.feature("POST /api/v2/medicalcards/{medicalcard_id}/vaccinations/{pet_id}")
    @Test(run_test=True, group_name="Medicalcards", log=True)
    def test_post_medicalcard_vaccination(self, medicalcards_start, post_medicalcard_vaccination_json_data):
        medicalcards_start.post_medicalcard_vaccination(
            json_data=post_medicalcard_vaccination_json_data
        )

    @pytest.mark.positive
    @allure.feature("PATCH /api/v2/medicalcards/{medicalcard_id}/vaccinations/{vaccination_id}")
    @Test(run_test=True, group_name="Medicalcards", log=True)
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
