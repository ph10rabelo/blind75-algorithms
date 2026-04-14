class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lista = collections.defaultdict(set)
        res = []
        for i in nums:
            lista[i].add(1)
        for chave in lista:
            for chave2 in lista:
                if chave-chave2 == 1:
                    res.append(chave)
        if not nums:
            return 0
        return len(res)+1
