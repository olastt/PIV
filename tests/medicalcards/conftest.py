import pytest

from base.methods.medicalcards.medicalcards_start import MedicalcardsStart


@pytest.fixture
def medicalcards_start():
    """Фикстура для создания экземпляра MedicalcardsStart."""
    start = MedicalcardsStart()
    yield start
