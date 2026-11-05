transactions = []

def add_transaction():
    description = input("descreva sua transação: ")
    transaction_type = input("Digite o tipo (R para Receita / D para Despesa): ").upper().strip()
    amount = float(input("Digite o valor: "))

    transaction = {
        "Description": description,
        "Type": transaction_type,
        "Amount": amount
    }

    transactions.append(transaction)

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