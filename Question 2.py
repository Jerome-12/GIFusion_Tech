class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency:  # if a number already in the list, it increase by 1
                frequency[num] += 1
            else:
                frequency[num] = 1
        nums.sort(key=lambda x: (frequency[x], -x)) # list is sorted by the least frequent number in the list by ascending order
        return nums
        