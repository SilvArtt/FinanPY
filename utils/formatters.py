def get_valid_type(tipo=""):
    while tipo not in ["R", "D"]:
        tipo = input("Digite o tipo (R para Receita / D para Despesa): ")
        tipo = tipo.upper().strip()
    return tipo

def get_valid_amount():
    while True:
        try:
            amount = float(input(f"Digite o valor: "))
        except ValueError:
            print("Valor invalido, Digite um número!")
            continue

        if amount <= 0:
            print("Valor invalido, Não aceitamos números abaixo ou igual á zero!")
            continue
        return amount

def get_valid_description(description=""):
    while not description or len(description) > 255:
        description = input("descreva sua transação: ").upper().strip()
    return description

def get_valid_option():
    while True:
        try:
            op = int(input("Escolha uma Opção [1] a [3], [0] para sair: "))
        except ValueError:
            print("Opção Invalida! digite apenas números!")
            continue
        if not 0 <= op <= 3:
            print("Erro, selecione uma opção de [0] a [3].")
            continue
        return op
