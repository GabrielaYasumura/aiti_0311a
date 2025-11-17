from funcoes import *

def test_email_valido():
    assert email_valido("exemplo@dominio.com") == True
    assert email_valido("exemplo.com") == False
    assert email_valido("exemplo@dominio") == False

def test_dividir():
    assert dividir(4,2) == 2
    assert dividir(1,0) == None