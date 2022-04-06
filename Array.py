import array as arr

test = arr.array("i", [1, 2, -1, 3, 4, 5, 7])   # 'i' will be the data type of signed have integers.
# testt = arr.array("I", [1, 2, 3, 4, -1])
# "I" will be the data type of unsigned only positive integers.
testtt = arr.array("I", [1, 2, 3, 4])

# for i in len(test):
print(test.buffer_info())   # buffer_info() will give you the output - one is address of array and second is data type.
# print(testt)
print(testtt)
for i in testtt:
    print(i)

test_char = arr.array("u", ["a", "b", "c"])
for i in test_char:
    print(i)

copy_array = arr.array(testtt.typecode, (a*a for a in testtt))
for i in copy_array:
    print(i)


def insert():
    import array as arr

    in_array = arr.array("i", [])
    length_of_array = int(input("Enter the length of an array : "))
    for i in range(length_of_array):
        print("Enter the element number", i + 1, "of the array")
        add_array = int(input())
        in_array.append(add_array)
    print(in_array)
    search_index = int(input("Enter the number you want to find index of that number : "))
    for i in range(len(in_array)):
        if in_array[i] == search_index:
            print(i, "is the index of", search_index)
            break
    print("search index using functions - ", in_array.index(search_index))


def numpy():
    def tes1():
        import numpy as np
        test1 = np.array([1, 2, 3, 4, 5], str)
        test2 = np.linspace(0, 16, num=10, endpoint=False, retstep=True,  dtype=int)
        # num - it divides the number of the parts.(optional- default number is 50)
        # endpoint = it gives us choose to us weather we want to include last sample in the array list or not(optional).
        # retstep = it gives us the difference(optional).
        # dtype = it gives us the datatype(optional)
        test3 = np.arange(1, 10, 2)
        # (it will start from, upto, number of addition)
        test4 = np.logspace(0, 4, num=5, endpoint=True, base=2, dtype=int)
        test5 = np.zeros(5, int)
        test6 = np.ones(10, float)
        print(test1)
        print(test2)
        print(test3)
        print(test4)
        print(test5)
        print(test6)

    def tes2():
        import numpy as np
        test1 = np.array([1, 2, 3, 4, 5])
        test2 = test1
        test3 = test1
        test1[1] = 4
        test4 = test1.view()
        test5 = test1.copy()
        test1[4] = 2

        print(test2)
        print(id(test1))    # id-id used for the address.
        print(id(test2))
        print(id(test3))
        print(id(test4))
        print(test1)
        print(test5)
    def matrx():
        import numpy as np
        from numpy import matrix
        arr = np.array([
                        [1, 2, 3],
                       [4, 5, 6]
                        ])
        print(arr)
        print(arr.dtype)    # it gives the data type of the array.
        print(arr.size)  # it gives the no.of elements in the array.
        print(arr.shape)    # it gives no.of rows, no.of columns in the array.
        print(arr.ndim)   # it gives the no.of dimensions in the array.
        print(arr.flatten())    # it will total rows in a single row.
        print(arr.reshape(3, 2))    # it will gives the no.of rows and columns according to our conditions
        print()
        m = matrix("1 2 3; 4 6 8; 1 4 5")
        n = matrix("1 2 9; 9 6 8; 6 4 5")

        print(m)
        print(m.diagonal())  # it will print the diagonal matrix of the m.
        print(m.max())  # it will give the maximum value of the "m" matrix.
        print(m.min())  # it will give the minimum value of the "m" matrix.
        print("addition", "\n",  m+n)
        print("multiplication", "\n", m*n)
    matrx()

# difference between array and list is integer is seperated by ',' in list and '_' in array.


