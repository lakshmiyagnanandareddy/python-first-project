import bisect
lis = [1, 22, 22, 33, 35, 40, 50]
print(bisect.bisect_right(lis, 22))
bisect.insort_right(lis, 22)
print(lis)


def grade(score, cutoff=[60, 70, 80, 90], grade='hFDCBA'):
    i = bisect.bisect_right(cutoff, score)
    return grade[i]


grades = [grade(score) for score in [10, 60, 77, 99, 88]]
print(grades)
