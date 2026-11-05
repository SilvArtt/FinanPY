from Funcoes.Transacao import transactions

def check_balance():
    balance = update_balance()
    print(f"Saldo: R${balance:.2f}")
    input("Pressione ENTER para Continuar...")

def update_balance():
    balance = 0

    for transaction in transactions:
        if transaction["Type"] == "R":
            balance += transaction["Amount"]
        elif transaction["Type"] == "D":
            balance -= transaction["Amount"]

    return balance