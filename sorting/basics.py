"""
bubble sort
"""
unsorted_list = [1, 5, 2, 4, 3]
for i in range(len(unsorted_list)-1):
    if unsorted_list[i] > unsorted_list[i+1]:
        count = unsorted_list[i]
        unsorted_list[i] = unsorted_list[i+1]
        unsorted_list[i+1] = count

for i in range(len(unsorted_list)-1):
    if unsorted_list[len(unsorted_list) - (i+1)] < unsorted_list[len(unsorted_list) - (i + 2)]:
        count = unsorted_list[len(unsorted_list) - (i+1)]
        unsorted_list[len(unsorted_list) - (i+1)] = unsorted_list[len(unsorted_list) - (i + 2)]
        unsorted_list[len(unsorted_list) - (i + 2)] = count

print("bubble sort :")
print(unsorted_list)


"""
insertion sort
"""

unsorted_list = [5, 3, 1, 8, 2]
for i in range(len(unsorted_list)):

    for j in range(i):
        if j == i:
            break
        elif unsorted_list[i - j] < unsorted_list[i - (j + 1)]:
            count = unsorted_list[i - j]
            unsorted_list[i - j] = unsorted_list[i - (j + 1)]
            unsorted_list[i - (j + 1)] = count

print("insertion sort :")
print(unsorted_list)


"""
Selection sort
"""
unsorted_list = [40, 23, 22, 10, 44, 2, 1, 50]

unsorted_list.index(min(unsorted_list))
unsorted_list[unsorted_list.index(min(unsorted_list))], unsorted_list[0] = unsorted_list[0], unsorted_list[unsorted_list.index(min(unsorted_list))]
for j in range(len(unsorted_list)-1):
    swap = max(unsorted_list)
    for i in range(len(unsorted_list)):
        if unsorted_list[j] < swap:
            if swap > unsorted_list[i] > unsorted_list[j]:
                swap = unsorted_list[i]
    unsorted_list[unsorted_list.index(swap)], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[unsorted_list.index(swap)]
print("selection sort :")
print(unsorted_list)


"""
merge sort
"""


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                arr[k] = right[j]
                j += 1
            else:
                arr[k] = left[i]
                i += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [10, 33, 12, 46, 23, 78, 22, 43]
merge_sort(arr)

print("merge sort :")
for i in range(len(arr)):
    print(arr[i], end=" ")
print()


"""
Shell sort
"""


def shell_sort(arr):
    first_value = 0
    second_value = len(arr)//2

    def first_interval(arr, first_value, second_value):
        if len(arr) <= second_value:
            return arr
        elif arr[first_value] > arr[second_value]:
            arr[first_value], arr[second_value] = arr[second_value], arr[first_value]
            first_interval(arr, first_value+1, second_value+1)
        else:
            first_interval(arr, first_value + 1, second_value + 1)

    first_interval(arr, first_value, second_value)

    def second_interval(arr, first_value, second_value):

         def first_subset(arr, first_value, second_value):
            for i in range(len(arr)//2):
                for i in range(len(arr)//2):
                    if first_value <= len(arr) >= second_value:
                        if arr[first_value] > arr[second_value] and first_value < second_value:
                            arr[first_value], arr[second_value] = arr[second_value], arr[first_value]
                            second_value += 2
                        else:
                            second_value += 2
                first_value +=2
                second_value = 0
            return arr

         first_subset(arr, first_value=0, second_value=0)

         def second_subset(arr, first_value, second_value):
            for i in range(len(arr)//2):
                for i in range(len(arr)//2):
                    if first_value <= len(arr) >= second_value:
                        if arr[first_value] > arr[second_value] and first_value < second_value:
                            arr[first_value], arr[second_value] = arr[second_value], arr[first_value]
                            second_value += 2
                        else:
                            second_value += 2
                first_value += 2
                second_value = 1
            return arr

         second_subset(arr, first_value=1, second_value=1)

    second_interval(arr, first_value, second_value)

    for i in range(len(arr)):
        for j in range(i):
            if i == j:
                j += 1
            elif arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                j +=1
            else:
                j += 1
        i += 1


arr = [70, 100, 30, 20, 37, 60, 80, 4]
shell_sort(arr)

print("shell sort :")
for i in range(len(arr)):
    print(arr[i], end=" ")
print()
"""
quick sort
"""


def arrange(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] < pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort(arr, low, high):
    if low < high:
        pi = arrange(arr, low, high)

        quick_sort(arr, low, pi-1)

        quick_sort(arr, pi+1, high)


arr = [10, 3, 30, 40, 15, 20, 18]
size = len(arr)
quick_sort(arr, 0, size-1)
print("quick sort :", arr)


"""
linear search
"""


def linear_search(arr, search_number):
    for i in range(len(arr)):
        if arr[i] == search_number:
            return print(search_number, "is in the index of", i, " in the array.")
    print(search_number, "is not found in the array.")


arr = [1, 90, 20, 30, 22, 50, 100]
search_number = 22
linear_search(arr, search_number)


"""
binary search
"""


def binary_search(arr, search_number, low, high):
    mid = low + (high - low)//2

    if arr[mid] == search_number:
        return mid

    elif arr[mid] < search_number:
        low = mid+1
        return binary_search(arr, search_number, low, high)
    elif arr[mid] > search_number:
        high = mid - 1
        return binary_search(arr, search_number, low, high)


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
search_number = 30

print(binary_search(arr, search_number, low=0, high=len(arr)-1))
