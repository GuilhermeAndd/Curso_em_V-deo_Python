def solicitar_data_nascimento():
    data_nascimento = input('Qual é a sua data de nascimento(dd-mm-aaaa)? ')
    return data_nascimento

data_nascimento = solicitar_data_nascimento()
print('Sua data de nascimento é:', data_nascimento)
