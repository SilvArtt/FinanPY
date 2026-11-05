from core.balance import check_balance
from core.transaction import *
from utils.formatters import get_valid_option
isRunning = True

if __name__ == '__main__':
   while isRunning:
       print("=" * 32)
       print("       FinanPY")
       print("=" * 32)
       print("[1] Adicionar transação")
       print("[2] Ver saldo atual")
       print("[3] Listar transações")
       print("[0] Sair")
       print("=" * 32)

       op = get_valid_option()

       match op:
           case 1:
               add_transaction()
           case 2:
               check_balance()
           case 3:
               print("\n--- Listar transações ---")
               print("R - Receitas")
               print("D - Despesas")
               print("T - Todas")

               opt = input("Escolha uma opção: ").upper().strip()
               list_transaction(opt)
               input("Pressione ENTER para Continuar...")
           case 0:
               print("Saiu do programa!")
               isRunning = False
           case _:
               print("Erro, Selecione de [0] a [3].")


