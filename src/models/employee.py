class Employee:
    """
    Класс для представления сотрудника ресторана.
    """
    def __init__(self, id: int, name: str, role: str):
        """
        Инициализация сотрудника.
        
        Args:
            id: Уникальный идентификатор сотрудника
            name: Имя сотрудника
            role: Должность сотрудника
        """
        self.id = id
        self.name = name
        self.role = role
        self.tasks = []

    def assign_task(self, task):
        """Назначить задачу сотруднику."""
        self.tasks.append(task)
        task.assign_to(self)

    def complete_task(self, task):
        """Отметить задачу как выполненную."""
        if task in self.tasks:
            task.update_status("выполнено")
            
    def __str__(self):
        """Строковое представление сотрудника."""
        return f"{self.name} ({self.role})"