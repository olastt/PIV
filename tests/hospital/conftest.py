import pytest

from base.methods.hospital.hospital_start import HospitalStart


@pytest.fixture
def hospital_start():
    """Фикстура для создания экземпляра HospitalStart."""
    start = HospitalStart()
    yield start
