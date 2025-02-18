class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = {}
        for i, n in enumerate(nums):
            if n in temp.keys():
                temp[n].append(i)
            else:
                temp[n] = [i]
        nums.sort()
        left = 0
        right = len(nums) - 1
        while nums[left] + nums[right] != target:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
        if nums[left] == nums[right]:
            return [temp[nums[left]][0], temp[nums[right]][1]]
        return [temp[nums[left]][0], temp[nums[right]][0]]