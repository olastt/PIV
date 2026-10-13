"""Сверка коллекций клиента с независимыми эталонами из ВМ."""


def collection_records(body, items_field):
    data = body["data"]
    if items_field == "card" and isinstance(data, list):
        return [record for group in data for record in group["card"]]
    records = data[items_field]
    if items_field == "vaccination":
        return [record for group in records for record in group]
    return records


def assert_expected_fields(actual, expected, path="record"):
    if isinstance(expected, dict):
        assert isinstance(actual, dict), f"{path}: ожидался объект"
        for field, value in expected.items():
            assert field in actual, f"{path}.{field}: отсутствует поле"
            assert_expected_fields(actual[field], value, f"{path}.{field}")
    elif isinstance(expected, list):
        assert isinstance(actual, list) and len(actual) == len(expected), f"{path}: неверный состав списка"
        for index, value in enumerate(expected):
            assert_expected_fields(actual[index], value, f"{path}[{index}]")
    else:
        assert type(actual) is type(expected) and actual == expected, f"{path}: значение не совпадает с эталоном ВМ"


def assert_reference_records(actual, expected, identity_fields, complete=False):
    assert expected, "Нужны независимые эталонные записи из ВМ"
    identities = set()
    for reference in expected:
        assert isinstance(reference, dict), "Эталонная запись должна быть объектом"
        assert all(field in reference for field in identity_fields), "В эталоне отсутствует идентификатор записи"
        assert all(type(reference[field]) in (str, int) for field in identity_fields), "Идентификаторы эталона должны быть string или integer"
        identity = tuple((type(reference[field]), reference[field]) for field in identity_fields)
        assert identity not in identities, "В эталоне повторяется идентификатор записи"
        identities.add(identity)
        matches = [record for record in actual if all(
            type(record.get(field)) is type(reference[field]) and record.get(field) == reference[field]
            for field in identity_fields
        )]
        assert len(matches) == 1, "Эталонная запись отсутствует или повторяется в ответе"
        assert_expected_fields(matches[0], reference)
    if complete:
        assert len(actual) == len(expected), "Ответ содержит записи сверх полного эталона ВМ"
