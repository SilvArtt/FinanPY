import json

def load_data():
    try:
        with open("Data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        print("Erro: Os dados da transações não foram lidos ou corromperam")
        return []

def save_data(transactions):
    try:
        with open("Data.json", "w", encoding="utf-8") as file:
            json.dump(transactions, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"a transação foi adicionada à memória, mas não foi salva no disco. Erro: {e}")