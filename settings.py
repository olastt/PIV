import os
from src.config.url import Url

from dotenv import load_dotenv

load_dotenv()

PLATFORM = os.environ.get('PLATFORM', 'test')


class BaseSettings:
    """Простой класс настроек без валидации"""

    @property
    def vm_url(self) -> str:
        return f'{Url.DOMAIN_VM_PROD}'

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


base_settings = BaseSettings()