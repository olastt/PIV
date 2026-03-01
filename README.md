# API Autotests Project

Проект автоматизированного тестирования API с использованием Python, pytest и Allure Reports.

## О проекте

Этот проект содержит автоматизированные тесты для REST API Mobile, включая:

- Создание, чтение, обновление и удаление сущностей
- Валидацию структур ответов
- Генерацию детальных отчетов в Allure

## Технологии

- **Python 3.8+** - основной язык программирования
- **pytest** - фреймворк для тестирования
- **Allure Report** - система отчетности
- **HTTPX** - HTTP клиент для запросов
- **Pydantic** - валидация данных
- **Curlify2** - генерация cURL команд

## Установка и настройка

### 1. Клонирование репозитория

```bash
git clone https://github.com/olastt/mobile-
cd mobile-
```

### 2. Настройка виртуального окружения

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate     # Windows
```

### 3.Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения

```bash
cp .env.example .env
```

### 5. Заполните необходимые переменные:

LOGIN=your_login
PASSWORD=your_password
APP_NAME=vm
TOKEN=your_login
X_REST_API_KEY=your_key
PLATFORM=test

Запустите автотесты:

```bash
pytest --alluredir=./allure-results
```

Для открытия отчета в Allure:

```bash
allure serve ./allure-results    
```

Все тесты с маркером positive

```bash
pytest -m positive
```

Все тесты с маркером negative

```bash
pytest -m negative
```

С генерацией Allure отчетов

```bash
pytest -m negative --alluredir=./allure-results
```
