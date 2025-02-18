class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left = 0
        right = height.length() - 1
        while left < right:
            val = (right - left) * min([height[left], height[right]])
            if val > res:
                res = val
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        
        return res