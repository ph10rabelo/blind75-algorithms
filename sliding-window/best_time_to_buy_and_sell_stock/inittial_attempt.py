class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimo = float('inf')
        maximo = 0
        for i, valor in enumerate(prices): 
            minimo = min(minimo,valor)
            maximo = max(maximo,valor)
            
        if prices == sorted(prices, reverse=True):
            return 0
