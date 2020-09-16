# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            result = target - nums[i]
            for j in nums[i + 1:]:
                if result == j:
                    two_index = nums[i + 1:].index(j) + i + 1
                    return i, two_index


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ones_index = -1
        for i in range(len(nums)):
            result = target - nums[i]
            if result in nums[i + 1:]:
                ones_index = nums[i + 1:].index(result) + i + 1
                break
        if ones_index > 0:
            return i, ones_index
        else:
            return []


class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index, value in enumerate(nums):
            nums_dict[value] = index
        for index, value in enumerate(nums):
            ones = target - value
            ones_index = nums_dict.get(ones)
            if ones_index is not None and index != ones_index:
                return index, ones_index





if __name__ == '__main__':
    x = Solution()
    print(x.twoSum([1, 1], 2))
