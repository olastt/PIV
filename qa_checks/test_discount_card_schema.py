import pytest
from pydantic import ValidationError

from src.schemas.piv.get_discount_card import GetDiscountCardItem


CARD = {
    "id": 1, "pet_id": 0, "title": "QA", "number": 123,
    "create_date": "2026-10-13", "card_type": "discount", "is_default": True,
    "start_date": None, "end_date": None,
}


@pytest.mark.parametrize("start,end", [
    (None, None), ("2026-10-13", None), (None, "2027-10-13"),
    ("2026-10-13", "2027-10-13"),
])
def test_card_accepts_optional_date_values(start, end):
    card = GetDiscountCardItem.model_validate(dict(CARD, start_date=start, end_date=end))
    assert card.start_date == start and card.end_date == end


@pytest.mark.parametrize("field", ["start_date", "end_date"])
def test_nullable_date_field_must_still_be_present(field):
    body = dict(CARD)
    del body[field]
    with pytest.raises(ValidationError):
        GetDiscountCardItem.model_validate(body)


@pytest.mark.parametrize("mutation", [
    {"start_date": 123}, {"end_date": False},
    {"number": "123"}, {"is_default": 1},
])
def test_other_type_constraints_are_preserved(mutation):
    with pytest.raises(ValidationError):
        GetDiscountCardItem.model_validate(dict(CARD, **mutation))
