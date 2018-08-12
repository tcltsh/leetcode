import os, sys

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        totallen = len(nums1) + len(nums2)
        if totallen == 0:
            return 0.0
        maxValue = None
        if len(nums1) > 0:
            maxValue = nums1[len(nums1)-1] if maxValue is None else max(maxValue, nums1[len(nums1) - 1])
        if len(nums2) > 0:
            maxValue = nums2[len(nums2)-1] if maxValue is None else max(maxValue, nums2[len(nums2) - 1])
        nums1.append(maxValue + 1)
        nums2.append(maxValue + 1)

        f1 = f2 = 0
        cnt = totallen / 2
        lastLow = None
        while cnt > 0:
            if nums1[f1] < nums2[f2]:
                lastLow = nums1[f1]
                f1 +=1
            else:
                lastLow = nums2[f2]
                f2 +=1
            cnt -= 1
        if (totallen) % 2 == 0:
            return float(lastLow + min(nums1[f1], nums2[f2]))/2
        else:
            return float(min(nums1[f1], nums2[f2]))

if __name__ == "__main__":
    s = Solution()
    print s.findMedianSortedArrays([1, 3], [2])
    print s.findMedianSortedArrays([1, 2], [3, 4])
    print s.findMedianSortedArrays([], [1])
