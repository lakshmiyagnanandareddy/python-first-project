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



def main():

    def ex(k, a, j):
        for i in range(k):
            if i == j:
                pass
            elif a[i] == a[j]:
                x = a[i]
                a.remove(x)
                k = k-1
                ex(k, a, j + 1)
        if j == k:
            print(a)
        ex(k, a, j + 1)

    a = arr.array("i", [1, 2, 1, 3, 4, 4, 7, 5])
    j = 0
    k = len(a)
    ex(k, a, j)


main()