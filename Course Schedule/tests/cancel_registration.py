import unittest
from src.lms import LMS
from src.employees.employee import Employee
from src.courses.course import Course
from src.courses.course_enum import CourseStatus


class TestCancelRegistration(unittest.TestCase):

    def setUp(self):
        self.lms = LMS()

    def test_cancel_registration_accepted(self):
        employee = Employee("REG-COURSE-john-PYTHON", "john", "john@gmail.com", "CANCEL_ACCEPTED")
        course = Course("PYTHON", "JOHN", "2025-08-01", "5", "50")
        course.employees.append(employee)
        self.lms.lms["OFFERING-PYTHON-JOHN"] = course

        result = self.lms.cancel_registration(["CANCEL", "REG-COURSE-john-PYTHON"])
        self.assertEqual(result, "REG-COURSE-john-PYTHON CANCEL_ACCEPTED")
        self.assertEqual(len(course.employees), 0)

    def test_cancel_registration_rejected(self):
        employee = Employee("REG-COURSE-john-PYTHON", "john", "john@gmail.com", "CANCEL_REJECTED")
        course = Course("PYTHON", "JOHN", "2025-08-01", "5", "50")
        course.employees.append(employee)
        course.set_course_status(CourseStatus.CONFIRMED.value)
        self.lms.lms["OFFERING-PYTHON-JOHN"] = course

        result = self.lms.cancel_registration(["CANCEL", "REG-COURSE-john-PYTHON"])
        self.assertEqual(result, "REG-COURSE-john-PYTHON CANCEL_REJECTED")
        self.assertEqual(len(course.employees), 1)  # not removed

    def test_cancel_registration_not_found(self):
        course = Course("PYTHON", "JOHN", "2025-08-01", "5", "50")
        self.lms.lms["OFFERING-PYTHON-JOHN"] = course

        result = self.lms.cancel_registration(["CANCEL", "NON-EXISTENT-ID"])
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
