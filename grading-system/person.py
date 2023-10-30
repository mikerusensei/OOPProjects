class Person:
    def __init__(self, id, name, age, gender, role) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.role = role

class Student(Person):
    def __init__(self, id, name, age, gender) -> None:
        super().__init__(id, name, age, gender, 'Student')
        self.enrolled_subjects = []
        self.subs_with_grade = []
        self.overall_grade = []

    def enroll_subjects(self, subject):
        if subject.code not in self.enrolled_subjects:
            print(f"Successfully enrolled in {subject.name}")
            self.enrolled_subjects.append(subject.code)
            subject.instructor.students_teaching.append(self.name)
        else:
            print(f"You are already enrolled in {subject.name}")

    def drop_subject(self, subject):
        if subject.code in self.enrolled_subjects:
            print(f"Successfully dropped in {subject.name}")
            self.enrolled_subjects.remove(subject.code)
            subject.instructor.students_teaching.remove(self.name)
        else:
            print(f"You are not currently enrolled in {subject.name}")

    def display_details(self, grading_period):
        print(f"[STUDENT OVERVIEW]\nId: {self.id}\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}\nEnrolled Subjects: {self.enrolled_subjects}")
        if self.subs_with_grade:
            print(f"[{grading_period.upper()} GRADES]")
            for subject_code, subject_grade, period in self.subs_with_grade:
                if period == grading_period:
                    print(f"{subject_code} {subject_grade}")
    
    def calculate_average(self, subject):
        total_grade = 0
        total_weight = 0
        for subject_code, subject_grade, period in self.subs_with_grade:
            if subject_code == subject.code:
                total_grade += subject_grade
                total_weight += 1
        
        if total_weight == 0:
            return 0  

        average = total_grade / total_weight
        print(f"Overall Grade in {subject.code}: {average}")
        return average

class Instructor(Person):
    def __init__(self, id, name, age, gender) -> None:
        super().__init__(id, name, age, gender, 'Instructor')
        self.subjects_teaching = None
        self.student_grades = []
        self.students_teaching = []

    def assign_subject(self, subject):
        self.subjects_teaching = subject
        subject.instructor = self

    def give_grade(self, student, grading_period):
        if student.name in self.students_teaching:
            grade = self.calculate_grade(student, grading_period)
            student.subs_with_grade.append((self.subjects_teaching.code, grade, grading_period))
            self.student_grades.append((student.name, grade, grading_period))
        else:
            print(f"{student.name} was not on the list")

    def calculate_grade(self, student, grading_period):
        self.total_grade = (
            (0.1 * self.get_grade(self.subjects_teaching.attendance_grade[grading_period], student.name)) +
            (0.2 * self.get_grade(self.subjects_teaching.quiz_grade[grading_period], student.name)) +
            (0.2 * self.get_grade(self.subjects_teaching.seatwork_grade[grading_period], student.name)) +
            (0.2 * self.get_grade(self.subjects_teaching.recitation_grade[grading_period], student.name)) +
            (0.3 * self.get_grade(self.subjects_teaching.exam_grade[grading_period], student.name))
            )
        #self.student_grades.append((student.name, self.total_grade))
        return self.total_grade
    
    def get_grade(self, grade, student):
        for name, grades in grade:
            if name == student:
                return grades
        return 0

    def display_student_records(self, grading_period):
        print(f"[{self.name}'s CLASS RECORD on {self.subjects_teaching.name}]")
        for index, (student_name, student_grade, grading_period) in enumerate(self.student_grades):
            print(f"{index + 1}. {student_name} {grading_period} {student_grade}")

    def display_details(self):
        if self.subjects_teaching:
            self.subject_name = self.subjects_teaching.name
        else:
            self.subject_name = 'None'
        print(f"[INSTRUCTOR OVERVIEW]\nId: {self.id}\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}\nTeaching: {self.subject_name}\nStudents: {self.students_teaching}")
