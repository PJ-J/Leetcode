class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for i, num in enumerate(nums):
            if target-num in dict_.keys():
                return [dict_[target-num], i]
            else:
                dict_[num] = i