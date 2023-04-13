SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53
Total = SP + RJ + MG + ES + Outros
Porcentagem = 0

Estado = str(input("Escolha o estado para saber a porcentagem: "))

if Estado in ['SP', 'RJ', 'MG', 'ES', 'Outros']:
  if Estado == 'SP':
    Porcentagem = SP * 100 / Total
    print(f'A porcentagem de SP é {Porcentagem:.2f}%')
  elif Estado == 'RJ':
    Porcentagem = RJ * 100 / Total
    print(f'A porcentagem de SP é {Porcentagem:.2f}%')
  elif Estado == 'MG':
    Porcentagem = MG * 100 / Total
    print(f'A porcentagem de SP é {Porcentagem:.2f}%')
  elif Estado == 'ES':
    Porcentagem = ES * 100 / Total
    print(f'A porcentagem de SP é {Porcentagem:.2f}%')
  elif Estado == 'Outros':
    Porcentagem = Outros * 100 / Total
    print(f'A porcentagem de SP é {Porcentagem:.2f}%')