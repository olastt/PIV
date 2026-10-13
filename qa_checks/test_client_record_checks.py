import pytest

from tests.helpers.client_records import (
    assert_expected_fields,
    assert_reference_records,
    collection_records,
)


@pytest.mark.parametrize("body,field,expected", [
    ({"data": {"admission": [{"admission_id": "1"}]}}, "admission", [{"admission_id": "1"}]),
    ({"data": {"vaccination": [[{"medcard_id": "1"}], [{"medcard_id": "2"}]]}}, "vaccination", [{"medcard_id": "1"}, {"medcard_id": "2"}]),
    ({"data": {"card": [{"id": 1}]}}, "card", [{"id": 1}]),
    ({"data": [{"card": [{"id": 1}]}, {"card": [{"id": 2}]}]}, "card", [{"id": 1}, {"id": 2}]),
    ({"data": []}, "card", []),
])
def test_nested_collections_keep_all_records(body, field, expected):
    assert collection_records(body, field) == expected


def test_independent_reference_allows_unchecked_fields():
    actual = [{"id": "1", "content": "Expected", "pet": {"alias": "QA", "type": "cat"}}]
    expected = [{"id": "1", "content": "Expected", "pet": {"alias": "QA"}}]
    assert_reference_records(actual, expected, ("id",))


@pytest.mark.parametrize("actual", [
    [], [{"id": "2", "content": "Expected"}],
    [{"id": 1, "content": "Expected"}],
    [{"id": "1", "content": "Wrong"}],
    [{"id": "1"}],
    [{"id": "1", "content": "Expected"}, {"id": "1", "content": "Expected"}],
])
def test_missing_wrong_or_duplicate_record_is_rejected(actual):
    with pytest.raises(AssertionError):
        assert_reference_records(actual, [{"id": "1", "content": "Expected"}], ("id",))


def test_complete_reference_rejects_additional_records():
    actual = [{"id": "1", "content": "Expected"}, {"id": "2", "content": "Unexpected"}]
    expected = [{"id": "1", "content": "Expected"}]
    assert_reference_records(actual, expected, ("id",), complete=False)
    with pytest.raises(AssertionError):
        assert_reference_records(actual, expected, ("id",), complete=True)


def test_duplicate_references_do_not_fake_coverage():
    expected = [{"id": "1", "content": "Expected"}] * 2
    with pytest.raises(AssertionError):
        assert_reference_records(expected[:1], expected, ("id",))


def test_vaccination_identity_distinguishes_same_medcard():
    actual = [{"medcard_id": "1", "vaccine_id": "2", "vaccination_date": "2026-10-01", "name": "QA"},
              {"medcard_id": "1", "vaccine_id": "3", "vaccination_date": "2026-10-01", "name": "Other"}]
    assert_reference_records(actual, [actual[0]], ("medcard_id", "vaccine_id", "vaccination_date"))


@pytest.mark.parametrize("actual,expected", [
    ({"pet": {"alias": "Other"}}, {"pet": {"alias": "QA"}}),
    ({"is_default": 1}, {"is_default": True}),
    ({"media": [{"type": "image"}]}, {"media": []}),
    ({"media": [{"type": "image"}]}, {"media": [{"type": "video"}]}),
])
def test_wrong_nested_values_and_types_are_rejected(actual, expected):
    with pytest.raises(AssertionError):
        assert_expected_fields(actual, expected)
