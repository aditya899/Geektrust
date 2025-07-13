import unittest
from src.lms import LMS
from src.courses.course import Course


class TestAddCourse(unittest.TestCase):
    def setUp(self):
        self.lms = LMS()

    def test_add_course_with_insufficient_details(self):
        # Less than 6 items
        result = self.lms.add_course(["ADD-COURSE", "PYTHON", "JOHN"])
        self.assertEqual(result, "INPUT_DATA_ERROR")

    def test_add_course_with_valid_details(self):
        details = ["ADD-COURSE", "PYTHON", "JOHN", "2025-08-01", "5", "50"]
        result = self.lms.add_course(details)
        expected_id = "OFFERING-PYTHON-JOHN"
        self.assertEqual(result, expected_id)
        self.assertIn(expected_id, self.lms.lms)
        self.assertIsInstance(self.lms.lms[expected_id], Course)
        self.assertEqual(self.lms.lms[expected_id].course_title, "PYTHON")
        self.assertEqual(self.lms.lms[expected_id].instructor, "JOHN")


if __name__ == "__main__":
    unittest.main()
