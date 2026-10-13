"""Проверки значений ответа поверх существующих Pydantic-схем."""


def assert_json_body(response):
    media_type = response.response_headers.get("content-type", "").split(";", 1)[0].strip().lower()
    assert media_type == "application/json" or media_type.endswith("+json"), "Ожидался JSON Content-Type"
    assert response.response_json is not None, "Ответ должен содержать валидный JSON"
    return response.response_json


def assert_piv_success(response):
    body = assert_json_body(response)
    assert isinstance(body, dict), "Успешный ответ должен быть объектом"
    assert body.get("success") is True, "HTTP 200 должен подтверждать success=true"
    return body


def assert_nonempty_string(value, field):
    assert isinstance(value, str) and value.strip(), f"{field} должен быть непустой строкой"


def assert_collection_count(data, items_field):
    total = data["totalCount"]
    assert type(total) is int and total >= 0, "totalCount должен быть неотрицательным integer"
    assert total >= len(data[items_field]), "totalCount меньше количества возвращённых элементов"


def assert_articles_pagination(response, page, size):
    body = assert_json_body(response)
    assert body["current_page"] == page, "Вернулась другая страница"
    assert str(body["per_page"]) == str(size), "Вернулся другой размер страницы"
    assert len(body["data"]) <= size, "Количество статей превышает size"
    assert body["total"] >= len(body["data"]), "total меньше количества статей"
    assert body["last_page"] >= 1, "last_page должен быть положительным"
    ids = [item["id"] for item in body["data"]]
    assert len(ids) == len(set(ids)), "На странице есть повторяющиеся id статей"
    if body["data"]:
        assert body["from"] == (page - 1) * size + 1, "Неверная нижняя граница страницы"
        assert body["to"] == body["from"] + len(body["data"]) - 1, "Неверная верхняя граница страницы"
        assert body["to"] <= body["total"], "Граница страницы превышает total"
    else:
        assert body.get("from") is None and body["to"] is None, "У пустой страницы должны отсутствовать границы"
    if page == 1:
        assert body["prev_page_url"] is None, "У первой страницы не должно быть предыдущей"
    if page >= body["last_page"]:
        assert body["next_page_url"] is None, "После последней страницы не должно быть следующей"
    return body
