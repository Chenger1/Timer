from decimal import Decimal

from src.models.tasks import Tasks


class TaskEarningCalculator:
    @classmethod
    def calculate_earning_for_task(cls, task: Tasks):
        task_duration_in_hours = (task.end_date - task.start_date).seconds / 60 / 60
        if task.project.rate is None:
            task.earned = Decimal(0)
        else:
            task.earned = round(Decimal(task_duration_in_hours) * task.project.rate, 2)
