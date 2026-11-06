from core.transaction import transactions
from utils.formatters import format_balance

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





