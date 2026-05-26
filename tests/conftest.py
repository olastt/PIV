import os

import pytest
from dotenv import load_dotenv

from base.methods.admission.admission_start import AdmissionStart
from base.methods.auth.auth_start import AuthStart
from base.methods.billing.billing_start import BillingStart
from base.methods.calls.calls_start import CallsStart
from base.methods.cassa.cassa_start import CassaStart
from base.methods.checkversion.checkversion_start import CheckversionStart
from base.methods.clients.clients_start import ClientsStart
from base.methods.clinic.clinic_start import ClinicStart
from base.methods.combomanuals.combomanuals_start import CombomanualsStart
from base.methods.common.common_start import CommonStart
from base.methods.diagnoses.diagnoses_start import DiagnosesStart
from base.methods.hospital.hospital_start import HospitalStart
from base.methods.invoice.invoice_start import InvoiceStart
from base.methods.medicalcards.medicalcards_start import MedicalcardsStart
from base.methods.notification.notification_start import NotificationStart
from base.methods.pets.pets_start import PetsStart
from base.methods.products.products_start import ProductsStart
from base.methods.roles.roles_start import RolesStart
from base.methods.tariff.tariff_start import TariffStart
from base.methods.users.users_start import UserStart


_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(_project_root, ".env"))


@pytest.fixture(scope="session", autouse=True)
def ensure_auth_token():
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    app_name = os.getenv("APP_NAME")
    domain = os.getenv("DOMAIN")
    clinic_id = os.getenv("CLINIC_ID")

    if not domain:
        raise AssertionError(
            "В .env отсутствует DOMAIN. Добавьте DOMAIN=<имя_домена_клиники>, "
            "иначе API будет возвращать 401 (No domain name found)."
        )

    if not clinic_id:
        raise AssertionError(
            "В .env отсутствует CLINIC_ID. Добавьте CLINIC_ID=<id_клиники>, "
            "иначе API будет возвращать 401 (No clinic id found)."
        )

    if app_name and not os.getenv("X_MOBILE_APP"):
        os.environ["X_MOBILE_APP"] = app_name

    if login and password:
        AuthStart.auth_with_login_and_password(login=login, password=password, app_name=app_name)
        return

    token = os.getenv("X_REST_API_KEY") or os.getenv("X_TOKEN") or os.getenv("TOKEN")
    if not token:
        raise AssertionError(
            "Для запуска API-тестов нужны LOGIN/PASSWORD или уже установленный "
            "X_REST_API_KEY/X_TOKEN/TOKEN."
        )


@pytest.fixture
def admission_start():
    return AdmissionStart()


@pytest.fixture
def auth_start():
    return AuthStart()


@pytest.fixture
def billing_start():
    return BillingStart()


@pytest.fixture
def calls_start():
    return CallsStart()


@pytest.fixture
def cassa_start():
    return CassaStart()


@pytest.fixture
def checkversion_start():
    return CheckversionStart()


@pytest.fixture
def clients_start():
    return ClientsStart()


@pytest.fixture
def clinic_start():
    return ClinicStart()


@pytest.fixture
def combomanuals_start():
    return CombomanualsStart()


@pytest.fixture
def common_start():
    return CommonStart()


@pytest.fixture
def common_start_for_settings():
    return CommonStart()


@pytest.fixture
def diagnoses_start():
    return DiagnosesStart()


@pytest.fixture
def hospital_start():
    return HospitalStart()


@pytest.fixture
def invoice_start():
    return InvoiceStart()


@pytest.fixture
def medicalcards_start():
    return MedicalcardsStart()


@pytest.fixture
def notification_start():
    return NotificationStart()


@pytest.fixture
def pets_start():
    return PetsStart()


@pytest.fixture
def products_start():
    return ProductsStart()


@pytest.fixture
def roles_start():
    return RolesStart()


@pytest.fixture
def tariff_start():
    return TariffStart()


@pytest.fixture
def user_start():
    return UserStart()
