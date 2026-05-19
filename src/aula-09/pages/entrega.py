def calcular_taxa_entrega(distancia):
    """Calcula a taxa de entrega com base na distância, aplicando uma taxa fixa para distâncias de até 3 km e uma taxa adicional para distâncias maiores."""

    if distancia < 0:
        raise ValueError("Distância inválida")

    if distancia <= 3:
        return 5

    adicional = (distancia - 3) * 2

    return 5 + adicional