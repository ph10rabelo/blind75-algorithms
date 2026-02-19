class Solution:
  def twoSum(self, nums:list[int], target:int)-> list[int]:
    memoria = {}
    for i, n in enumerate[num]:
      complemento = target - n
      if complemento in memoria:
        return [memoria[complemento],i]
      memoria[n] = i
