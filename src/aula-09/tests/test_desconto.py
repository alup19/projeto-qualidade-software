import pytest
from pages.desconto import aplicar_desconto


def test_deve_aplicar_desconto_corretamente():
    """Teste para verificar se o desconto é aplicado corretamente."""

    resultado = aplicar_desconto(150, 20)

    assert resultado == 120


def test_deve_aceitar_desconto_zero():
    """Teste para verificar se o desconto de 0% é aceito e não altera o valor total."""

    resultado = aplicar_desconto(95, 0)

    assert resultado == 95


def test_deve_gerar_erro_para_percentual_invalido():
    """Teste para verificar se um erro é gerado quando o percentual de desconto é inválido (negativo ou maior que 100)."""
    
    with pytest.raises(ValueError):
        aplicar_desconto(120, 130)