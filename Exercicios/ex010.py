#input do dinheiro total 
dinheiro_total = float(input('Quanto você possui na carteira: R$'))

dolares = dinheiro_total / 5.26

print(f'Você pode comprar com R${dinheiro_total:.2f} é : US${dolares:.2f} ')