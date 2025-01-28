largura = float(input('Qual a largura da parede?'))
altura = float(input('Qual a altura da parede?'))

área = largura * altura 
qtd_total = área / 2 

print(f'A dimensão da sua parede é {largura:.2f}m x {altura:.2f}m com área de {área:.2f}m²\nA quantidade total para pinta-la é {qtd_total:.1f}l de tinta')
