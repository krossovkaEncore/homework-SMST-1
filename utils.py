import sys
from pathlib import Path


def get_base_dir() -> Path:
    """Возвращает папку запуска программы."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent

    return Path(__file__).resolve().parent


def insure_save_file(filename="tasks.txt") -> Path:
    """Создаёт файл сохранений, если он отсутствует."""
    save_file = get_base_dir() / filename
    save_file.touch(exist_ok=True)
    return save_file

def check_confirm(message="Вы уверены? (да/нет): "):
    while True:
        answer = input(message).strip().lower()

        if answer in ("да", "д", "yes", "y"):
            return True

        if answer in ("нет", "н", "no", "n"):
            return False

        print("Введите «да» или «нет».")
