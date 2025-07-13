from src.courses.course import Course
from src.employees.employee import Employee
from src.employees.employee_enum import EmployeeStatus
from src.courses.course_enum import CourseStatus


class LMS:
    lms = {}

    def add_course(self, course_details):
        if len(course_details) < 6:
            return "INPUT_DATA_ERROR"
        else:
            course_offering_id = 'OFFERING-' + course_details[1] + '-' + course_details[2]
            course = Course(course_details[1], course_details[2], course_details[3], course_details[4],
                            course_details[5])
            self.lms[course_offering_id] = course
            return course_offering_id

    def register_course(self, register_details):
        if len(register_details) < 3:
            return "INPUT_DATA_ERROR"

        course_offering_id = register_details[2]
        if course_offering_id not in self.lms:
            return
        course = self.lms[course_offering_id]
        if len(course.employees) < int(course.max_employee):
            if course.get_course_status() == CourseStatus.CONFIRMED.value:
                return EmployeeStatus.DECLINED.value
            employee_name = register_details[1].split('@')[0]
            course_title = course.course_title
            register_id = 'REG-COURSE-' + employee_name + '-' + course_title
            employee = Employee(register_id, employee_name, register_details[1], EmployeeStatus.ACCEPTED.value)
            course.employees.append(employee)
            return ' '.join([register_id, EmployeeStatus.ACCEPTED.value])
        elif len(course.employees) == int(course.max_employee):
            return "COURSE_FULL_ERROR"

    def course_allotment(self, allot_details):
        course_offering_id = allot_details[1]
        if course_offering_id not in self.lms:
            return
        course = self.lms[course_offering_id]
        self.print_confirmed_course(course, course_offering_id)

    def cancel_registration(self, cancel_details):
        registration_number = cancel_details[1]
        for course_offering_id, course in self.lms.items():
            for employee in course.employees:
                if employee.registration_number == registration_number:
                    if course.get_course_status() == CourseStatus.CONFIRMED.value:
                        return ' '.join([registration_number, EmployeeStatus.CANCEL_REJECTED.value])
                    else:
                        course.employees.remove(employee)
                        return ' '.join([registration_number, EmployeeStatus.CANCEL_ACCEPTED.value])

    @staticmethod
    def print_confirmed_course(course, course_offering_id):
        _employees = course.employees
        sorted_employees = sorted(course.employees, key=lambda _employees: _employees.registration_number)
        if len(course.employees) == 0 or len(course.employees) < int(course.min_employee):
            course.set_course_status(CourseStatus.COURSE_CANCELED.value)
            for employee in sorted_employees:
                print(' '.join([employee.registration_number, employee.email, course_offering_id, course.course_title,
                                course.instructor, course.date, CourseStatus.COURSE_CANCELED.value]))
        else:
            course.set_course_status(CourseStatus.CONFIRMED.value)
            for employee in sorted_employees:
                print(' '.join([employee.registration_number, employee.email, course_offering_id, course.course_title,
                                course.instructor, course.date, CourseStatus.CONFIRMED.value]))

    # def print_added_course(self):
    #     print(self.lms)
