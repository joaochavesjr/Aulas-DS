def pode_acessar(cargo, dia_semana):
    dias_uteis = ["segunda-feira", "terça-feira", "quarta-feira",
                   "quinta-feira", "sexta-feira"]
    acesso_liberado = False
    # Gerentes têm acesso irrestrito
    if cargo.lower() == "gerente":
        acesso_liberado = True
    # Analistas têm acesso somente em dias úteis
    elif cargo.lower() == "analista" and dia_semana.lower() in dias_uteis:
        acesso_liberado = True
    # Estagiários têm acesso somente em dias úteis
    elif cargo.lower() == "estagiário" and dia_semana.lower() in dias_uteis:
        acesso_liberado = True
    
    return acesso_liberado

# Teste do programa
cargo = input("Digite o cargo do funcionário: ")
dia_semana = input("Digite o dia da semana: ")
if pode_acessar(cargo, dia_semana):
    print("Acesso Permitido.")
else:
    print("Acesso Negado.")