# Aula 6 – Planejamento e Execução de Testes

> Disciplina: Qualidade de Software  
> Projeto: LocalEats  
> Integrantes do grupo:  
> Alberto Parker
> Eduardo Leal


---

# 1. Plano de Testes

## 1.1 Objetivo
Descreva o objetivo do plano de testes.

> Validar as principais funcionalidades do sistema LocalEats, garantindo que atendam aos requisitos esperados, funcionem corretamente e ofereçam uma boa experiência ao usuário.

---

## 1.2 Escopo

### O que será testado
- Login e cadastro de usuários
- Busca de restaurantes
- Realização de pedidos

### O que NÃO será testado
- Integração com sistemas externos
- Segurança do sistema
- Avaliações de restaurante
- Favoritar restaurante

---

## 1.3 Funcionalidades selecionadas
Liste as funcionalidades que serão foco dos testes:

- Login/Cadastro
- Busca de restaurantes
- Pedido

---

## 1.4 Estratégia de Testes

Descreva como os testes serão realizados.

- Tipos de teste:
  - ( x ) Funcional
  - ( x ) Usabilidade
  - ( ) Outros: _______

- Abordagem:
  > Testes baseado em cenários simulando o uso real de um usuário.

---

## 1.5 Responsáveis

Defina os papéis na equipe:

| Nome          | Responsabilidade           |
|---------------|----------------------------|
| Alberto Parker| Execução dos testes        |
| Eduardo Leal  | Planejamento e documentação|

---

# 2. Casos de Teste

Crie no mínimo 5 casos de teste.

---

## CT-01 – Cadastro do usuário

**Pré-condição:**  
Usuário não possui cadastro no sistema

**Passos:**  
1. Acessar a tela de cadastro
2. Preencher nome, e-mail e senha válidos
3. Clicar em “Cadastrar”

**Dados de entrada (se aplicável):**  
nome: eduardo leal
email: eduardolealsoares2005@gmail.com
senha: leal

**Resultado esperado:**  
Usuário é cadastrado com sucesso e redirecionado para a tela inicial

---

## CT-02 – Login com dados válidos

**Pré-condição:**
Usuário já cadastrado

**Passos:**  
1. Acessar a tela de login
2. Inserir e-mail e senha válidos
3. Clicar em “Entrar” 

**Dados de entrada (se aplicável):**  
email: eduardolealsoares2005@gmail.com
senha: leal

**Resultado esperado:**  
Usuário é redirecionado para a página inicial com sucesso
---

## CT-03 – Login com senha incorreta

**Pré-condição:**  
Usuário já cadastrado

**Passos:**  
1. Acessar a tela de login
2. Inserir e-mail e senha que sejam inválidos
3. Clicar em “Entrar”  

**Dados de entrada (se aplicável):**  
email: eduardolealsoares2005@gmail.com
senha: 12345

**Resultado esperado:**  
Sistema não permite a entrada para tela inicial e exibe mensagem de erro
---

## CT-04 – Buscar restaurante

**Pré-condição:**
Usuário logado

**Passos:**  
1. Acessar barra de busca
2. Digitar nome de restaurante
3. Clicar em buscar

**Dados de entrada (se aplicável):**  
Restaurante Sabor 0
**Resultado esperado:**  
Lista de restaurantes relacionados aparece

---
## CT-05 – Realizar pedido

**Pré-condição:**  
Usuário logado e restaurante selecionado

**Passos:**  
1. Escolher produto
2. Adicionar ao carrinho
3. Finalizar o pedido

**Dados de entrada (se aplicável):**  

**Resultado esperado:**  
Pedido é registrado com sucesso
---



# 3. Execução dos Testes

Preencha a tabela com os resultados obtidos.

| ID     | Resultado (Passou/Falhou) | Evidência (descrição ou print)         |
|--------|--------------------------|-----------------------------------------|
| CT-01  |           Passou         |   Cadastro realizado com sucesso        |
| CT-02  |           Passou         |   Login realizado com sucesso           |
| CT-03  |           Passou         |   Mensagem de erro exibida              |
| CT-04  |           Falhou         |   Restaurante relacionados não listados |
| CT-05  |           Passou         |   Pedido realizado com sucesso          |

---

# 4. Análise dos Resultados

- Quantidade de testes executados: 5
- Quantidade de testes que passaram: 4  
- Quantidade de testes que falharam: 1 

## Principais problemas encontrados
- Problemas para encontrar restaurantes pela busca

---

# 5. Reflexão

Responda às questões abaixo:

- O plano de testes ajudou a organizar melhor o processo? Por quê?
Sim pois nos deu mais clareza facilitando na hora de executar

- Algum problema só foi identificado durante a execução? Explique.
Sim, o problema das buscas pois antes de testar a ferramente de busca não tinha comko saber se funcionava ou não

- O que o grupo melhoraria no processo de testes?
Incluir diversos testes em diversas ocasiões
---

## Conclusão

O comportamento das funcionalidades foi considerado parcialmente aceitável, pois a maioria funcionou corretamente, mas ainda existem falhas importantes que precisam ser corrigidas.


---

# 6. Conclusão Geral

Faça um resumo final:

- Qualidade geral do sistema testado: Boa, mas com pontos a melhorar
- Principais pontos positivos: Interface simples e grande parte das funcionalidades básicas funcionando
- Principais problemas identificados: Funcionalidade de busca não funciona 
- Impressão geral do grupo sobre o processo de testes: O processo de testes foi essencial para identificar falhas e melhorar o sistema
