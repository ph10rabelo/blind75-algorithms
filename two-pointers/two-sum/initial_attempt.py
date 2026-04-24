class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       memoria = []
       aux = {}
       for i in nums:
        primeiro = i
        for j in nums:
            if j == primeiro or j == primeiro*-1:
                complemento = (primeiro+j)*-1
                if memoria
                memoria.append([i,j,complemento])
        return memoria
