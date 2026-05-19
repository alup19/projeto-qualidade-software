def calcular_total_pedido(itens, valor_minimo):
    """Calcula o total do pedido com base nos itens e verifica se o valor mínimo é atingido."""
    
    total = sum(item["preco"] for item in itens)

    if total < valor_minimo:
        raise ValueError("Valor mínimo do pedido não atingido")

    return total