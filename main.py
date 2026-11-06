from core.balance import check_balance
from core.report import monthly_report
from core.transaction import *
from utils.formatters import get_valid_option
from utils.clean import clean_terminal
import logging

logging.basicConfig(
    filename='finanpy.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

isRunning = True

if __name__ == '__main__':
   while isRunning:
       clean_terminal()
       
       print("=" * 32)
       print("       FinanPY")
       print(f"      Saldo Atual: R$ {check_balance()}")
       print("=" * 32)
       print("[1] Adicionar transação")
       print("[2] Listar transações")
       print("[3] Relatorio Mensal")
       print("[0] Sair")
       print("=" * 32)

       op = get_valid_option()

       match op:
           case 1:
               add_transaction()
           case 2:
               print("\n--- Listar transações ---")
               print("R - Receitas")
               print("D - Despesas")
               print("T - Todas")

               opt = input("Escolha uma opção: ").upper().strip()
               list_transaction(opt)
               input("Pressione ENTER para Continuar...")
           case 3:
               monthly_report()
           case 0:
               print("Saiu do programa!")
               isRunning = False
           case _:
               print("Erro, Selecione de [0] a [3].")


