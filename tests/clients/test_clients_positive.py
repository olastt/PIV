import allure
import pytest
from Library.MakeyIS import Test


class TestClientsPositive:
    @pytest.mark.positive
    @allure.epic('РљР»РёРµРЅС‚С‹')
    @allure.feature('GET /api/v2/clients/{client_id}')
    @allure.title('РџРѕР»СѓС‡РµРЅРёРµ РёРЅС„РѕСЂРјР°С†РёРё Рѕ РєР»РёРµРЅС‚Рµ')
    @Test(run_test=True, group_name="РљР»РёРµРЅС‚С‹", log=True)
    def test_get_client_by_id(self, clients_start):
        clients_start.get_client_by_id()

    @pytest.mark.positive
    @allure.epic('РљР»РёРµРЅС‚С‹')
    @allure.feature('GET /api/v2/clients/search/')
    @allure.title("РџРѕРёСЃРє РїРѕ Р±Р°Р·Рµ РєР»РёРµРЅС‚РѕРІ")
    @Test(run_test=True, group_name="РљР»РёРµРЅС‚С‹", log=True)
    def test_get_clients_search(self, clients_start):
        clients_start.get_clients_search()

    @pytest.mark.positive
    @allure.epic('РљР»РёРµРЅС‚С‹')
    @allure.feature('GET /api/v2/clients/{client_id}/pets')
    @allure.title("РџРѕР»СѓС‡РµРЅРёРµ РёРЅС„РѕСЂРјР°С†РёРё Рѕ РїРёС‚РѕРјС†Р°С… РєР»РёРµРЅС‚Р°")
    @Test(run_test=True, group_name="РљР»РёРµРЅС‚С‹", log=True)
    def test_get_client_pets(self, clients_start):
        clients_start.get_client_pets()

    @pytest.mark.positive
    @allure.epic('РљР»РёРµРЅС‚С‹')
    @allure.feature('GET /api/v2/clients/{client_id}/match')
    @allure.title('РЎРѕРїРѕСЃС‚Р°РІР»РµРЅРёРµ РєР»РёРµРЅС‚Р°')
    @Test(run_test=True, group_name="РљР»РёРµРЅС‚С‹", log=True)
    def test_clients_match(self, clients_start):
        clients_start.get_client_match()

    @pytest.mark.positive
    @allure.epic('РљР»РёРµРЅС‚С‹')
    @allure.feature('GET /api/v2/clients/{client_id}/contacts')
    @allure.title('РљРѕРЅС‚Р°РєС‚С‹ РєР»РёРµРЅС‚Р°')
    @Test(run_test=True, group_name="РљР»РёРµРЅС‚С‹", log=True)
    def test_contacts_info_by_client(self, clients_start):
        clients_start.get_client_contacts()

    @pytest.mark.positive
    @allure.epic('РљР»РёРµРЅС‚С‹')
    @allure.feature('GET /api/v2/clients/{client_id}/pets/{pet_id}')
    @allure.title('РџРёС‚РѕРјРµС† РєР»РёРµРЅС‚Р° РїРѕ ID')
    @Test(run_test=True, group_name="РљР»РёРµРЅС‚С‹", log=True)
    def test_pet_info_by_client(self, clients_start):
        clients_start.get_client_pet_by_id()

    @pytest.mark.positive
    @allure.epic('РљР»РёРµРЅС‚С‹')
    @allure.feature('PATCH /api/v2/clients/{client_id}')
    @allure.title('РћР±РЅРѕРІР»РµРЅРёРµ РєР»РёРµРЅС‚Р°')
    @Test(run_test=True, group_name="РљР»РёРµРЅС‚С‹", log=True)
    def test_patch_client(self, clients_start):
        clients_start.patch_client(client_id=1)

    @pytest.mark.positive
    @allure.feature("POST /api/v2/clients")
    @Test(run_test=True, group_name="Clients", log=True)
    def test_create_client(self, clients_start):
        clients_start.post_client()
