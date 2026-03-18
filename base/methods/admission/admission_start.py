import allure
from base.methods.admission.admission_methods import AdmissionMethods


class AdmissionStart:

    def __init__(self):
        self.admission = AdmissionMethods()

    def get_admission_by_id(self, admission_id=1, params=None):
        with allure.step("Запрос приёма по ID"):
            response = self.admission.get_admission_by_id(admission_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_admissions_by_user(self, user_id=1, clinic_id=1,
                               page_number=1, page_size=20,
                               filter_status="save"):
        params = {
            "clinic_id": clinic_id,
            "page[number]": page_number,
            "page[size]": page_size,
            "filter[status]": filter_status,
            ###save,accepted,delayed,deleted,directed,in_treatment,not_approved,not_confirmed
        }
        with allure.step("Запрос приёмов пользователя"):
            response = self.admission.get_admissions_by_user(user_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    # def create_admission(self, user_id=1, json_data=None):
    #     json_data = {
    #         "admission_data": {
    #             "admission_type_id": 4,
    #             "admission_date": "2026-03-21 14:50:00",
    #             "user_id": 1,
    #             "clinic_id": 1,
    #             "client_id": 21,
    #             "pet_id": 10,
    #             "status": "save",
    #             "description": "заметка для приема создание из постман",
    #             "admission_length": "00:15:00",
    #         }
    #     }
    #     with allure.step("Создание приёма"):
    #         response = self.admission.create_admission(user_id, json_data=json_data)
    #     with allure.step("Проверка статус кода 200"):
    #         response.assert_status_code(200)
    #     return response
