valor_produto = float(input('Digite o preço do produto: R$'))
desconto = 0.05 * valor_produto
print(f'O seu produto custa {valor_produto} com 5% de desconto o seu produto passará a custar: R${valor_produto - desconto:.2f}')
