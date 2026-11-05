from core.json import load_data,save_data
from utils.formatters import *
transactions = load_data()

def add_transaction():
    description = get_valid_description()
    transaction_type = get_valid_type()
    amount = get_valid_amount()

    transaction = {
        "Description": description,
        "Type": transaction_type,
        "Amount": amount
    }

    transactions.append(transaction)
    save_data(transactions)

def list_transaction(condition):
    if condition not in ("R", "D", "T"):
        print("Opção inválida.")
        return

    transactions_found = [
        transaction
        for transaction in transactions
        if condition == "T" or transaction["Type"] == condition
    ]

    if not transactions_found:
        print("Nenhuma transação registrada.")
        return

    for number, transaction in enumerate(transactions_found,start=1):
        tipo = "Receita" if transaction["Type"] == "R" else "Despesa"
        sinal = '+' if transaction["Type"] == "R" else '-'
        print(
            f"{number}. {transaction['Description']} | "
            f"{tipo} | {sinal} R$ {transaction['Amount']:.2f}"
        )

