class TimeSlot:
    def __init__(self, days: str, start_time: str, end_time: str):
        self.days = days
        self.start_time = start_time
        self.end_time = end_time

    def overlaps(self, other: 'TimeSlot') -> bool:
        """Returns True if this time slot overlaps with another."""
        # Simple overlap check: check if they share any days
        shared_days = set(self.days).intersection(set(other.days))
        if not shared_days:
            return False
            
        # Check time overlap
        return not (self.end_time <= other.start_time or self.start_time >= other.end_time)

class Course:
    def __init__(self, code: str, title: str, capacity: int, time_slot: TimeSlot, prerequisites: list = None):
        self.code = code
        self.title = title
        self.capacity = capacity
        self.time_slot = time_slot
        self.prerequisites = prerequisites or []
        self.enrolled_students = []

    def is_full(self) -> bool:
        return len(self.enrolled_students) >= self.capacity

class Student:
    def __init__(self, student_id: str, name: str):
        self.id = student_id
        self.name = name
        self.enrolled_courses = []
        self.completed_courses = []

    def has_completed(self, course_code: str) -> bool:
        return course_code in self.completed_courses

class EnrollmentSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student: Student):
        self.students[student.id] = student

    def add_course(self, course: Course):
        self.courses[course.code] = course

    def register_course(self, student_id: str, course_code: str) -> dict:
        """
        Equivalent to registerCourse from EnrollmentSystem.java.
        Attempts to register a student for a course, checking all rules.
        """
        student = self.students.get(student_id)
        if not student:
            return {"success": False, "message": f"Student not found: {student_id}"}

        course = self.courses.get(course_code)
        if not course:
            return {"success": False, "message": f"Course not found: {course_code}"}

        # 1. Already enrolled check
        if course_code in student.enrolled_courses:
            return {"success": False, "message": f"You are already enrolled in {course_code}."}

        # 2. Capacity check
        if course.is_full():
            return {"success": False, "message": f"Course {course_code} is full (capacity: {course.capacity})."}

        # 3. Prerequisite check
        for prereq in course.prerequisites:
            if not student.has_completed(prereq):
                return {"success": False, "message": f"Prerequisite not met: you must complete {prereq} before enrolling."}

        # 4. Time conflict check
        for enrolled_code in student.enrolled_courses:
            enrolled_course = self.courses.get(enrolled_code)
            if enrolled_course and enrolled_course.time_slot.overlaps(course.time_slot):
                return {
                    "success": False, 
                    "message": f"Schedule conflict: {course_code} overlaps with {enrolled_code}."
                }

        # All checks passed — perform enrollment
        student.enrolled_courses.append(course_code)
        course.enrolled_students.append(student_id)
        return {"success": True, "message": f"Successfully enrolled in {course_code} - {course.title}."}

# ==========================================
# Example usage demonstrating the Use Case
# ==========================================
if __name__ == '__main__':
    system = EnrollmentSystem()
    
    # 1. Setup Data
    system.add_course(Course("CS101", "Intro to Programming", 30, TimeSlot("MWF", "09:00", "10:00")))
    system.add_course(Course("CS201", "Data Structures", 25, TimeSlot("MWF", "10:00", "11:00"), prerequisites=["CS101"]))
    system.add_course(Course("MATH101", "Calculus I", 35, TimeSlot("MWF", "10:30", "11:30")))

    alice = Student("STU001", "Alice Johnson")
    system.add_student(alice)

    # 2. Test registration
    print("--- Test 1: Missing Prerequisite ---")
    result1 = system.register_course("STU001", "CS201")
    print(result1["message"])

    print("\n--- Test 2: Successful Registration ---")
    alice.completed_courses.append("CS101") # Simulate passing the prereq
    result2 = system.register_course("STU001", "CS201")
    print(result2["message"])

    print("\n--- Test 3: Time Conflict ---")
    result3 = system.register_course("STU001", "MATH101")
    print(result3["message"])
