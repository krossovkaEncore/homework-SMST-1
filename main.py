import core
import storage
import view


def main():
    collection = []
    
    storage.load_tasks(collection)
    
    while True:
        print("\n========== TASK MANAGER ==========")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Изменить задачу")
        print("4. Удалить задачу")
        print("5. Сохранить и выйти")
        print("==================================")

        choice = input("Выберите действие: ")

        match choice:
            case "1":
                view.show_tasks(collection)

            case "2":
                core.add_task(collection)

            case "3":
                core.edit_task(collection)

            case "4":
                core.delete_task(collection)

            case "5":
                storage.save_tasks(collection)
                print("Работа программы завершена.")
                break

            case _:
                print("Неверный пункт меню.")

if __name__ == "__main__":
    main()