import pytest

from base.methods.diagnoses.diagnoses_start import DiagnosesStart


@pytest.fixture
def diagnoses_start():
    """Фикстура для создания экземпляра DiagnosesStart."""
    start = DiagnosesStart()
    yield start
