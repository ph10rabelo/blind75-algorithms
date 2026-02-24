class Solution:
    def isAnagram(self, s:str,t:str) -> bool:
      if len(s) != len(t):
        return False
      return sorted(s) == sorted(t)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      mae = []
      anagramas= set()
      for p in strs:
        if "".join(sorted(p)) in anagramas:
          for l in mae:
            if self.isAnagram(l[0],p):
              l.append(p)
        else:
          anagramas.add("".join(sorted(p)))
          mae.append([p])   
      return mae
