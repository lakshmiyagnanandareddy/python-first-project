import array as arr


def ex():
    a = arr.array("i", [1, 4, 4, 7, 8, 8])
    k = range(len(a))
    for i in k:
        x = 0
        for j in k:
            if a[i] == a[j]:
                x = x+1
                k = k-1
                y = a[j]
                a.remove(y)
        print(a[i], "is occurred in an array is", x, "times")


#  removing duplicate
def main():

    def ex(k, a, j):
        if j == k:
            return a
        elif j < k:
            for i in range(k):
                if i == j:
                    pass
                elif a[i] == a[j]:
                    x = a[i]
                    a.remove(x)
                    k = k-1
                    return ex(k, a, j)
            return ex(k, a, j + 1)

    a = arr.array("i", [1, 2, 1, 3, 4, 4, 7, 5])
    j = 0
    k = len(a)
    reverse = ex(k, a, j)
    print(reverse)

# occurence
def occur():

    def occ(a, j, k, b):
        if b <= j-1:
            i = 0
            x = 0
            for i in range(j):
                if a[i] == a[b]:
                    x = x+1
            print(a[b], "is occurred :", x, "times")
            return occ(a, j, k, b+1)
    a = arr.array("i", [1, 3, 4, 6, 3, 1, 1])
    j = len(a)
    k = 0
    b = 0
    occ(a, j, k, b)


def remov():
    import array as arr
    a = arr.array("i", [1, 2, 3, 4, 5, 3, 6])
    a.remove(3)
    print(a)


def duplic():
        def ex(k, a, j):
            if j == k:
                return True
            elif j < k:
                for i in range(k):
                    if i == j:
                        pass
                    elif a[i] == a[j]:
                        return False
                return ex(k, a, j + 1)

        a = arr.array("i", [1, 2, 3, 4, 5])
        j = 0
        k = len(a)
        print((ex(k, a, j)))


def firstOccur():
    def ex(k, a, j):
        if j == k:
            return -1
        elif j < k:
            for i in range(k):
                if i == j:
                    pass
                elif a[i] == a[j]:
                    return a[i], "is the first occurence value"
            return ex(k, a, j + 1)

    a = arr.array("i", [1, 2, 3, 4, 5, 5])
    j = 0
    k = len(a)
    print((ex(k, a, j)))


def FindingSequence():
    import array as arr
    a = arr.array("i", [10, 14, 15, 16, 18, 20])
    j = 0
    for k in range(min(a), max(a)):
        if k == a[j]:
            j = j+1
            pass
        else:
            print(k)


def ad():
    import array as arr

    def test(nums):
        return sum(range(10, 21)) - sum(list(nums))

    array_num = arr.array('i', [10, 11, 12, 13, 14, 16, 17, 18, 19, 20])
    print("Original array:")
    for i in range(len(array_num)):
        print(array_num[i], end=' ')
    print("\nMissing number in the said array (10-20): ", test(array_num))

    array_num = arr.array('i', [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    print("\nOriginal array:")
    for i in range(len(array_num)):
        print(array_num[i], end=' ')
    print("\nMissing number in the said array (10-20): ", test(array_num))


ad()