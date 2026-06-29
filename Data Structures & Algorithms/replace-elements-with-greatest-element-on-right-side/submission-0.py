'''
Reorder for greatest elements
length contraints
hash map
'''


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            max = i+1
            for j in range(i+1, len(arr)):
                if arr[j] > arr[max]:
                    max =j
            arr[i] = arr[max]
        arr[-1] = -1
        return arr
        