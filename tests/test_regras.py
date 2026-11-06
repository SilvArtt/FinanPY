import pytest
from unittest.mock import patch
from utils.formatters import AMOUNT_PATTERN, MONTH_PATTERN
from core.balance import update_balance

# --- Testes de Saldo ---

@patch("core.balance.transactions", new=[
    {"Type": "R", "Amount": 1000},
    {"Type": "D", "Amount": 300},
])
def test_balance_receita_e_despesa():
    # Act
    resultado = update_balance()
    # Assert
    assert resultado == 700


@patch("core.balance.transactions", new=[])
def test_balance_lista_vazia():
    resultado = update_balance()
    assert resultado == 0


# --- Testes de Regex para Valor ---

@pytest.mark.parametrize("valor", ["100", "100.50", "100,50"])
def test_amount_pattern_aceita_validos(valor):
    assert AMOUNT_PATTERN.fullmatch(valor), f"Deveria aceitar: {valor!r}"


@pytest.mark.parametrize("valor", ["abc", "-50", "100.555", ""])
def test_amount_pattern_rejeita_invalidos(valor):
    assert not AMOUNT_PATTERN.fullmatch(valor), f"Deveria rejeitar: {valor!r}"


# --- Testes de Regex para Mês ---

@pytest.mark.parametrize("mes", ["01/2026", "12/2030"])
def test_month_pattern_aceita_validos(mes):
    assert MONTH_PATTERN.fullmatch(mes)


@pytest.mark.parametrize("mes", ["13/2026", "1/2026", "01-2026"])
def test_month_pattern_rejeita_invalidos(mes):
    assert not MONTH_PATTERN.fullmatch(mes)