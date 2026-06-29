'''
constraints:
var = nums, val
remove n val in nums
nums in any order
(num elements in nums != val) = k
k values reordered to start

solution:
k will be a counter
arr = list stored in nums
conditional to check if val or not, then updates counter.
for loop to add elements and use conditional

'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in range(len(nums)):
            if nums[num] != val:
                nums[k] = nums[num]
                k+=1
            
        return k


        