import pytest
from pages.entrega import calcular_taxa_entrega


def test_deve_retornar_taxa_fixa():
    """Teste para verificar se a taxa fixa é retornada corretamente para distâncias de até 3 km."""
    
    resultado = calcular_taxa_entrega(3)

    assert resultado == 5


def test_deve_calcular_taxa_adicional():
    """Teste para verificar se a taxa adicional é calculada corretamente para distâncias maiores que 3 km."""

    resultado = calcular_taxa_entrega(7)

    assert resultado == 13


def test_deve_gerar_erro_para_distancia_negativa():
    """Teste para verificar se um erro é gerado quando a distância é negativa."""

    with pytest.raises(ValueError):
        calcular_taxa_entrega(-4)