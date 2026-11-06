from storage.json_storage import load_data,save_data
from utils.formatters import *
transactions = load_data()

def add_transaction():
    description = get_valid_description()
    transaction_type = get_valid_type()
    amount = get_valid_amount()
    category = get_valid_category(transaction_type)
    date = format_date()

    transaction = {
        "Description": description,
        "Type": transaction_type,
        "Amount": amount,
        "Category": category,
        "Date": date
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
        tipo = {"R": "Receita", "D": "Despesa"}.get(transaction["Type"], "Desconhecido")
        sinal = {"R": "+", "D": "-"}.get(transaction["Type"], "?")
        description = transaction["Description"]
        amount = transaction["Amount"]
        category = transaction.get("Category") or "N/A"
        date = transaction.get("Date") or "N/A"

        print(
            f"{number}. {date} | {description} | {tipo} | {sinal} R$ {amount:.2f} | Categoria: {category}"
        )

