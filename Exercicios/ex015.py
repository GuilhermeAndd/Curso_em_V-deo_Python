km = float(input('Qual a quantidade percorrida?(Em km): '))
dias = int(input('Quantos dias ele foi alugado? '))
pagamento = 60 * dias + (0.15 * km)
print(f'A quantidade total a pagar é R${pagamento:.2f}')