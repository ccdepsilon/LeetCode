class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x1 = abs(x)
        x2 = x1
        res = 0
        i = 0
        while x2 != 0:
            i += 1
            x2 = x2 // 10
        i -= 1
        while x1 != 0:
            temp = x1 % 10
            res += temp * (10 ** i)
            x1 = x1 // 10
            i -= 1
        res = res if x > 0 else -res
        if res > (2 ** 31 - 1) or res < (-2 ** 31):
            return 0
        else:
            return res

s=Solution()
print(s.reverse(-123))