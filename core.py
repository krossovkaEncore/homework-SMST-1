from view import show_tasks
from utils import check_confirm


def add_task(collection):
    task = input("Введите новую задачу: ").strip()

    if task:
        collection.append(task)
        print("Задача добавлена.")
    else:
        print("Задача не может быть пустой.")


def edit_task(collection):
    if not collection:
        print("Список задач пуст.")
        return

    show_tasks(collection)