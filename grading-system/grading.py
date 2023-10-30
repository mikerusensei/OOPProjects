from person import Instructor

class Subject:
    def __init__(self, code, name, units, days) -> None:
        self.code = code
        self.name = name
        self.instructor = None
        self.units = units
        self.days = days

class Grading(Subject):
    def __init__(self, code, name, units, days) -> None:
        super().__init__(code, name, units, days)
        self.grading_periods = ['prelim', 'midterm', 'semi-final', 'final']
        self.attendance_grade = {}
        self.quiz_grade = {}
        self.seatwork_grade = {}
        self.recitation_grade = {}
        self.exam_grade = {}
        self.initialize_dict()

    def initialize_dict(self):
        for period in self.grading_periods:
            self.attendance_grade[period] = []
            self.quiz_grade[period] = []
            self.seatwork_grade[period] = []
            self.recitation_grade[period] = []
            self.exam_grade[period] = []

    def add_attendace_grade(self, instructor, student, grade, grading_period):
        if grading_period in self.grading_periods:
            if self.code in student.enrolled_subjects:
                if instructor == self.instructor:
                    print(f"{self.instructor.name} Recorded {grading_period.capitalize()} [Attendace]")
                    self.attendance_grade[grading_period].append((student.name, grade))
                else:
                    print(f"Instructor {self.instructor.name} can only add grade")
            else:
                print(f"{student.name} was not enrolled in {self.name}")

    def add_quiz_grade(self, instructor, student, grade, grading_period):
        if self.code in student.enrolled_subjects:
            if instructor == self.instructor:
                print(f"{self.instructor.name} Recorded {grading_period.capitalize()} [Quiz]")
                self.quiz_grade[grading_period].append((student.name, grade))
            else:
                print(f"Instructor {self.instructor.name} can only add grade")
        else:
            print(f"{student.name} was not enrolled in {self.name}")
            
    def add_seatwork_grade(self, instructor, student, grade, grading_period):
        if self.code in student.enrolled_subjects:
            if instructor == self.instructor:
                print(f"{self.instructor.name} Recorded {grading_period.capitalize()} [Seatwork]")
                self.seatwork_grade[grading_period].append((student.name, grade))
            else:
                print(f"Instructor {self.instructor.name} can only add grade")
        else:
            print(f"{student.name} was not enrolled in {self.name}")

    def add_recitation_grade(self, instructor, student, grade, grading_period):
        if self.code in student.enrolled_subjects:
            if instructor == self.instructor:
                print(f"{self.instructor.name} Recorded {grading_period.capitalize()} [Recitation]")
                self.recitation_grade[grading_period].append((student.name, grade))
            else:
                print(f"Instructor {self.instructor.name} can only add grade")
        else:
            print(f"{student.name} was not enrolled in {self.name}")

    def add_exam_grade(self, instructor, student, grade, grading_period):
        if self.code in student.enrolled_subjects:
            if instructor == self.instructor:
                print(f"{self.instructor.name} Recorded {grading_period.capitalize()} [Exam]")
                self.exam_grade[grading_period].append((student.name, grade))
            else:
                print(f"Instructor {self.instructor.name} can only add grade")
        else:
            print(f"{student.name} was not enrolled in {self.name}")
