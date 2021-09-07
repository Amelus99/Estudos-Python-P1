from decimal import Decimal
valor = 1.91
valorD = Decimal('1.91')

print(valor)
print("{:.10f}".format(valor))
print("{:.30f}".format(valor))

print()

print(valorD)
print("{:.10f}".format(valorD))
print("{:.30f}".format(valorD))
