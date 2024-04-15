import pytest
from funcionario import Funcionario, Cargo

@pytest.fixture
def desenvolvedor():
    return Funcionario("João", "joao@example.com", 3500, Cargo.DESENVOLVEDOR)

@pytest.fixture
def dba():
    return Funcionario("Pedro", "pedro@example.com", 2500, Cargo.DBA)

@pytest.fixture
def testador():
    return Funcionario("Carlos", "carlos@example.com", 2500, Cargo.TESTADOR)

@pytest.fixture
def gerente():
    return Funcionario("José", "jose@example.com", 6000, Cargo.GERENTE)

def test_calcula_salario_desenvolvedor_maior_ou_igual_3000(desenvolvedor):
    assert desenvolvedor.calcular_salario_liquido() == 2800.0

def test_calcula_salario_desenvolvedor_menor_que_3000():
    desenvolvedor = Funcionario("Maria", "maria@example.com", 2500, Cargo.DESENVOLVEDOR)
    assert desenvolvedor.calcular_salario_liquido() == 2250.0

def test_calcula_salario_dba_maior_ou_igual_2000(dba):
    assert dba.calcular_salario_liquido() == 1875.0

def test_calcula_salario_dba_menor_que_2000():
    dba = Funcionario("Ana", "ana@example.com", 1500, Cargo.DBA)
    assert dba.calcular_salario_liquido() == 1275.0

def test_calcula_salario_testador_maior_ou_igual_2000(testador):
    assert testador.calcular_salario_liquido() == 1875.0

def test_calcula_salario_testador_menor_que_2000():
    testador = Funcionario("Amanda", "amanda@example.com", 1500, Cargo.TESTADOR)
    assert testador.calcular_salario_liquido() == 1275.0

def test_calcula_salario_gerente_maior_ou_igual_5000(gerente):
    assert gerente.calcular_salario_liquido() == 4200.0

def test_calcula_salario_gerente_menor_que_5000():
    gerente = Funcionario("Patrícia", "patricia@example.com", 4000, Cargo.GERENTE)
    assert gerente.calcular_salario_liquido() == 3200.0