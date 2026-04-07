class Solution:


    def encode(self, strs: List[str]) -> str:
        resultado = " "
        for i in strs:
            resultado += " " +i
        return resultado
    def decode(self, s: str) -> List[str]:
        if s == "  ":
            return [""]
        resultado = s.split()
        return resultado
