class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        div1 = (len(nums1) + 1) // 2
        totall = len(nums1) + len(nums2)
        left_total = (totall + 1) // 2
        div2 = left_total - div1
        if nums1 == []:
            if totall % 2 == 0:
                return (nums2[div2] + nums2[div2 - 1]) / 2
            else:
                return nums2[div2 - 1]
        if nums2 == []:
            if totall % 2 == 0:
                return (nums1[div1] + nums1[div1 - 1]) / 2
            else:
                return nums1[div1 - 1]
        while 1:
            if div1 == 0:
                if nums1[0] < nums2[div2 - 1]:
                    div1 += 1
                    div2 -= 1
                else:
                    if div2 != len(nums2):
                        maxleft = nums2[div2 - 1]
                        minright = min(nums1[0], nums2[div2])
                        break
                    else:
                        maxleft = nums2[div2 - 1]
                        minright = nums1[0]
                        break
            elif div2 == 0:
                if nums2[0] < nums1[div1 - 1]:
                    div2 += 1
                    div1 -= 1
                else:
                    if div1 != len(nums1):
                        maxleft = nums1[div1 - 1]
                        minright = min(nums2[0], nums1[div1])
                        break
                    else:
                        maxleft = nums1[div1 - 1]
                        minright = nums2[0]
                        break
            elif div1 == len(nums1):
                if nums1[div1 - 1] > nums2[div2]:
                    div1 -= 1
                    div2 += 1
                else:
                    maxleft = max(nums1[div1 - 1], nums2[div2 - 1])
                    minright = nums2[div2]
                    break
            elif div2 == len(nums2):
                if nums2[div2 - 1] > nums1[div1]:
                    div2 -= 1
                    div1 += 1
                else:
                    maxleft = max(nums2[div2 - 1], nums1[div1 - 1])
                    minright = nums1[div1]
                    break
            else:
                if nums1[div1 - 1] <= nums2[div2] and nums2[div2 - 1] <= nums1[div1]:
                    maxleft = max(nums1[div1 - 1], nums2[div2 - 1])
                    minright = min(nums2[div2], nums1[div1])
                    break
                elif nums1[div1 - 1] > nums2[div2]:
                    div1 -= 1
                    div2 += 1
                elif nums2[div2 - 1] > nums1[div1]:
                    div1 += 1
                    div2 -= 1

        if totall % 2 == 0:
            return (maxleft + minright) / 2
        else:
            return maxleft

                

s=Solution()
print(s.findMedianSortedArrays([1,2,4],[3]))