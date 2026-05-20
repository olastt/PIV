from uuid import uuid4

import pytest

from base.methods.calls.calls_start import CallsStart, resolve_call_id_after_create


@pytest.fixture
def calls_start():
    """Фикстура для создания экземпляра CallsStart."""
    return CallsStart()


@pytest.fixture
def call_for_update(calls_start, user_id=1):
    """Создаёт прозвон для теста update; id передаётся в update_user_call через calls_start."""
    note = f"pytest_call_{uuid4().hex[:8]}"
    json_data = {
        "call_data": {
            "date": "2026-03-13 14:00:00",
            "status": "save",
            "pet_id": 4,
            "note": note,
            "clinic_id": 1,
        }
    }
    response = calls_start.create_user_call(user_id=user_id, json_data=json_data)
    call_id = resolve_call_id_after_create(calls_start, user_id, response, note=note)
    assert call_id is not None, (
        f"Не удалось получить call_id после создания (note={note!r}): "
        f"create={getattr(response, 'response_json', None)}"
    )
    calls_start.update_call_user_id = user_id
    calls_start.update_call_id = call_id
