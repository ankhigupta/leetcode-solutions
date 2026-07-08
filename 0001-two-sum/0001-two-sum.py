class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # freq={}
        # for i in range(len(nums)):
        #     comple=target-nums[i]
        #     if nums[i] not in  freq:
        #         freq[comple]=i
        #     else:
        #         return [freq[nums[i]],i]



        # freq={}
        # for i in range(len(nums)-1):
        #     if nums[i]+nums[i+1]==target:
        #         freq[i]=


        freq={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in freq:
                return freq[rem],i
            freq[nums[i]]=i