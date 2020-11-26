import unittest
from src.task import Task

def get_preferred_option (task_1, task_2):
    if task_1 or task_2 == "clean_windows" and task_1 or task_2 != "cook_dinner":
        return "clean_windows"
    elif task_1 or task_2 == "wash_dishes" and task_1 or task_2 != "clean_windows":
        return "wash_dishes"
    else:
         task_1 or task_2 == "cook_dinner" and task_1 or task_2 != "wash_dishes"
         return "cook_dinner"
