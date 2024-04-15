import pytest
from person import DAO, Person, Email

@pytest.fixture
def dao():
    return DAO()

def test_save_valid_person(dao):
    person = Person(1, "John Doe", 30)
    person.email.append(Email(1, "johndoe@example.com"))
    dao.save(person)
    assert len(dao.persons) == 1

def test_save_invalid_person(dao):
    person = Person(2, "John", 300)
    dao.save(person)
    assert len(dao.persons) == 0

def test_save_person_without_email(dao):
    person = Person(3, "Jane Doe", 25)
    dao.save(person)
    assert len(dao.persons) == 0

def test_save_person_with_invalid_email(dao):
    person = Person(4, "Alice Wonderland", 35)
    person.email.append(Email(1, "invalidemail.com"))
    dao.save(person)
    assert len(dao.persons) == 0

def test_save_person_with_valid_email(dao):
    person = Person(5, "Bob Builder", 40)
    person.email.append(Email(1, "bob@example.com"))
    dao.save(person)
    assert len(dao.persons) == 1
