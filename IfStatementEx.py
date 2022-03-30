#avgForTheExamResult

noOfExams = 4
examResult_1 = int(input("Enter first exam result "))
examResult_2 = int(input("Enter second exam result "))
examResult_3 = int(input("Enter the third exam result "))
examResult_4 = int(input("Enter the fourth exam result "))
avg = (examResult_1+examResult_2+examResult_3+examResult_4)/noOfExams
if avg >= 50:
    print("The student passed the exam with", avg, "%")
else:
    print("The student failed the exam with", avg, "%")

# typistInterview
minute = 60
typeSpeed = int(input("Enter the type speed of the candidate"))
if minute < typeSpeed:
    print("The candidate is passed and come for the second interview")
else:
    print("we required the candidate who can type above 60 WPM")
