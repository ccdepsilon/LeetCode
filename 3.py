class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        cur_len = 0
        left = 0 
        right = 0
        while right < len(s):
            while s[right] in s[left : right]:
                if left == right:
                    break
                left += 1
                
            
            right += 1
            cur_len = right - left
            if cur_len > max_len:
                max_len = cur_len
        return max_len
            
s=Solution()
s.lengthOfLongestSubstring('bbbbbbbb')
