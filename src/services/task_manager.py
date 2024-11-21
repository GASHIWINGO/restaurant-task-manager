import os
import sys
from typing import List

# Получаем путь к директории src
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from models.task import Task
from models.employee import Employee

class TaskManager:
    """
    Класс для управления задачами и сотрудниками.
    """
    def __init__(self):
        """Инициализация менеджера задач."""
        self.tasks: List[Task] = []
        self.employees: List[Employee] = []

    def create_task(self, title: str, description: str) -> Task:
        """
        Создать новую задачу.
        
        Args:
            title: Название задачи
            description: Описание задачи
            
        Returns:
            Task: Созданная задача
        """
        task_id = len(self.tasks) + 1
        task = Task(task_id, title, description)
        self.tasks.append(task)
        return task

    def add_employee(self, name: str, role: str) -> Employee:
        """
        Добавить нового сотрудника.
        
        Args:
            name: Имя сотрудника
            role: Должность сотрудника
            
        Returns:
            Employee: Созданный сотрудник
        """
        employee_id = len(self.employees) + 1
        employee = Employee(employee_id, name, role)
        self.employees.append(employee)
        return employee

    def get_employee_tasks(self, employee_id: int) -> List[Task]:
        """Получить список задач сотрудника."""
        for employee in self.employees:
            if employee.id == employee_id:
                return employee.tasks
        return []

    def get_tasks_by_status(self, status: str) -> List[Task]:
        """Получить список задач по статусу."""
        return [task for task in self.tasks if task.status == status]