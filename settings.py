import os
from src.config.url import Url

from dotenv import load_dotenv

load_dotenv()

PLATFORM = os.environ.get('PLATFORM', 'test')


class BaseSettings:
    """Простой класс настроек без валидации"""

    @property
    def vm_url(self) -> str:
        """Базовый URL API. В CI можно задать VM_URL (например тестовый бэкенд без Cloudflare)."""
        return os.getenv("VM_URL", "").strip() or Url.DOMAIN_VM_TEST

    @property
    def login(self) -> str:
        return os.getenv('LOGIN', '')

    @property
    def password(self) -> str:
        return os.getenv('PASSWORD', '')

    @property
    def app_name(self) -> str:
        return os.getenv('APP_NAME', '')

    @property
    def token(self) -> str:
        return os.getenv('TOKEN', '')

    @property
    def x_rest_api_key(self) -> str:
        return os.getenv('X_REST_API_KEY', '')

    @property
    def faker_locales(self):
        """Локаль для Faker (строка или список). По умолчанию ru_RU."""
        val = os.getenv('FAKER_LOCALES', 'ru_RU')
        if isinstance(val, str) and val:
            return [v.strip() for v in val.split(',')] if ',' in val else val
        return ['ru_RU']

    @property
    def user_password(self) -> str:
        return os.getenv('USER_PASSWORD', os.getenv('PASSWORD', ''))


base_settings = BaseSettings()