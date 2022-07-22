import csv
with open("demo.csv", 'r') as demo:
    read_file = csv.reader(demo)
    with open("demo1.csv", 'w') as demo1:
        write = csv.writer(demo1, delimiter='-')
        for writ in read_file:
            write.writerow(writ)
with open("demo1.csv", 'r') as demo1_file:
    demo_read_file = csv.reader(demo1_file, delimiter='-')
    for details in demo_read_file:
        print(details)

with open("demo.csv", 'r') as demo1_file:
    demo_read_file = csv.DictReader(demo1_file, fieldnames=["first_name", "Last_name", "email"])
    next(demo_read_file)
    for details in demo_read_file:
        print(details["email"])

