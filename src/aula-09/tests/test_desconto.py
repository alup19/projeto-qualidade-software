import pytest
from pages.desconto import aplicar_desconto


def test_deve_aplicar_desconto_corretamente():
    resultado = aplicar_desconto(150, 20)

    assert resultado == 120


def test_deve_aceitar_desconto_zero():
    resultado = aplicar_desconto(95, 0)

    assert resultado == 95


def test_deve_gerar_erro_para_percentual_invalido():
    with pytest.raises(ValueError):
        aplicar_desconto(120, 130)