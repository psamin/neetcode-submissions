class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        anslen = n*2
        ans = [0]*anslen
        for i in range(n):
            ans[i] = nums[i]
        for i in range(n,2*n):
            ans[i] = nums[i-n]

        return ans
        