from person import Student, Instructor
from grading import Grading


if __name__ == '__main__':
    # create subjects
    oop = Grading('OOP', 'Object Oriented Programming', 3, 'Saturday')
    humcoin = Grading('HUMCOIN', 'Human Computer Interaction', 3, 'Thursday')
    discrete = Grading('DISCRETE-2', 'Discrete Structures', 3, 'Friday')
    accounting = Grading('ACCTGFND', 'Fundamentals of Accounting', 3, 'Saturday')
    fil = Grading('FIL-3', 'Malikhaing Pagsulat', 3, 'Friday')
    aap = Grading('AAP', 'Arts Appreciation', 3, 'Monday')
    tcw = Grading('TCW', 'The Contemporary World', 3, 'Monday')
    pe = Grading('PE-3', 'Individual Sports', 2, 'Monday')

    # create instructors
    instructor_1 = Instructor('0001', 'Aldrich Bernardo', 25, 'Male')
    instructor_2 = Instructor('0002', 'Susana Tolentino', 25, 'Female')
    instructor_3 = Instructor('0003', 'Jober Reyes', 25, 'Male')
    instructor_4 = Instructor('0004', 'Ernesto Arca', 25, 'Male')
    instructor_5 = Instructor('0005', 'Lou Ayende', 25, 'Female')
    instructor_6 = Instructor('0006', 'Annabelle Buising', 25, 'Female')
    instructor_7 = Instructor('0007', 'Juarel Inson', 25, 'Male')
    instructor_8 = Instructor('0008', 'Orly Romiral', 25, 'Male')

    # assign instructors
    instructor_1.assign_subject(oop)
    instructor_2.assign_subject(humcoin)
    instructor_3.assign_subject(discrete)
    instructor_4.assign_subject(accounting)
    instructor_5.assign_subject(fil)
    instructor_6.assign_subject(aap)
    instructor_7.assign_subject(tcw)
    instructor_8.assign_subject(pe)

    # create students
    student_1 = Student('23-0001', 'Michael Alexis', 19, 'Male')
    student_2 = Student('23-0002', 'Raecell Ann', 19, 'Female')
    student_3 = Student('23-0003', 'Rodien Jillian', 19, 'Female')
    student_4 = Student('23-0004', 'Mark Jomari', 20, 'Male')

    #################################################
    ###### Trial Process Student_1 (Correct) #####
    # enroll student_1
    student_1.enroll_subjects(oop)
    student_1.enroll_subjects(humcoin)
    student_1.enroll_subjects(discrete)
    student_1.enroll_subjects(accounting)
    student_1.enroll_subjects(fil)
    student_1.enroll_subjects(aap)
    student_1.enroll_subjects(tcw)
    student_1.enroll_subjects(pe)

    ### [PRELIM] ###
    # grading oop
    oop.add_attendace_grade(instructor_1, student_1, 100, 'prelim')
    oop.add_quiz_grade(instructor_1, student_1, 90, 'prelim')
    oop.add_seatwork_grade(instructor_1, student_1, 90, 'prelim')
    oop.add_recitation_grade(instructor_1, student_1, 100, 'prelim')
    oop.add_exam_grade(instructor_1, student_1, 85, 'prelim')
    instructor_1.give_grade(student_1, 'prelim')
    
    # grading humcoin
    humcoin.add_attendace_grade(instructor_2, student_1, 100, 'prelim')
    humcoin.add_quiz_grade(instructor_2, student_1, 90, 'prelim')
    humcoin.add_seatwork_grade(instructor_2, student_1, 90, 'prelim')
    humcoin.add_recitation_grade(instructor_2, student_1, 85, 'prelim')
    humcoin.add_exam_grade(instructor_2, student_1, 90, 'prelim')
    instructor_2.give_grade(student_1, 'prelim')

    ### [MIDTERM] ###
    # grading oop
    oop.add_attendace_grade(instructor_1, student_1, 100, 'midterm')
    oop.add_quiz_grade(instructor_1, student_1, 90, 'midterm')
    oop.add_seatwork_grade(instructor_1, student_1, 90, 'midterm')
    oop.add_recitation_grade(instructor_1, student_1, 100, 'midterm')
    oop.add_exam_grade(instructor_1, student_1, 85, 'midterm')
    instructor_1.give_grade(student_1, 'midterm')

    # grading humcoin
    humcoin.add_attendace_grade(instructor_2, student_1, 100, 'midterm')
    humcoin.add_quiz_grade(instructor_2, student_1, 90, 'midterm')
    humcoin.add_seatwork_grade(instructor_2, student_1, 90, 'midterm')
    humcoin.add_recitation_grade(instructor_2, student_1, 85, 'midterm')
    humcoin.add_exam_grade(instructor_2, student_1, 90, 'midterm')
    instructor_2.give_grade(student_1, 'midterm')

    ### [SEMI FINAL] ###
    # grading oop
    oop.add_attendace_grade(instructor_1, student_1, 100, 'semi-final')
    oop.add_quiz_grade(instructor_1, student_1, 90, 'semi-final')
    oop.add_seatwork_grade(instructor_1, student_1, 90, 'semi-final')
    oop.add_recitation_grade(instructor_1, student_1, 100, 'semi-final')
    oop.add_exam_grade(instructor_1, student_1, 85, 'semi-final')
    instructor_1.give_grade(student_1, 'semi-final')

    ### [FINAL] ###
    # grading oop
    oop.add_attendace_grade(instructor_1, student_1, 100, 'final')
    oop.add_quiz_grade(instructor_1, student_1, 90, 'final')
    oop.add_seatwork_grade(instructor_1, student_1, 90, 'final')
    oop.add_recitation_grade(instructor_1, student_1, 100, 'final')
    oop.add_exam_grade(instructor_1, student_1, 85, 'final')
    instructor_1.calculate_grade(student_1, 'final')
    instructor_1.give_grade(student_1, 'final')
    
    # displaying details
    student_1.display_details('prelim')
    student_1.display_details('midterm')
    student_1.display_details('semi-final')
    student_1.display_details('final')
    student_1.calculate_average(oop)
    student_1.calculate_average(humcoin)

    #################################################


    '''
    #################################################
    ##### Trial Process Student 3 (Wrong) #####
    # enroll student_3
    student_3.enroll_subjects(oop)
    student_3.enroll_subjects(humcoin)
    student_3.enroll_subjects(discrete)
    student_3.enroll_subjects(accounting)
    student_3.enroll_subjects(fil)
    student_3.enroll_subjects(aap)
    student_3.enroll_subjects(tcw)
    student_3.enroll_subjects(pe)

    #student_3.enroll_subjects(oop)
    #student_3.drop_subject(pe)
    #student_3.drop_subject(pe)

    # oop grading
    oop.add_attendace_grade(instructor_2, student_3, 100)
    oop.add_quiz_grade(instructor_2, student_3, 95)
    oop.add_seatwork_grade(instructor_2, student_3, 99)
    oop.add_recitation_grade(instructor_2, student_3, 100)
    oop.add_exam_grade(instructor_2, student_3, 90)
    instructor_1.calculate_grade(student_3)
    instructor_1.give_grade(student_3)

    # display details
    #student_3.display_details()
    
    #################################################
    '''

    #################################################
    ### Instrutor ###
    instructor_1.display_details()
    instructor_1.display_student_records('prelim')
