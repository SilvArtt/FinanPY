from core.transaction import transactions

def monthly_report():
    month_balance = 0.0
    count = 0

    selected_month = input("Qual mês/ano deseja consultar (formato MM/AAAA, ex: 11/2026)?: ").strip()

    for transaction in transactions:
        if selected_month in transaction.get("Date", "N/A"):
            if transaction["Type"] == "R":
                month_balance += transaction["Amount"]
            elif transaction["Type"] == "D":
                month_balance -= transaction["Amount"]

            count += 1

    if count == 0:
        print(f"Nenhuma transação encontrada para o período {selected_month}.")
    else:
        print(f"Foram encontradas {count} transações no período {selected_month}. Saldo do mês: R$ {month_balance:.2f}")
    input("Pressione ENTER para sair...")