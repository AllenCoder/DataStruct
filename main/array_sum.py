class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        iterate = range(length)
        for a in iterate:
            for b in range(a+1, length):

                if nums[a] + nums[b] == target:
                    return [a, b]


nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target))
