import os

from dotenv import load_dotenv

from src.config.url import Url


load_dotenv()

PLATFORM = os.environ.get("PLATFORM", "test")


class BaseSettings:
    """Simple environment-backed settings for API tests."""

    @property
    def vm_url(self) -> str:
        return os.getenv("VM_URL", "").strip() or Url.DOMAIN_VM_TEST

    @property
    def login(self) -> str:
        return os.getenv("LOGIN", "")

    @property
    def password(self) -> str:
        return os.getenv("PASSWORD", "")

    @property
    def app_name(self) -> str:
        return os.getenv("APP_NAME", "")

    @property
    def token(self) -> str:
        return os.getenv("TOKEN", "")

    @property
    def x_rest_api_key(self) -> str:
        return os.getenv("X_REST_API_KEY", "")

    @property
    def faker_locales(self):
        value = os.getenv("FAKER_LOCALES", "ru_RU")
        if isinstance(value, str) and value:
            return [item.strip() for item in value.split(",")] if "," in value else value
        return ["ru_RU"]

    @property
    def user_password(self) -> str:
        return os.getenv("USER_PASSWORD", os.getenv("PASSWORD", ""))


base_settings = BaseSettings()
