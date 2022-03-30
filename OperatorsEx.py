#discount for a sells man
discountOf = 30/100
originalPrice = int(input("the product price is "))
print("the product price after the discount is",originalPrice*discountOf,sep='# ')# sep will seperate both strings
                                                                                # end it is used to write at the end of the line

#averageForATeacher
number_of_exams = 3
firstExamMarks = int(input("Enter the marks of the first exam"))
secondExamMarks = int(input("Enter the marks of the second exam"))
thirdExamMarks = int(input("Enter the marks of the third exam"))
print("Average of this marks is",(firstExamMarks + secondExamMarks + thirdExamMarks)/number_of_exams)


#percentageOfPassedAndFailedStudents
passedStudentsInAClass = int(input("Enter the number of students passed in the class "))
failedStudentsInAClass = int(input("Enter the number of students failed in the class "))
totalStudentsInAClass = int(input("Enter the number of the students the class "))
print("The percentage of the students passed in the class is",((passedStudentsInAClass / totalStudentsInAClass) * 100))
print("The percentage of the students failed in the class is ",((failedStudentsInAClass / totalStudentsInAClass) * 100))
