def main():
    student1 = "vinitha"
    student2 = "nandu"
    student3 = "lakshmi"

    my_file = open("student.txt", "w")

    my_file.write(student1 + "\n")
    my_file.write(student2 + "\n")
    my_file.write(student3 + "\n")

    my_file.close()

    print("your data has been successfully saved")


def read():

    my_file = open("student.txt", "rt")# r- read,a-append,w-write,x-create file....t-text format,b-binary mode(ex;images)
    #print(my_file.read()) # read()-inside the brackets we give a number it will print that much characters only
    line1 = my_file.readline().rstrip("\n")# .rstip("\n") removes "\n"which we have written first line in the write part
                                            # it will removes the data from the lat by comparing the removing string's
    print(line1)
    print(my_file.readline())
    print(my_file.readline())
main()
read()
