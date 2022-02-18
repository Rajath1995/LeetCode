class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1+nums2)
        mid_ele = (len(nums3)-1) / 2 
        if mid_ele%2==1 or mid_ele%2==0:
            mid = nums3[int(mid_ele)]
        elif mid_ele%2==1:
            mid = nums3[int(mid_ele)]
        else:
            mid = (nums3[int(mid_ele)] + nums3[int(mid_ele)+1])/2
        return mid
# https://leetcode.com/problems/median-of-two-sorted-arrays/
