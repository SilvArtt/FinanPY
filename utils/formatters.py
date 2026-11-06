from datetime import datetime
import re

def get_valid_type(tipo=""):
    while tipo not in ["R", "D"]:
        tipo = input("Digite o tipo (R para Receita / D para Despesa): ")
        tipo = tipo.upper().strip()
    return tipo

AMOUNT_PATTERN = re.compile(r"^\d+([.,]\d{1,2})?$")

def get_valid_amount():
    while True:
        value = input("Digite o valor: ").strip()

        if not AMOUNT_PATTERN.fullmatch(value):
            print("Valor invalido, Apenas números, com até 2 casas decimais!")
            continue

        try:
            amount = float(value.replace(",", "."))
        except ValueError:
            print("Valor invalido, Digite um número!")
            continue

        if amount <= 0:
            print("Valor inválido. Não aceitamos valores menores ou iguais a zero.")
            continue

        return amount

MONTH_PATTERN = re.compile(r"^(0[1-9]|1[0-2])/\d{4}$")

def get_valid_month():
    while True:
        month = input("Qual mês/ano deseja consultar (MM/AAAA)?:").strip()

        if not MONTH_PATTERN.fullmatch(month):
            print("Formato Invalido!, Formato Aceito: (MM/AAAA), ex: (01/2010)")
            continue

        return month



def get_valid_description(description=""):
    while not description or len(description) > 255:
        description = input("descreva sua transação: ").upper().strip()
    return description

def get_valid_category(transaction_type):
    r_category = {
         1:"SALÁRIO",
         2:"FREELANCE/EXTRA",
         3:"INVESTIMENTOS",
         4:"PRESENTES",
         5:"OUTROS"
    }
    d_category = {
         1: "ALIMENTAÇÃO",
         2: "MORADIA",
         3: "TRANSPORTE",
         4: "SAÚDE",
         5: "LAZER",
         6: "EDUCAÇÃO",
         7: "VESTUÁRIO",
         8: "OUTROS"
    }

    categories = r_category if transaction_type == "R" else d_category if transaction_type == "D" else None

    if not categories:
        print("Erro: Tipo de transação invalida!")
        return "N/A"

    while True:
        print("\nSelecione a categoria:")
        for key,value in categories.items():
            print(f"{key}: {value.title()}")
        try:
            category = int(input("Digite o número da categoria: "))

            if category in categories:
                return categories[category]
            print("Erro: Categoria inválida! Escolha um número da lista.")
        except ValueError:
            print("Erro: Entrada inválida! Digite apenas números inteiros.")

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

def format_balance(value):
    return f"R${value:.2f}"

def format_date():
    return datetime.now().strftime("%d/%m/%Y %H:%M")