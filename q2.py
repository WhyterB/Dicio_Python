credenciais_clientes = {
    'alice123': {'username': 'alice123',
                 'password': 'alic3P@ssw0rd',
                 'status': 'active', },
    'bob456': {'username': 'bob456',
               'password': 'bobP@ssord!',
                'status': 'inactive', },
    'charlie789': {'username': 'charlie789',
                   'password': 'Ch@rçoeP@ss9',
                   'status': 'active',}
}

alerta = 'Enviar alerta!' if 'inactive' in credenciais_clientes['bob456'] .values() else "Sem alerta!"
print(alerta)