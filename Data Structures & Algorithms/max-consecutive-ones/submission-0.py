class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        highest = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if count> highest:
                    highest = count
            if nums[i]==0:
                count = 0
            

        return highest
        