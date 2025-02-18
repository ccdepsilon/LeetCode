class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {
            'I':             1,
            'V':             5,
            'X':             10,
            'L':             50,
            'C':             100,
            'D':             500,
            'M':             1000
        }
        s = s[::-1]
        res = 0
        pre = ''
        for c in s:
            res += hash[c]
            if res not in hash.values():
                if hash[pre] / hash[c] == 5 or hash[pre] / hash[c] == 10:
                    res -= hash[c] * 2
            pre = c

        return res