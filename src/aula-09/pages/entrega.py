def calcular_taxa_entrega(distancia):
    if distancia < 0:
        raise ValueError("Distância inválida")

    if distancia <= 3:
        return 5

    adicional = (distancia - 3) * 2

    return 5 + adicional