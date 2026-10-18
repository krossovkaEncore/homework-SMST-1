from pathlib import Path

TASKS_FILE = Path(__file__).with_name("tasks.txt")


def load_tasks(collection):
    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            collection.clear()

            for line in file:
                task = line.strip()

                if task:
                    collection.append(task)

        print("Задачи загружены из файла.")

    except FileNotFoundError:
        print("Файл с задачами не найден. Будет создан новый.")


def save_tasks(collection):
    try:
        with TASKS_FILE.open("w", encoding="utf-8") as file:
            for task in collection:
                file.write(task + "\n")

        print("Задачи сохранены в файл.")

    except OSError as error:
        print(f"Ошибка сохранения задач: {error}")
