# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

## Integrantes

- Alberto Parker
- Eduardo Leal

---

## 1. Repositório da Atividade

| Item | Descrição |
|--------|--------|
| Nome do repositório | localeats-ci-laboratorio |
| Link do repositório | https://github.com/dudyus/localeats-ci-laboratorio |

### Estrutura de Diretórios

```text
localeats-ci-laboratorio/
├── tests/
│   ├── test_fav.py
│   └── features/
│       └── order_total.feature
├── .github/
│   └── workflows/
│       └── quality.yml
├── restaurante_fav.py
└── requirements.txt
```

---

## 2. Planejamento da Funcionalidade

| Item | Descrição |
|--------|--------|
| Título da Issue | Implementar funcionalidade de restaurante favorito |
| Objetivo da funcionalidade | Permitir que o usuário marque um restaurante como favorito |
| Link da Issue | https://github.com/dudyus/localeats-ci-laboratorio/issues/1 |

---

## 3. Teste Automatizado

| Item | Descrição |
|--------|--------|
| Tipo de teste | Unitário |
| Objetivo do teste | Verificar se o restaurante é marcado como favorito corretamente |
| Link para o arquivo do teste | https://github.com/dudyus/localeats-ci-laboratorio/blob/main/tests/test_fav.py |

```python
from restaurante_fav import marcar_favorito

def test_marcar_restaurante_favorito():
    resultado = marcar_favorito("Restaurante Sabor 1")
    assert resultado["favorito"] is True
```

---

## 4. Pipeline de Integração Contínua

| Item | Descrição |
|--------|--------|
| Nome do workflow | Quality Check |
| Evento que dispara a execução | push e pull_request |
| Link para o workflow | https://github.com/dudyus/localeats-ci-laboratorio/blob/main/.github/workflows/quality.yml |
| Link da execução | https://github.com/dudyus/localeats-ci-laboratorio/actions |

```yaml
name: Quality Check

on:
  push:
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: pip install pytest

      - run: python -m pytest -v
```

---

## 5. Indicadores de Qualidade

| Indicador | Valor |
|------------|---------|
| Quantidade de testes executados | 1 |
| Quantidade de testes aprovados | 1 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | Sucesso |

---

## 6. Registro de Defeito

| Item | Descrição |
|--------|--------|
| Título do defeito | Falha ao marcar restaurante como favorito |
| Severidade | Alta |
| Link da Issue | https://github.com/dudyus/localeats-ci-laboratorio/issues/2 |

O defeito foi simulado alterando a função responsável por marcar um restaurante como favorito para retornar um valor incorreto. O problema foi identificado pela falha do teste automatizado durante a execução do pipeline. Após corrigir a implementação, os testes voltaram a ser aprovados.