def check_confirm(message="Вы уверены? (да/нет): "):
    while True:
        answer = input(message).strip().lower()

        if answer in ("да", "д", "yes", "y"):
            return True

        if answer in ("нет", "н", "no", "n"):
            return False

        print("Введите «да» или «нет».")
