import pytest

from base.methods.admission.admission_start import AdmissionStart


@pytest.fixture
def admission_start():
    """Фикстура для создания экземпляра AdmissionStart."""
    start = AdmissionStart()
    yield start
