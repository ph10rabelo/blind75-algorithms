from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        contagem = Counter(nums)
        tuplas = contagem.most_common(k)
        for i in tuplas:
          resultado, ocorrencia = i
          output.append(resultado)
        return output
