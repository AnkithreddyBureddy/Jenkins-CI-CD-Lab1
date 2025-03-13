import unittest
import todo

class TestTodoApp(unittest.TestCase):
    def test_add_task(self):
        todo.save_tasks([])  # Clear previous tasks
        todo.add_task("Test Task")
        self.assertIn("Test Task", todo.load_tasks())

    def test_remove_task(self):
        todo.save_tasks(["Test Task"])
        todo.remove_task(1)
        self.assertNotIn("Test Task", todo.load_tasks())

if __name__ == "__main__":
    unittest.main()
