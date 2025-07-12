class Course:

    def __init__(self, course_title, instructor, date, min_employee, max_employee):
        self.employees = []
        self._course_id = None
        self.course_title = course_title
        self.instructor = instructor
        self.min_employee = min_employee
        self.max_employee = max_employee
        self.date = date
        self._course_status = None

    def get_course_id(self):
        return self._course_id

    def set_course_id(self, course_id):
        self._course_id = course_id

    def get_course_status(self):
        return self._course_status

    def set_course_status(self, course_status):
        self._course_status = course_status
