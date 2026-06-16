import os

from dotenv import load_dotenv

_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(_project_root, ".env"))

import pytest

from base.failure_report import init_failures_file, report_test_failure
from base.methods.apikey.apikey_start import ApikeyStart
from base.methods.articles.articles_start import ArticlesStart
from base.methods.clients.clients_start import ClientsStart
from base.methods.clinic.clinic_start import ClinicStart
from base.methods.discount_card.discount_card_start import DiscountCardStart
from base.methods.domain_name.domain_name_start import DomainNameStart
from base.methods.events.events_start import EventsStart
from base.methods.medicalcards.medicalcards_start import MedicalcardsStart
from base.methods.phone_prefix.phone_prefix_start import PhonePrefixStart
from base.methods.piv_admissions.piv_admissions_start import PivAdmissionsStart
from base.methods.sms.sms_start import SmsStart
from base.methods.token.token_start import TokenStart
from base.request_context import begin_test


@pytest.fixture(scope="session", autouse=True)
def init_failure_artifacts():
    init_failures_file()


@pytest.fixture(autouse=True)
def reset_http_context():
    begin_test()
    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        report_test_failure(item.nodeid, str(report.longrepr))


@pytest.fixture(scope="session", autouse=True)
def ensure_piv_api_key():
    """
    Перед тестами:
    1. getToken → md5(token + domain) — collection key
    2. GET /apiKey/byClinicCode — clinic apiKey
    3. clinic apiKey → X-API-KEY для всех остальных PIV-запросов
    """
    TokenStart().bootstrap_piv_session()


@pytest.fixture
def token_start():
    return TokenStart()


@pytest.fixture
def apikey_start():
    return ApikeyStart()


@pytest.fixture
def clients_start():
    return ClientsStart()


@pytest.fixture
def phone_prefix_start():
    return PhonePrefixStart()


@pytest.fixture
def sms_start():
    return SmsStart()


@pytest.fixture
def domain_name_start():
    return DomainNameStart()


@pytest.fixture
def piv_admissions_start():
    return PivAdmissionsStart()


@pytest.fixture
def medicalcards_start():
    return MedicalcardsStart()


@pytest.fixture
def clinic_start():
    return ClinicStart()


@pytest.fixture
def articles_start():
    return ArticlesStart()


@pytest.fixture
def events_start():
    return EventsStart()


@pytest.fixture
def discount_card_start():
    return DiscountCardStart()
