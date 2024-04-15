from typing import List, Tuple
import re

class Person:
    def __init__(self, id: int, nome: str, idade) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.email: List[Email] = []
        pass

class Email:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        pass

class DAO:
    def __init__(self) -> None:
        self.persons = []

    def save(self, person:Person):
        valido = self.isValidToInclude(person)
        if len(valido) == 0:
            self.persons.append(person)

    def isValidToInclude(self, person:Person):
        erros = []
        if not self.is_name_valid(person.nome):
            erros.append("O nome deve ser completo")
        if not self.is_idade_valid(person.idade):
            erros.append("A idade deve ser entre 1 à 200")
        if not self.person_has_email(person.email):
            erros.append("Você deve enviar pelo menos um email")
        for email in person.email:
            if not self.is_email_valid(email.name):
                erros.append("O email deve estar no formato _____@____._____")
        print(erros)
        return erros

    def is_name_valid(self, nome:str):
        nome_completo = nome.split(" ")
        digito = bool(re.search(r'\d', nome))
        if len(nome_completo) >= 2 and not digito:
            return True
        else: 
            return False
        
    def is_idade_valid(self, idade:int) -> bool:
        if 1 < idade <= 200:
            return True
        else:
            return False
        
    def person_has_email(self, emails: List[Email]):
        if len(emails) >= 1:
            return True
        else:
            return False
        
    def is_email_valid(self, email:str) -> Tuple[bool, None]:
        padrao = r"^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$"
        return re.match(padrao, email) is not None
