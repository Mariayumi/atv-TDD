class Triangulo: 
    def triangulo_teste(self, a, b, c):
        # Verifica se um dos lados é negativo ou zero
        if a <= 0 or b <= 0 or c <= 0:
            return "Não é um triângulo válido"
        # Verifica se a soma de dois lado é igual ou menos ao terceiro
        elif a + b <= c or a + c <= b or b + c <= a:
            return "Não é um triângulo válido"

        if a == b == c:
            return "Triângulo Equilátero"
        elif a == b or a == c or b == c:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
        
