# API Tests — Pet in Vet (PIV)

Автотесты REST API мобильного приложения **Pet in Vet**.

Стек: **Python**, **pytest**, **httpx**, **Pydantic**, **Allure**.

Репозиторий: [api-tests-pet-in-vet](https://gitlab.vetmanager.cloud/vetmanager/api-tests-pet-in-vet)

---

## Что покрываем

| Модуль | Эндпоинты |
|--------|-----------|
| Token | `POST` getToken (Vetmanager auth) |
| ApiKey | `GET /apiKey/byClinicCode` |
| Clients | `GET /clients/clientByPhone` |
| Phone prefix | `GET /getPhonePrefix` |
| SMS | `POST /sms/send`, `GET /sms/check` |
| Domain | `GET /domainName` |
| Admissions | `GET /admissions` |
| Medical cards | `GET /medicalCards/recomendations`, `/vaccinations` |
| Clinics | `GET /clinics` |
| Articles | `GET /articles/lastThree`, `/articles` |
| Events | `POST /event` |
| Discount card | `GET /discountCard` |

Есть **positive** (200) и **negative** (400, 401, 403, 404, 422, 500) сценарии по swagger.

---

## Как устроена авторизация

Перед тестами (session fixture в `tests/conftest.py`):

1. `POST getToken` на Vetmanager → `token`
2. `md5(token + DOMAIN_PIV)` → временный ключ коллекции
3. `GET /apiKey/byClinicCode?code=CLINIC_CODE` → `apiKey` клиники
4. `apiKey` кладётся в `X-API-KEY` для всех остальных запросов к PIV

Базовый URL API: `https://petinvet.ru/api/v2`

---

## Структура проекта

```
base/
  piv_client.py          # HTTP-клиент PIV (X-API-KEY)
  methods/               # methods + start по эндпоинтам
  request_context.py     # контекст HTTP для упавших тестов
  failure_report.py      # данные падения → Allure + JSON
src/
  config/url.py          # URL и пути
  schemas/piv/           # строгие Pydantic-схемы (200 и ошибки)
tests/
  */test_*_positive.py
  */test_*_negative.py
  helpers/               # хелперы для negative
  conftest.py            # fixtures + bootstrap сессии
scripts/
  bitrix_notify.py       # уведомление в Bitrix24 после CI
.github/workflows/
  run_tests.yml          # GitHub Actions (Allure → Surge → Bitrix)
```

---

## Установка

```bash
git clone https://gitlab.vetmanager.cloud/vetmanager/api-tests-pet-in-vet.git
cd api-tests-pet-in-vet

python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

Рекомендуется **Python 3.11** (как в CI).

---

## Переменные окружения

В корне нужен файл `.env`:

```env
LOGIN_PIV=your_login
PASSWORD_PIV=your_password
APP_NAME_PIV=piv
DOMAIN_PIV=your_clinic_domain
CLIENT_ID=6
CLIENT_PHONE=9184140259
CLINIC_CODE=10077
```

| Переменная | Назначение |
|------------|------------|
| `LOGIN_PIV` / `PASSWORD_PIV` | Учётка Vetmanager для getToken |
| `APP_NAME_PIV` | Имя приложения (`piv`) |
| `DOMAIN_PIV` | Домен клиники (для md5-ключа) |
| `CLINIC_CODE` | Код клиники для `/apiKey/byClinicCode` |
| `CLIENT_ID` | ID клиента для admissions / medicalcards / discount |
| `CLIENT_PHONE` | Телефон для `/clients/clientByPhone` (без ведущей `7`) |
| `SMS_CODE` | Опционально — код из SMS для `/sms/check` |

`API_TOKEN_COLLECTION` и `X_API_KEY` выставляются автоматически при bootstrap и **не нужно** задавать руками.

---

## Запуск тестов

Все тесты:

```bash
pytest
```

Только positive / negative:

```bash
pytest -m positive
pytest -m negative
```

Конкретный модуль:

```bash
pytest tests/clients/
pytest tests/medicalcards/test_medicalcards_negative.py
```

С Allure (по умолчанию уже пишется в `allure-results` через `pytest.ini`):

```bash
pytest
allure serve allure-results
```

---

## Отчёты при падении

Если тест падает:

- в **Allure** попадают cURL, тело ответа и сводка «Данные упавшего теста»
- локально пишется `test-artifacts/failures.json`
- в **CI** эти данные уходят в Bitrix вместе со ссылкой на Allure (Surge)

---

## CI

Workflow: `.github/workflows/run_tests.yml`

- push в `main` / `master`, ручной запуск, по будням по расписанию
- прогон pytest → Allure → Surge → уведомление Bitrix (`scripts/bitrix_notify.py`)

Нужные secrets: `SURGE_DOMAIN`, `SURGE_TOKEN`, `BITRIX_WEBHOOK_URL`, `BITRIX_CHAT_ID`.  
`.env` должен быть в корне репозитория (как сейчас принято в проекте).

---

## Полезные команды

```bash
# Список тестов
pytest --collect-only -q

# Тихий прогон как в CI
pytest --tb=no -q

# Только один тест
pytest tests/apikey/test_apikey_positive.py::TestApikeyPositive::test_get_api_key_by_clinic_code
```
