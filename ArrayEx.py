import array as arr


def main():

    def removes_duplicate_elements_in_array(array_list, array_list_index):
        if array_list_index == len(array_list):
            return array_list
        elif array_list_index < len(array_list):
            for i in range(len(array_list)):
                if i == array_list_index:
                    pass
                elif array_list[i] == array_list[array_list_index]:
                    removing_element = array_list[i]
                    array_list.remove(removing_element)
                    return removes_duplicate_elements_in_array(array_list, array_list_index)

            return removes_duplicate_elements_in_array(array_list, array_list_index + 1)

    array_list = arr.array("i", [1, 2, 1, 3, 4, 4, 7, 5])
    array_list_index = 0
    array_list = removes_duplicate_elements_in_array(array_list, array_list_index)
    print(array_list)


def find_number_of_occurrence():

    def find_number_of_occurrence(array_list, array_list_index):
        if array_list_index <= len(array_list)-1:
            num_of_occurrence = 0
            for i in range(len(array_list)):
                if array_list[i] == array_list[array_list_index]:
                    num_of_occurrence = num_of_occurrence+1
            print(array_list[array_list_index], "is occurred :", num_of_occurrence, "times")

            return find_number_of_occurrence(array_list, array_list_index + 1)

    array_list = arr.array("i", [1, 3, 4, 6, 3, 1, 1])
    array_list_index = 0
    find_number_of_occurrence(array_list, array_list_index)


def remove():
    import array as arr
    array_list = arr.array("i", [1, 2, 3, 4, 5, 3, 6])
    array_list.remove(3)
    print(array_list)


def find_list_contains_any_duplicate_element():

    def find_list_contain_any_duplicate_element(array_list, array_list_index):
        if array_list_index == len(array_list):
            return True
        elif array_list_index < len(array_list):
            for i in range(len(array_list)):
                if i == array_list_index:
                    pass
                elif array_list[i] == array_list[array_list_index]:
                    return False

            return find_list_contain_any_duplicate_element(array_list, array_list_index + 1)

        array_list = arr.array("i", [1, 2, 3, 4, 5])
        array_list_index = 0
        print((find_list_contain_any_duplicate_element(array_list, array_list_index)))


def find_first_repeating_number():

    def find_first_repeating_number(array_list, array_list_index):
        if array_list_index == (len(array_list)):
            return -1

        elif array_list_index < len(array_list):
            for i in range(len(array_list)):
                if i == array_list_index:
                    pass
                elif array_list[i] == array_list[array_list_index]:
                    return array_list[i], "is the first repeating value"

            return find_first_repeating_number(array_list, array_list_index + 1)

    array_list = arr.array("i", [1, 2, 3, 4, 5])
    array_list_index = 0
    print((find_first_repeating_number(array_list, array_list_index)))


def finding_sequence():
    import array as arr
    array_list = arr.array("i", [10, 14, 15, 16, 18, 20])
    array_list_index = 0
    for missing_number in range(min(array_list), max(array_list)):
        if missing_number == array_list[array_list_index]:
            array_list_index = array_list_index+1
            pass
        else:
            print(missing_number, "", end="")


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

def mama():
    def tips_none(lst, fn=lambda x: x):
      return all(not fn(x) for x in lst)

    print(tips_none([0, 1, 2, 0], lambda x: x >= 2 ))
    print(tips_none([0, 0, 0]))


finding_sequence()