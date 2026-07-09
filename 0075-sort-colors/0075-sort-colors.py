class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)-1):
            for  j in range(1,len(nums)):
                if i<j and nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]