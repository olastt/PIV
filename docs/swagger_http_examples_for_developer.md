# Прямые запросы и ответы: расхождения со Swagger

Дата: 13 октября 2026. Выполнены отдельные HTTP-запросы через httpx. Автотесты, pytest, фикстуры и API-клиенты проекта не использовались. Ожидания сверены вручную с предоставленным swagger.yaml.

Проверено: https://petinvet.ru/api/v2. В Swagger указан https://petinvet.online/api/v2 — применимость контракта к .ru нужно подтвердить.

**Важно:** ниже ответы сокращены до относящихся к расхождению полей. Ключи, номер карты и ID медкарт заменены подписанными строковыми placeholders; типы и уровни вложенности сохранены. Числа, флаги, null, сообщения ошибок и Content-Type взяты из свежих ответов. Пропущенные поля не означают их отсутствия в API.

Для запросов с ключом используйте существующий ключ домена вместо <API_KEY>; для запроса получения ключа без code — подготовленный collection key. Значения ключей в файл не включены.

## API key выдаётся без заголовка авторизации

**Запрос:**

```http
GET /api/v2/apiKey/byClinicCode?code=<CLINIC_CODE> HTTP/1.1
Host: petinvet.ru
Accept: application/json
```

**Фактически — фрагмент ответа:**

```http
HTTP/1.1 200
Content-Type: application/json

{
  "success": true,
  "message": "Parameter found",
  "data": {
    "apiKey": "<API_KEY скрыт>"
  }
}
```

**Расхождение:** Swagger требует X-API-KEY (security: ApiKeyAuth). Фактически получен HTTP 200 и непустой ключ.

## GET: ошибка приходит массивом

**Запрос:**

```http
GET /api/v2/apiKey/byClinicCode HTTP/1.1
Host: petinvet.ru
Accept: application/json
X-API-KEY: <COLLECTION_KEY>
```

**Фактически — фрагмент ответа:**

```http
HTTP/1.1 400
Content-Type: application/json

[
  {
    "success": false,
    "message": "Missing required parameter: code",
    "data": {
      "errorCode": 400
    }
  }
]
```

**Расхождение:** Swagger описывает объект ошибки. Фактически корневое значение — массив из одного объекта.

## POST /event: ошибка приходит массивом

**Запрос:**

```http
POST /api/v2/event HTTP/1.1
Host: petinvet.ru
Accept: application/json
X-API-KEY: <API_KEY>
Content-Type: application/json

{}
```

**Фактически — фрагмент ответа:**

```http
HTTP/1.1 400
Content-Type: application/json

[
  {
    "success": false,
    "message": "Missing required parameter: device_id",
    "data": {
      "errorCode": 400
    }
  }
]
```

**Расхождение:** Swagger описывает объект ошибки 400. Фактически — массив из одного объекта.

## POST /sms/send: ошибка приходит массивом

**Запрос:**

```http
POST /api/v2/sms/send HTTP/1.1
Host: petinvet.ru
Accept: application/json
X-API-KEY: <API_KEY>
Content-Type: application/json

{}
```

**Фактически — фрагмент ответа:**

```http
HTTP/1.1 400
Content-Type: application/json

[
  {
    "success": false,
    "message": "Missing required parameter: phone",
    "data": {
      "errorCode": 400
    }
  }
]
```

**Расхождение:** Swagger описывает объект ошибки 400. Фактически — массив из одного объекта.

## Скидочные карты: контейнер и типы полей

**Запрос:**

```http
GET /api/v2/discountCard?client_id=1414 HTTP/1.1
Host: petinvet.ru
Accept: application/json
X-API-KEY: <API_KEY>
```

**Фактически — фрагмент ответа:**

```http
HTTP/1.1 200
Content-Type: application/json

{
  "success": true,
  "data": {
    "totalCount": 1,
    "card": [
      {
        "number": "<номер карты скрыт>",
        "is_default": 1,
        "start_date": null,
        "end_date": null
      }
    ]
  }
}
```

**Расхождение:** Swagger: data — массив групп, number — integer, is_default — boolean, даты — string без nullable. Фактически data — объект, number — string, is_default — 1, даты — null. Возможность карты без дат подтверждена пользователем.

## Вакцинации: вложенные массивы

**Запрос:**

```http
GET /api/v2/medicalCards/vaccinations?client_id=1414 HTTP/1.1
Host: petinvet.ru
Accept: application/json
X-API-KEY: <API_KEY>
```

**Фактически — фрагмент ответа:**

```http
HTTP/1.1 200
Content-Type: application/json

{
  "success": true,
  "data": {
    "totalCount": 2,
    "vaccination": [
      [
        {
          "medcard_id": "<ID медкарты скрыт>"
        }
      ],
      [
        {
          "medcard_id": "<ID медкарты скрыт>"
        }
      ]
    ]
  }
}
```

**Расхождение:** Swagger: vaccination — массив объектов VaccinationItem. Фактически — массив массивов объектов.

## Статьи: Content-Type, from/to и null-ссылки

**Запрос:**

```http
GET /api/v2/articles?page=1&size=10 HTTP/1.1
Host: petinvet.ru
Accept: application/json
X-API-KEY: <API_KEY>
```

**Фактически — фрагмент ответа:**

```http
HTTP/1.1 200
Content-Type: text/html; charset=UTF-8

{
  "current_page": 1,
  "from": 1,
  "to": 3,
  "links": [
    {
      "url": null,
      "label": "&laquo; Previous",
      "active": false
    },
    {
      "url": "https://petinvet.ru/api/v2/articles?page=1",
      "label": "1",
      "active": true
    },
    {
      "url": null,
      "label": "Next &raquo;",
      "active": false
    }
  ],
  "next_page_url": null,
  "prev_page_url": null,
  "total": 3
}
```

**Расхождение:** Swagger: application/json; from/to — string; URL-поля — string без nullable. Фактически Content-Type text/html, from/to — числа, отсутствующие ссылки — null. В примере самого Swagger ссылки null уже есть, но типы схемы это не разрешают.

## Статьи: пример при size=1

**Запрос:**

```http
GET /api/v2/articles?page=1&size=1 HTTP/1.1
Host: petinvet.ru
Accept: application/json
X-API-KEY: <API_KEY>
```

**Фактически — фрагмент ответа:**

```http
HTTP/1.1 200
Content-Type: text/html; charset=UTF-8

{
  "current_page": 1,
  "from": 1,
  "to": 1,
  "links": [
    {
      "url": null,
      "label": "&laquo; Previous",
      "active": false
    },
    {
      "url": "https://petinvet.ru/api/v2/articles?page=1",
      "label": "1",
      "active": true
    },
    {
      "url": "https://petinvet.ru/api/v2/articles?page=2",
      "label": "2",
      "active": false
    },
    {
      "url": "https://petinvet.ru/api/v2/articles?page=3",
      "label": "3",
      "active": false
    },
    {
      "url": "https://petinvet.ru/api/v2/articles?page=2",
      "label": "Next &raquo;",
      "active": false
    }
  ],
  "next_page_url": "https://petinvet.ru/api/v2/articles?page=2",
  "prev_page_url": null,
  "total": 3
}
```

**Расхождение:** Content-Type также text/html; from/to числовые; ссылка предыдущей страницы отсутствует (null).

## Документированный POST /getToken возвращает 404

**Запрос:**

```http
POST /api/v2/getToken HTTP/1.1
Host: petinvet.ru
Accept: application/json
X-API-KEY: <API_KEY>
Content-Type: application/json

{"login": "qa_invalid_login", "password": "qa_invalid_password", "app_name": "piv"}
```

**Фактически — фрагмент ответа:**

```http
HTTP/1.1 404
Content-Type: application/json

{
  "message": ""
}
```

**Расхождение:** Для неверных credentials Swagger описывает 401. Прямой запрос вернул 404 и {"message":""}.

## Ограничения этого прогона

Выполнено 9 отдельных запросов плюс GET для получения ключа из подготовленной авторизации. POST-запросы негативные: новая SMS не отправлялась, новое событие не записывалось. Credentials в примере /getToken намеренно вымышленные. .env не изменялся.

Это список воспроизведённых различий документации и ответов, а не автоматическое утверждение, что каждое различие — баг backend. Другие endpoints/статусы из предыдущего отчёта здесь не заявляются как повторно проверенные прямыми запросами.

Источник фактических фрагментов: test-artifacts/direct-http-examples.json. Исходный Swagger не изменён.
