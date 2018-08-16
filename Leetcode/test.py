class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B=[]
        for i in range(len(A[0])):
            temp=[]
            for j in range(len(A)):
                temp.append(A[i][j])
            B.append(temp)
        return B
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=0
        string=''.join(str(i)for i in nums)
        for i in string:
            print(i)
        for i in string.split('0'):
            if max<len(i):
                max=len(i)
        return max
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        nums=sorted(list(set(nums)))
        print(nums)
        for i in range(len(nums)-1):
            if nums[i]+1 != nums[i]:
                result.append(nums[i])
        return result
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        print(nums)
        if nums[-1]<0:
            return nums[-1]*nums[-2]*nums[-3]
        elif nums[-2]<0:
            return nums[0]*nums[1]*nums[-1]
        elif nums[-3]<0:
            return nums[0]*nums[1]*nums[-1]
        else:
            return nums[-1]*nums[-2]*nums[-3]
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.append(nums2)
        nums1=sorted(nums1)
        length=len(nums1)
        if length%2:
            return nums1[length//2]
        else:
            return (nums1[length//2]+nums1[length//2-1])/2


    def removeDuplicates(self, A):
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp=[nums[i],nums[left],nums[right]]
                if nums[i] + nums[left] + nums[right]>0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right]<0:
                    left += 1
                else:
                    temp = [nums[i], nums[left], nums[right]]
                    if temp not in result:
                        result.append(temp)
                        left+=1
                    else:
                        left+=1
        return result
# print(Solution().twoSum([3,2,4],6))
# print(Solution().transpose([[1,2,3],[4,5,6]]))
# print(Solution().findMaxConsecutiveOnes([1,0,1,1,0,1]))
# print(Solution().maximumProduct([722,634,-504,-379,163,-613,-842,-578,750,951,-158,30,-238,-392,-487,-797,-157,-374,999,-5,-521,-879,-858,382,626,803,-347,903,-205,57,-342,186,-736,17,83,726,-960,343,-984,937,-758,-122,577,-595,-544,-559,903,-183,192,825,368,-674,57,-959,884,29,-681,-339,582,969,-95,-455,-275,205,-548,79,258,35,233,203,20,-936,878,-868,-458,-882,867,-664,-892,-687,322,844,-745,447,-909,-586,69,-88,88,445,-553,-666,130,-640,-918,-7,-420,-368,250,-786]))
# print(Solution().findMedianSortedArrays([1,3],[2]))
# print(Solution().removeDuplicates([1,1,2,3,3,4]))
# print(Solution().threeSum([-2,0,1,1,2]))






































