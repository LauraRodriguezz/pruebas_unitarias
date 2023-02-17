from funciones import sumar, isitPrime


def test_sumar():
    assert sumar(2,4) == 6
    assert sumar(-2,2) == 0
    
    assert sumar(2,2) == 4
    

def test_es_primo():
    assert isitPrime(7) is True
    assert isitPrime(4) is False
    
    