import pytest
from pages.pedido import calcular_total_pedido


def test_deve_calcular_total_do_pedido():
    """Teste para verificar se o total do pedido é calculado corretamente quando o valor mínimo é atingido."""
    
    itens = [{"preco": 18}, {"preco": 27}]
    valor_minimo = 40

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == 45


def test_deve_aceitar_valor_exatamente_no_minimo():
    """Teste para verificar se o total do pedido é calculado corretamente quando o valor total é exatamente igual ao valor mínimo."""

    itens = [{"preco": 22}, {"preco": 18}]
    valor_minimo = 40

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == 40


def test_deve_gerar_erro_quando_valor_minimo_nao_atingido():
    """Teste para verificar se um erro é gerado quando o valor mínimo não é atingido."""

    itens = [{"preco": 8}, {"preco": 9}]
    valor_minimo = 30

    with pytest.raises(ValueError):
        calcular_total_pedido(itens, valor_minimo)