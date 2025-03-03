import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def operations_json_get_info(directory):
    """Функция получения содержимого из .json файла"""
    try:
        with open(directory, encoding="utf-8") as f:
            logger.info(f"Успешно открыт файл, расположенный по пути: {directory}")
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Ошибка: FileNotFoundError, пусть к файлу: {directory}")
        return "файл не найден"
    except json.JSONDecodeError:
        logger.error(f"Ошибка: json.JSONDecodeError, пусть к файлу: {directory}")
        return []
