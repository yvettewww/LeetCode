# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# version1 -> accepted
# beats -> 84%
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}

        for i in range(len(nums)):
            if nums[i] * 2 == target:
                try:
                    return ([dict[nums[i]], i])
                except KeyError:
                    pass
            dict[nums[i]] = i
            try:
                if dict[target - nums[i]] != i:
                    return ([dict[target - nums[i]], i])
            except KeyError:
                continue


if __name__ == '__main__':
    print(Solution().twoSum([3, 3], 6))