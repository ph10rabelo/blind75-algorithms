class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 0
        output =[]
        product1 = 1
        product2 = 1
        while count < len(nums): 
            for j in range (count):
                product2 *= nums[j]
            for i in range(count+1, len(nums)):
                product1 *= nums[i]
            output.insert(count,product1*product2)
            count +=1
            product1 = 1
            product2 = 1
        return output
