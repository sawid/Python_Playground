from statistics import median

from pip import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedList = nums1 + nums2
        print(median(mergedList))

s1 = Solution()
inp1 = input()
inp2 = input()
s1.findMedianSortedArrays(inp1,inp2)