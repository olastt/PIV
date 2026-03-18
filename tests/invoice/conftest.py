import pytest
from base.methods.invoice.invoice_start import InvoiceStart


@pytest.fixture
def invoice_start():
    start = InvoiceStart()
    yield start