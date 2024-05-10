Pessoa = {
    'Nome': 'Matheus Borin',
    'Idade': '17',
    'Cidade': 'Campo Largo',
    'Aniversario': '22/07',
    'Colegio': 'CESF - Sagrada Familia'
}

Pessoa['Nome'] = 'Matheus Borin Soares'
Pessoa['Profissão'] = 'Estudante'
remover_valor = Pessoa.pop('Cidade')

print(remover_valor)
print(Pessoa)