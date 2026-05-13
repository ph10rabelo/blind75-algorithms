def maxProfit(self,prices:List[int])->int:
  maxLucro = 0
  for i in range(len(prices)):
    comprar = prices[i]
    for j in range(i+1,len(prices)):
      vender = prices[j]
      maxLucro = max(maxLucro, vender - comprar)
  return maxLucro
