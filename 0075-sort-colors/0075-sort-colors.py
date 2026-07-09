class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for i in range(0,len(nums)-1):
        #     for  j in range(1,len(nums)):
        #         if i<j and nums[i]>nums[j]:
        #             nums[i],nums[j]=nums[j],nums[i]

        left=0
        right=len(nums)-1

        i=0

        while i<=right:
            if nums[i]==1:
                i+=1
            elif nums[i]==0:
                nums[left],nums[i]=nums[i],nums[left]
                left+=1
                i+=1
            else:
                nums[right],nums[i]=nums[i],nums[right]
                right-=1
            