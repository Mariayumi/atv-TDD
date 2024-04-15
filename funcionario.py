from enum import Enum

class Cargo(Enum):
    DESENVOLVEDOR = 1
    DBA = 2
    TESTADOR = 3
    GERENTE = 4

class Funcionario:
    def __init__(self, nome, email, salario_base, cargo):
        self.nome = nome
        self.email = email
        self.salario_base = salario_base
        self.cargo = cargo

    def calcular_salario_liquido(self):
        if self.cargo == Cargo.DESENVOLVEDOR:
            if self.salario_base >= 3000:
                return self.salario_base * 0.8
            else:
                return self.salario_base * 0.9
        elif self.cargo == Cargo.DBA or self.cargo == Cargo.TESTADOR:
            if self.salario_base >= 2000:
                return self.salario_base * 0.75
            else:
                return self.salario_base * 0.85
        elif self.cargo == Cargo.GERENTE:
            if self.salario_base >= 5000:
                return self.salario_base * 0.7
            else:
                return self.salario_base * 0.8