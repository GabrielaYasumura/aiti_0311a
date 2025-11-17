def somar(a,b):
    return a + b

def comprimento(lista):
    return len(lista)



def test_somar():
    assert somar(1,2) == 3

def test_comprimento():
    assert comprimento([1,2,3,4,5]) == 5
