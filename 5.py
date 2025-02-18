class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 0
        for i in range(len(s)):
            if i == 0:
                right = 0
                left = -1
                curlen = 0
                while right < len(s) and s[right] == s[i]:
                    right += 1
                    curlen += 1
            elif i == len(s) - 1:
                left = i
                right = i + 1
                curlen = 0
                while left >= 0 and s[left] == s[i]:
                    left -= 1
                    curlen += 1
            else:
                left = i - 1
                right = i + 1
                curlen = 1
                flag = 0
                while left >= 0 and right < len(s) and ((s[left] == s[right] ) or (s[right] == s[i] and flag >= 0)):
                    if s[right] == s[i] and flag >= 0:
                        flag = 1
                        right += 1
                        curlen += 1
                    elif s[left] == s[right] :
                        left -= 1
                        right += 1
                        curlen += 2
                        flag = -1

            if curlen > maxlen:
                maxlen = curlen
                maxh = s[left+1: right]
        return maxh

s=Solution()
print(s.longestPalindrome("tattarrattat"))