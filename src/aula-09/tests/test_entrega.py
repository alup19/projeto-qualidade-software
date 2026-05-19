import pytest
from pages.entrega import calcular_taxa_entrega


def test_deve_retornar_taxa_fixa():
    resultado = calcular_taxa_entrega(3)

    assert resultado == 5


def test_deve_calcular_taxa_adicional():
    resultado = calcular_taxa_entrega(7)

    assert resultado == 13


def test_deve_gerar_erro_para_distancia_negativa():
    with pytest.raises(ValueError):
        calcular_taxa_entrega(-4)