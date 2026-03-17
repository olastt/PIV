import os
import pytest
from dotenv import load_dotenv

# Сразу подгружаем .env из корня проекта (mobile-), чтобы LOGIN/PASSWORD/APP_NAME были доступны
_project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(_project_root, ".env"))

from base.methods.users.users_start import UserStart
from base.methods.common.common_start import CommonStart
from base.methods.clients.clients_start import ClientsStart
from base.methods.pets.pets_start import PetsStart
from base.methods.products.products_start import ProductsStart
from base.methods.auth.auth_start import AuthStart
from base.methods.clinic.clinic_start import ClinicStart


@pytest.fixture
def auth_start():
    return AuthStart()


@pytest.fixture
def user_start():
    start = UserStart()
    yield start


@pytest.fixture
def common_start():
    start = CommonStart()
    yield start


@pytest.fixture
def clinic_start():
    start = ClinicStart()
    yield start


@pytest.fixture
def clients_start():
    start = ClientsStart()
    yield start


@pytest.fixture
def pets_start():
    start = PetsStart()
    yield start


@pytest.fixture
def products_start():
    start = ProductsStart()
    yield start
