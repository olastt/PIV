"""
Базовый класс для всех валидаторов.
Содержит общие методы для работы с Allure и стандартизированный интерфейс.
"""
import json
from typing import Dict, Any, Optional

import allure


class BaseValidator:
    """
    Базовый класс для всех валидаторов.
    Предоставляет стандартизированные методы для работы с Allure и валидации ошибок.
    """

    @staticmethod
    def attach_text(message: str, name: str = "Сообщение"):
        """
        Прикрепляет текстовое сообщение в Allure отчет.

        :param message: Текст для прикрепления
        :param name: Название вложения в Allure
        """
        allure.attach(message, name=name, attachment_type=allure.attachment_type.TEXT)

    @staticmethod
    def attach_json(data: Dict[str, Any], name: str = "Данные"):
        """
        Прикрепляет JSON данные в Allure отчет.

        :param data: Словарь с данными для прикрепления
        :param name: Название вложения в Allure
        """
        allure.attach(
            json.dumps(data, indent=2, ensure_ascii=False),
            name=name,
            attachment_type=allure.attachment_type.JSON
        )
