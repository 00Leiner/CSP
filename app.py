import data
import algo.scheduling as scheduling

if __name__ == "__main__":
    students = data.students
    courses = data.courses
    teachers = data.teachers
    rooms = data.rooms

    schedule = scheduling.Scheduling(students, courses, teachers, rooms)