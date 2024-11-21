class Task:
    """
    Класс для представления задачи в ресторане.
    """
    def __init__(self, id: int, title: str, description: str, status: str = "ожидает"):
        """
        Инициализация задачи.
        
        Args:
            id: Уникальный идентификатор задачи
            title: Название задачи
            description: Описание задачи
            status: Статус задачи (по умолчанию "ожидает")
        """
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.assigned_to = None

    def assign_to(self, employee):
        """Назначить задачу сотруднику."""
        self.assigned_to = employee

    def update_status(self, new_status):
        """Обновить статус задачи."""
        self.status = new_status

    def __str__(self):
        """Строковое представление задачи."""
        return f"Задача #{self.id}: {self.title} ({self.status})"