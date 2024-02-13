from ortools.sat.python import cp_model

class Scheduling:
    def __init__(self, students, courses, teachers, rooms):
        self.model = cp_model.CpModel()
        self.solver = cp_model.CpSolver()
        self.students = students
        self.teachers = teachers
        self.courses = courses
        self.rooms = rooms
        self.day = ["Monday", "tuesday"]
        self.time = [(7, 8), (8, 9)]
        
        # Variables
        self.teacher_course_assignment = {}  # Dictionary to represent teacher-course assignments
        self.course_room_assignment = {}     # Dictionary to represent course-room assignments
        self.student_course_assignment = {}  # Dictionary to represent student-course assignments
        self.teacher_student_assignment = {}  # Dictionary to represent teacher-student assignments
        self.teacher_room_assignment = {}     # Dictionary to represent teacher-room assignments
        self.student_room_assignment = {}     # Dictionary to represent student-room assignments
        self.course_assignment = {}  # Dictionary to represent course-room-time slot assignments

        # Domains
        self.teacher_domain = {}  # Dictionary to represent the specialized courses for each teacher
        self.room_type_domain = {}     # Dictionary to represent the available rooms for each course
        self.room_availability_domain = {} # Dictionary to represent the time slot available per rooms
        self.student_domain = {}  # Dictionary to represent the courses for each student

        # Populate
        self.define_teacher_domain()
        self.define_room_domain()
        self.define_student_domain()
        self.define_course_assignment()
        self.define_teacher_student_assingment()
        self.define_teacher_room_assingment()
        self.define_teacher_room_assingment()
        self.define_course_assignment()
        

        # Solve the model
        #self.solve()

    def define_teacher_domain(self):
        # Populate variables and domains based on sample data
        for teacher in self.teachers:
            self.teacher_domain[teacher['_id']] = [course['code'] for course in teacher['specialized']]

    def define_room_domain(self):

        for room in self.rooms:
            self.room_type_domain[room['_id']] = room['types']  # Assuming types represent the types of courses supported

        for room in self.rooms:
            self.room_availability_domain[room['_id']] = {}
            for day in self.day:
                self.room_availability_domain[room['_id']][day] = self.time

        #print(self.room_availability_domain)

    def define_student_domain(self):
        for student in self.students:
            self.student_domain[student['_id']] = [course['code'] for course in student['courses']]

    def define_course_assignment(self):
        for course in self.courses:
            # Assign teachers to courses based on specialization
            self.teacher_course_assignment[course['_id']] = [teacher['_id'] for teacher in self.teachers
                                                        if course['code'] in self.teacher_domain[teacher['_id']]]
            
            # Assign rooms to courses based on room types
            self.course_room_assignment[course['_id']] = [room['_id'] for room in self.rooms
                                                    if room['types'] == course['types']]

            # Assign courses to students
            self.student_course_assignment[course['_id']] = [student['_id'] for student in self.students
                                                        if course['code'] in self.student_domain[student['_id']]]
            
    def define_teacher_student_assingment(self):
        for teacher in self.teachers:
            for student in self.students:
                for course in student['courses']:
                    # Check if the teacher is specialized in the course in the student's curriculum
                    if any(course['code'] == spec_course['code'] for spec_course in teacher['specialized']):
                        self.teacher_student_assignment[(teacher['_id'], student['_id'], course['code'])] = True

    def define_teacher_room_assingment(self):
        for teacher in self.teachers:
            for room in self.rooms:
                self.teacher_room_assignment[(teacher['_id'], room['_id'])] = True  # Assuming all teachers can be assigned to all rooms

    def define_student_room_assingment(self):
        for student in self.students:
            for room in self.rooms:
                self.student_room_assignment[(student['_id'], room['_id'])] = True  # Assuming all students can be assigned to all rooms

    """def define_course_assignment(self):
        # Define constraints and populate variables
        for course in self.courses:
            for room in self.rooms:
                for day, time_slots in self.room_availability_domain[room['_id']].values():
                    print('timeslot:', time_slots)
                    for time_slot in time_slots:
                        print('timeslot:', time_slot)
                        if time_slot[0] + course['units'] <= time_slot[1]:
                            # If the course duration fits within the time slot, add the assignment
                            self.course_assignment[(course['_id'], room['_id'], day, time_slot)] = True

        #print(self.course_assignment)"""
