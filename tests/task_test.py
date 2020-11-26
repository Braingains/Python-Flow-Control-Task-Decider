import unittest
from src.task import Task

class TestTask(unittest.TestCase):
    def setUp(self):
        self.task_1 = Task("clean_windows", 10)
        self.task_2 = Task("cook_dinner", 15)
        self.task_3 = Task("wash_dishes", 5)
