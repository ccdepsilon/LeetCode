class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        dis = (numRows - 1) * 2
        res=[]
        if dis == 0:
            return s
        for i in range(numRows):
            id = i
            if i == 0:
                while id < len(s):
                    res.append(s[id])
                    id = id + dis
            elif i == numRows - 1:
                while id < len(s):
                    res.append(s[id])
                    id += dis
            else:
                flag = 0
                dif1 = dis - i * 2
                dif2 = dis - dif1
                while id < len(s):
                    res.append(s[id])
                    if flag == 0:
                        id += dif1
                        flag = 1
                    else:
                        id += dif2
                        flag = 0
        return ''.join(res)
        
s=Solution()
print(s.convert('PAYPALISHIRING',4))