import pytest
from main import Triangulo

@pytest.fixture(scope='function')
def triangulo():
    return Triangulo()


@pytest.mark.parametrize("a, b, c, esperado", [
    # equilátero válido
    (5, 5, 5, "Triângulo Equilátero"),
    # isósceles válido
    (3, 3, 4, "Triângulo Isósceles"),
    # escaleno válido
    (3, 4, 5, "Triângulo Escaleno"),
    # isósceles válido com 3 permutações
    (3, 3, 4, "Triângulo Isósceles"),
    (3, 4, 3, "Triângulo Isósceles"),
    (4, 3, 3, "Triângulo Isósceles"),
    # lado 0 inválido
    (5, 5, 0, "Não é um triângulo válido"),
    # lado negativo inválido
    (-3, 4, 5, "Não é um triângulo válido"),
    # soma de dois lado = ao terceiro inválido
    (10, 5, 5, "Não é um triângulo válido"),
    (5, 10, 5, "Não é um triângulo válido"),
    (5, 5, 10, "Não é um triângulo válido"),
    # soma de dois lado < ao terceiro inválido
    (1, 2, 4, "Não é um triângulo válido"),
    (1, 4, 2, "Não é um triângulo válido"),
    (4, 1, 2, "Não é um triângulo válido"),
    (4, 2, 1, "Não é um triângulo válido"),
    (2, 4, 1, "Não é um triângulo válido"),
    (2, 1, 4, "Não é um triângulo válido"),
    # todos os valores = 0 inválido
    (0, 0, 0, "Não é um triângulo válido"),

])
def test_tipo(a,b,c,esperado,triangulo: Triangulo):
    ret = triangulo.triangulo_teste(a,b,c)
    assert ret == esperado