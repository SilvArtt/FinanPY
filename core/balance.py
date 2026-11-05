from core.transaction import transactions


def check_balance():
    current_balance = update_balance()
    print(f"Saldo: {format_balance(current_balance)}")
    input("Pressione ENTER para Continuar...")

def update_balance():
    balance = 0

    for transaction in transactions:
        if transaction["Type"] == "R":
            balance += transaction["Amount"]
        elif transaction["Type"] == "D":
            balance -= transaction["Amount"]

    return balance

def format_balance(value):
    return f"R${value:.2f}"





