def aplicar_desconto(valor_total, percentual):
    if percentual < 0 or percentual > 100:
        raise ValueError("Percentual inválido")

    desconto = valor_total * (percentual / 100)

    return valor_total - desconto