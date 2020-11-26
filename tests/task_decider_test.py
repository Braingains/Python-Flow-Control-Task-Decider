import unittest
from src.task import Task
from src.task_decider import *

class TestTaskDecider(unittest.TestCase):
    def setUp(self):
        self.clean_windows = Task("clean_windows", 10)
        self.cook_dinner = Task("cook_dinner", 15)
        self.wash_dishes = Task("wash_dishes", 5)
    
    def test_clean_windows_beats_wash_dishes(self):
        get_preferred_option(self.clean_windows, self.wash_dishes)
        self.assertEqual("clean_windows", (self.clean_windows.description))

    def test_clean_windows_loses_to_wash_dishes(self):
        get_preferred_option(self.clean_windows, self.wash_dishes)
        self.assertEqual("wash_dishes", (self.wash_dishes.description))

    def test_wash_dishes_beats_cook_dinner(self):
        get_preferred_option(self.wash_dishes, self.cook_dinner)
        self.assertEqual("wash_dishes", (self.wash_dishes.description))
    
    def test_wash_dishes_loses_to_clean_windows(self):
        get_preferred_option(self.wash_dishes, self.clean_windows)
        self.assertEqual("clean_windows", (self.clean_windows.description))

    def test_cook_dinner_beats_clean_windows(self):
        get_preferred_option(self.cook_dinner, self.clean_windows)
        self.assertEqual("cook_dinner", (self.cook_dinner.description))

    def test_cook_dinner_loses_to_wash_dishes(self):
        get_preferred_option(self.cook_dinner, self.wash_dishes)
        self.assertEqual("wash_dishes", (self.wash_dishes.description))

    