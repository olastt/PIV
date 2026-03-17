import pytest

from base.methods.clinic.clinic_start import ClinicStart


@pytest.fixture
def clinic_start():
    """Фикстура для создания экземпляра ClinicStart."""
    start = ClinicStart()
    yield start