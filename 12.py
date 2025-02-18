class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        a = []
        res = ""
        for i in range(4):
            a.append(num % 10)
            num = num // 10
        for i in range(a[3]):
            res += 'M'

        if a[2] == 4:
            res += "CD"
        elif a[2] == 9:
            res += "CM"
        elif a[2] >= 5:
            res += "D"
            for i in range(a[2] - 5):
                res += "C"
        else:
            for i in range(a[2]):
                res += "C"
        
        if a[1] == 4:
            res += "XL"
        elif a[1] == 9:
            res += "XC"
        elif a[1] >= 5:
            res += "L"
            for i in range(a[1] - 5):
                res += "X"
        else:
            for i in range(a[1]):
                res += "X"

        if a[0] == 4:
            res += "IV"
        elif a[0] == 9:
            res += "IX"
        elif a[0] >= 5:
            res += "V"
            for i in range(a[0] - 5):
                res += "I"
        else:
            for i in range(a[0]):
                res += "I"
        
        return res