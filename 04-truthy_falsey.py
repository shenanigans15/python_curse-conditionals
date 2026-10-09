# Truthy (verdaderos)
print(bool(True))
print(bool(1))  # Los numeros distintos de 0 son verdaderos
print(bool(123))
print(bool(1.1))
print(bool(-1))
print(bool(1j))
print(bool("Hola"))  # Un string con valor es verdadero
print(bool([1, 2, 3]))
print(bool((1, 2, 3)))
print(bool({1, 2, 3}))


# Falsey (falsos)
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))
