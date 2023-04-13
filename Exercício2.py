N1 = 0
N2 = 1
Soma = 0

Termo = int(input("Digite um valor para verificar: "))

while Soma < Termo:
  Soma = N1 + N2
  N1 = N2
  N2 = Soma

if Soma == Termo:
  print("O número faz parte da sequencia de Fibonacci")
else:
  print("O número não faz parte da sequencia de Fibonacci")