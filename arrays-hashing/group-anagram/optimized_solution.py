from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grupos = defaultdict(list)
        for p in strs:
            chave = "".join(sorted(p))
            grupos[chave].append(p)
        return list(grupos.values())
