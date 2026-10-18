def show_tasks(collection):
    if not collection:
        print("\nСписок задач пуст.")
        return

    print("\n========== СПИСОК ЗАДАЧ ==========")

    for number, task in enumerate(collection, 1):
        print(f"{number}. {task}")

    print("==================================")


def show_menu():
    print("\n========== TASK MANAGER ==========")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Изменить задачу")
    print("4. Удалить задачу")
    print("5. Сохранить и выйти")
    print("==================================")


def show_message(message):
    print(message)
