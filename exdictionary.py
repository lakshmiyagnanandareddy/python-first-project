import pickle

def main():
    again = "y"
    while "y" == again:
        #print("1 for enter the student data")
        #print("2 for read student data")
        choice = 0
        while choice != 1 and choice != 2:
            try:
                choice = int(input("1 for enter the student data\n"
                                   "2 for read student data : "))
                if choice != 1 and choice !=2:
                    print("wrong entry")
            except:
                choice = int(input("Enter either 1 or 2"))

        if 1 == choice:
            my_file = open("student.text", "wb")
            write(my_file)
        elif 2 == choice:
            my_file = open("student.text", "rb")
            read(my_file)
        print("do you want to do something else\n"
              "type 'y' for yes and 'n' for no")
        again = input()


def write(my_file):
    again = "y"
    dictionary = dict()
    while "y" == again.lower() :
        student_name = input("Enter student name")
        student_score = int(input("Enter score"))
        dictionary[student_name] = student_score
        pickle.dump(dictionary, my_file)
        again = input("If you want to add other student data type 'y' for yes and 'n' for no.")
    my_file.close()

def read(my_file):
    permission = False
    try:

        while permission == False :
            my= pickle.load(my_file)
            print(my)
    except :
        permission == True
    my_file.close()




main()