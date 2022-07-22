"""
Write a Python program to find three integers which gives the sum of zero in a given array of integers using Binary Search (bisect)
"""
import bisect
import collections
def three_sums(nums):
    tripets = []
    num_freq = collections.Counter(nums)
    nums = sorted(num_freq)
    max_num = nums[-1]
    for i, v in enumerate(nums):
        if num_freq[v] >= 2:
            complement = -2 * v
            if complement in nums:
                tripets.append([v, complement, v])
        if num_freq[v] > 0:
            two_sum = -v
            lb = bisect.bisect_left(nums, two_sum - max_num, i+1)
            ub = bisect.bisect(nums, two_sum//2, lb)
            for u in nums[lb: ub]:
                complement = two_sum - u
                if complement in nums and u != complement:
                    tripets.append([v, u, complement])
    return tripets


nums = [-20, 0, 20, 40, -20, -40, 80]
result = three_sums(nums)
print(result)
