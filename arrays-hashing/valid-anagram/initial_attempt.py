def isAnagram(self, s: str, t: str) -> bool:
       conjunto1 = set()
       conjunto2 = set()
       l1 = list(s)
       l2 = list(t)
       if len(l1) == len(l2):
        for i in l1:
          conjunto1.add(i)
        for j in l2:
          conjunto2.add(j)
        if conjunto1 == conjunto2:
          return True
       return False
  #falhou em reconhecer strings como "bbcc" e "cccb" como nao sendo anagramas
