import random
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # With Bubble Sort
        # SC=O(1), TC=O(N^2),omega(N)

        # n=len(nums)

        # for i in range(n):
        #     isSwap=False
        #     for j in range(n-i-1):
        #         if nums[j]>nums[j+1]:
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        #             isSwap=True

        #     if not isSwap:
        #         break

        # return nums

        # With Insertion Sort
        # SC=O(1), TC=O(N^2),omega(N)

        # n=len(nums)
        # for i in range(1,n):
        #     key=nums[i]
        #     j=i-1

        #     while j>=0 and nums[j]>key:
        #         nums[j+1]=nums[j]
        #         j-=1
        #     nums[j+1]=key

        # return nums


        # With Selection Sort
        # SC=O(1), TC=O(N^2),omega(N^2)

        # n=len(nums)

        # for i in range(n):
        #     minm = nums[i]
        #     ind=i
        #     for j in range(i+1,n):
        #         while nums[j]<minm:
        #             minm=nums[j]
        #             ind=j

        #     nums[i],nums[ind]=nums[ind],nums[i]

        # return nums



        # With Merge Sort
        # SC=O(N), TC=O(N log N),omega(N log N), theta(N log N)

        # if len(nums)==1:
        #     return nums

        # mid=len(nums)//2
        # list1=self.sortArray(nums[:mid])
        # list2=self.sortArray(nums[mid:])

        # return self.merge(list1,list2)

    # def merge(self,l1,l2):
    #     i=0
    #     j=0
    #     res=[]

    #     while i<len(l1) and j<len(l2):
    #         if l1[i]>l2[j]:
    #             res.append(l2[j])
    #             j+=1
    #         else:
    #             res.append(l1[i])
    #             i+=1
        
    #     while i<len(l1):
    #         res.append(l1[i])
    #         i+=1

    #     while j<len(l2):
    #         res.append(l2[j])
    #         j+=1
        
    #     return res
        


        # With Quick Sort
        # SC=O(1), TC=O(N^2),omega(N log N)

        self.quick_sort(nums,0,len(nums)-1)

        return nums

    def quick_sort(self,nums,low,high):
        if low<high:

            index_j=self.partition(nums,low,high)
            self.quick_sort(nums,low,index_j-1)
            self.quick_sort(nums,index_j+1,high)


    def partition(self,nums,low,high):
        pivot_index = random.randint(low, high)
        nums[low], nums[pivot_index] = nums[pivot_index], nums[low]

        pivot=nums[low]
        i=low+1
        j=high

        while True:

            while i<=j and nums[i]<pivot:
                i+=1

            while i<=j and nums[j]>pivot:
                j-=1

            if i<=j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
            else:
                break

        nums[j],nums[low]=nums[low],nums[j]

        return j
            
