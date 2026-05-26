# Aula 12 – BDD e Automação Orientada a Comportamento

# 📌 PBL – LocalEats

---

# 👥 Integrantes

- Alberto Parker
- Eduardo Leal

---

# 🔹 1. Fluxos Escolhidos

## 👤 Integrante: Alberto Parker

### Fluxo
Histórico de pedidos

### Objetivo
Validar se os pedidos realizados pelo usuário são exibidos corretamente no sistema.

---

## 👤 Integrante: Eduardo Leal

### Fluxo
Navegação entre páginas

### Objetivo
Validar se o usuário consegue navegar corretamente entre as páginas do sistema sem erros.

---

# 🔹 2. Cenários BDD

## 📄 Arquivo
`features/historico_pedidos.feature`

```gherkin
Feature: Histórico de pedidos

  Scenario: Visualizar pedidos realizados
    Given que o usuário acessa a página de pedidos
    When visualizar o histórico de transações
    Then o sistema deve exibir os pedidos cadastrados

  Scenario: Validar valor total do pedido
    Given que o usuário acessa a página de pedidos
    When visualizar um pedido realizado
    Then o sistema deve exibir o valor total do pedido
```

---

## 📄 Arquivo
`features/navegacao_paginas.feature`

```gherkin
Feature: Navegação entre páginas

  Scenario: Navegar para favoritos
    Given que o usuário acessa o sistema
    When acessar a página de favoritos
    Then o sistema deve exibir a tela de favoritos

  Scenario: Navegar para pedidos
    Given que o usuário acessa o sistema
    When acessar a página de pedidos
    Then o sistema deve exibir a tela de pedidos
```

---

# 🔹 3. Automação com pytest-bdd

## 📂 Estrutura do Projeto

```txt
src/
└── aula-12/
    │
    ├── features/
    │   ├── historico_pedidos.feature
    │   └── navegacao_paginas.feature
    │
    ├── tests/
    │   ├── conftest.py
    │   ├── test_historico_pedidos.py
    │   └── test_navegacao_paginas.py
    │
    ├── evidencias/
    │   ├── evidencia1.png
    │   ├── evidencia2.png
    │   └── evidencia3.png
    │
    ├── requirements.txt
    │
    ├── README.md
    │
    └── aula-12-bdd-automacao-comportamento.md
```

---

# 🔹 4. Execução dos Testes

## ▶️ Comando executado

```bash
pytest -v
```

---

## ✅ Resultado esperado

```txt
======================================================================================================== test session starts ========================================================================================================

collected 4 items

tests/test_historico_pedidos.py::test_visualizar_pedidos_realizados PASSED                                                                                     [ 25%]

tests/test_historico_pedidos.py::test_validar_valor_total_do_pedido PASSED                                                                                     [ 50%]

tests/test_navegacao_paginas.py::test_navegar_para_favoritos PASSED                                                                                            [ 75%]

tests/test_navegacao_paginas.py::test_navegar_para_pedidos PASSED                                                                                              [100%]

======================================================================================================== 4 passed in 41.93s =========================================================================================================
```

---

# 🔹 5. Evidências

## 📷 Print da execução

```txt
evidencias/
  evidencia1.png
```

---

## 📷 Prints da aplicação

```txt
evidencias/
  evidencia2.png

evidencias/
  evidencia3.png
```

---

# 🔹 6. Análise Crítica

## O cenário ficou compreensível?

Sim. A estrutura Given-When-Then deixou os comportamentos mais claros e organizados.

---

## O teste automatizado ficou legível?

Sim. A separação entre cenários e implementação facilitou a leitura e manutenção dos testes.

---

## O BDD ajudou a entender o comportamento?

Sim. O comportamento esperado ficou compreensível tanto para pessoas técnicas quanto não técnicas.

---

## Quais dificuldades surgiram?

- Configuração do pytest-bdd
- Integração com Playwright
- Identificação de seletores estáveis
- Dependência da interface visual

---

## Os seletores foram frágeis?

Parcialmente. Alguns seletores dependem diretamente de textos e componentes visuais da aplicação.

---

## O teste ficou dependente da interface?

Sim. Alterações no frontend podem impactar diretamente os testes automatizados.

---

## O cenário representa uma regra de negócio?

Sim. Tanto o histórico de pedidos quanto a navegação entre páginas representam funcionalidades importantes do sistema.

---

## O que tornaria o teste mais robusto?

- Uso de atributos `data-testid`
- Seletores mais específicos
- Menor dependência de textos visíveis
- Melhor desacoplamento da interface

---

# 🔹 7. Reflexão Final

## BDD melhora a comunicação entre equipe?

Sim. O BDD aproxima QA, desenvolvimento e negócio através de uma linguagem mais clara e colaborativa.

---

## Todo teste deve usar BDD?

Não. O BDD é mais indicado para fluxos importantes e regras críticas do sistema.

---

## Quando vale a pena usar BDD?

Quando existe necessidade de documentar comportamentos de forma clara, colaborativa e automatizável.

---

## O comportamento ficou mais claro?

Sim. Os cenários ajudaram a visualizar melhor as funcionalidades e regras do sistema.

---

## Como isso ajuda no projeto do grupo?

Ajuda na organização, documentação viva, manutenção e entendimento dos requisitos do sistema.

---

# 📦 Repositório GitHub

```txt
https://github.com/alup19/projeto-qualidade-software/tree/main/src/aula-12
```

---

# ✅ Conclusão

A atividade permitiu compreender:

- Escrita de cenários BDD
- Estrutura Given-When-Then
- Integração entre pytest-bdd e Playwright
- Automação orientada a comportamento
- Organização de testes automatizados
- Importância da legibilidade dos testes
- Separação entre comportamento e implementação
- Documentação viva de requisitos