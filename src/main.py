from services.task_manager import TaskManager

def main():
    """Основная функция программы."""
    # Инициализация менеджера задач
    manager = TaskManager()

    # Создание сотрудников
    повар = manager.add_employee("Иван Петров", "Повар")
    официант = manager.add_employee("Мария Сидорова", "Официант")

    # Создание и назначение задач
    приготовление = manager.create_task(
        "Приготовить специальное блюдо",
        "Приготовить пасту карбонара для стола №3"
    )
    повар.assign_task(приготовление)

    обслуживание = manager.create_task(
        "Обслужить стол №5",
        "Принять заказ и обслужить гостей за столом №5"
    )
    официант.assign_task(обслуживание)

    # Вывод информации
    print("Задачи повара:")
    for task in повар.tasks:
        print(f"- {task}")

    print("\nЗадачи официанта:")
    for task in официант.tasks:
        print(f"- {task}")

if __name__ == "__main__":
    main()