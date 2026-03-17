"""
Корневой conftest: фикстуры auth_start и common_start доступны всем тестам,
чтобы тесты в tests/auth/ и при любом способе запуска находили их.
"""
import os
import pytest
from dotenv import load_dotenv

_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(_project_root, ".env"))

from base.methods.auth.auth_start import AuthStart
from base.methods.common.common_start import CommonStart


@pytest.fixture
def auth_start():
    return AuthStart()


@pytest.fixture
def common_start():
    start = CommonStart()
    yield start
