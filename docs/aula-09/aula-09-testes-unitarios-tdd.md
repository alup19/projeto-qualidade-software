# Aula 9 – Testes Unitários Automatizados e TDD – LocalEats

## 👥 Integrantes

- Alberto Parker
- Eduardo Leal

---

# 📁 Estrutura do Projeto

```bash
.
├── src/
│   └── aula-09/
│       ├── pages/
│       │   ├── pedido.py
│       │   ├── desconto.py
│       │   └── entrega.py
│       │
│       └── tests/
│           ├── test_pedido.py
│           ├── test_desconto.py
│           └── test_entrega.py
```

---

# 🔹 1. Funcionalidades escolhidas

Cada integrante ficou responsável por uma funcionalidade diferente do sistema LocalEats.

---

## 👤 Integrante 1 – Cálculo do total do pedido com valor mínimo

### Arquivo da implementação
`/src/aula-09/pages/pedido.py`

### Arquivo de testes
`/src/aula-09/tests/test_pedido.py`

### Descrição
Responsável por calcular o valor total do pedido e verificar se o valor mínimo exigido foi atingido.

### Regras de negócio

- O total deve ser a soma dos itens
- O pedido precisa atingir o valor mínimo
- Caso contrário, deve gerar erro

---

## 👤 Integrante 2 – Aplicação de desconto percentual

### Arquivo da implementação
`/src/aula-09/pages/desconto.py`

### Arquivo de testes
`/src/aula-09/tests/test_desconto.py`

### Descrição
Aplica um desconto percentual sobre o valor do pedido.

### Regras de negócio

- O percentual deve estar entre 0% e 100%
- O valor final não pode ser negativo

---

## 👤 Integrante 3 – Cálculo da taxa de entrega

### Arquivo da implementação
`/src/aula-09/pages/entrega.py`

### Arquivo de testes
`/src/aula-09/tests/test_entrega.py`

### Descrição
Calcula a taxa de entrega conforme a distância.

### Regras de negócio

- Até 3km → taxa fixa
- Acima de 3km → taxa adicional
- Distância negativa → erro

---

# 🔹 2. Testes Unitários

---

# 🧪 Integrante 1 – Testes do Pedido

---

## ✅ Teste 1 – Deve calcular corretamente o total do pedido

### Cenário testado
Valida se o pedido retorna corretamente o valor total quando o valor mínimo é atingido.

### Dados de entrada

```python
itens = [{"preco": 18}, {"preco": 27}]
valor_minimo = 40
```

### Resultado esperado

- Retornar 45
- Não gerar erro

### Execução
✅ Passou

---

## ✅ Teste 2 – Deve aceitar pedido no valor mínimo

### Cenário testado
Valida pedidos exatamente iguais ao valor mínimo.

### Dados de entrada

```python
itens = [{"preco": 22}, {"preco": 18}]
valor_minimo = 40
```

### Resultado esperado

- Retornar 40
- Não gerar erro

### Execução
✅ Passou

---

## ❌ Teste 3 – Deve gerar erro quando pedido não atingir valor mínimo

### Cenário testado
Valida pedidos abaixo do valor mínimo.

### Dados de entrada

```python
itens = [{"preco": 8}, {"preco": 9}]
valor_minimo = 30
```

### Resultado esperado

- Gerar `ValueError`

### Execução
✅ Passou

---

# 🧪 Integrante 2 – Testes do Desconto

---

## ✅ Teste 1 – Deve aplicar desconto corretamente

### Cenário testado
Valida desconto válido aplicado ao pedido.

### Dados de entrada

```python
valor_total = 150
percentual = 20
```

### Resultado esperado

- Retornar 120

### Execução
✅ Passou

---

## ✅ Teste 2 – Deve aceitar desconto de 0%

### Cenário testado
Valida comportamento sem desconto.

### Dados de entrada

```python
valor_total = 95
percentual = 0
```

### Resultado esperado

- Retornar 95

### Execução
✅ Passou

---

## ❌ Teste 3 – Deve gerar erro para percentual inválido

### Cenário testado
Valida percentual acima do permitido.

### Dados de entrada

```python
valor_total = 120
percentual = 130
```

### Resultado esperado

- Gerar `ValueError`

### Execução
✅ Passou

---

# 🧪 Integrante 3 – Testes da Taxa de Entrega

---

## ✅ Teste 1 – Deve retornar taxa fixa para distância curta

### Cenário testado
Valida taxa fixa para entregas até 3km.

### Dados de entrada

```python
distancia = 3
```

### Resultado esperado

- Retornar 5

### Execução
✅ Passou

---

## ✅ Teste 2 – Deve calcular taxa adicional corretamente

### Cenário testado
Valida cálculo para distância acima de 3km.

### Dados de entrada

```python
distancia = 7
```

### Resultado esperado

- Retornar 13

### Execução
✅ Passou

---

## ❌ Teste 3 – Deve gerar erro para distância negativa

### Cenário testado
Valida entrada inválida.

### Dados de entrada

```python
distancia = -4
```

### Resultado esperado

- Gerar `ValueError`

### Execução
✅ Passou

---

# 🔹 3. Aplicação do TDD

## Funcionalidade escolhida
Cálculo do total do pedido.

---

## 🔴 Red

Primeiramente foi criado o teste antes da implementação.

### Teste criado

```python
def test_deve_calcular_total_do_pedido():
    itens = [{"preco": 18}, {"preco": 27}]
    valor_minimo = 40

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == 45
```

### Resultado inicial

```bash
NameError: name 'calcular_total_pedido' is not defined
```

O teste falhou porque a função ainda não existia.

---

## 🟢 Green

Foi criada a implementação mínima para fazer o teste passar.

### Implementação inicial

```python
def calcular_total_pedido(itens, valor_minimo):
    return 45
```

O teste passou, mas ainda sem atender corretamente às regras de negócio.

---

## 🔵 Refactor

Após os testes passarem, o código foi melhorado.

### Implementação final

```python
def calcular_total_pedido(itens, valor_minimo):
    total = sum(item["preco"] for item in itens)

    if total < valor_minimo:
        raise ValueError("Valor mínimo do pedido não atingido")

    return total
```

### Melhorias realizadas

- Remoção de valores fixos
- Implementação dinâmica da soma
- Inclusão da validação do valor mínimo
- Código mais organizado e reutilizável

---

# 🔹 4. Refatoração

Durante o desenvolvimento foram realizadas melhorias como:

- Melhor organização dos arquivos
- Uso de nomes mais descritivos
- Separação entre implementação e testes
- Redução de duplicações
- Inclusão de tratamento de erros
- Melhor legibilidade

### Exemplo de melhoria

Antes:

```python
def calc(x):
    return x
```

Depois:

```python
def calcular_total_pedido(itens, valor_minimo):
    total = sum(item["preco"] for item in itens)

    if total < valor_minimo:
        raise ValueError("Valor mínimo do pedido não atingido")

    return total
```

🧩 O código ficou mais organizado, legível e fácil de manter, evitando problemas futuros durante novas implementações.

---

# 🔹 5. Execução dos Testes

| Total de testes | Passaram | Falharam |
|---|---|---|
| 9 | 9 | 0 |

---

## Evidência de execução

```bash
================== test session starts ==================

tests/test_desconto.py ... PASSED
tests/test_entrega.py ... PASSED
tests/test_pedido.py ... PASSED

================== 9 passed in 0.04s ==================
```

---

# 🔹 6. Reflexão no contexto do LocalEats

## Foi difícil escrever testes antes do código?

Sim. No início foi necessário mudar a lógica de desenvolvimento e pensar primeiro nos comportamentos esperados da funcionalidade.

---

## O TDD ajudou no desenvolvimento?

Sim. O TDD ajudou a desenvolver funcionalidades de forma mais organizada e segura.

---

## Os testes aumentaram a confiança no código?

Sim. Os testes automatizados ajudam a detectar erros rapidamente e evitam regressões.

---

## O que melhorariam?

- Criar mais cenários de teste
- Melhorar cobertura
- Automatizar testes no GitHub Actions
- Criar testes de integração

---

## Como isso ajuda no projeto do grupo?

Ajuda a manter a qualidade do sistema LocalEats, reduzindo falhas e facilitando futuras alterações no código.