# 🧪 Aula 5 – Testes Funcionais vs Estruturais  
**LocalEats**

## 👥 Integrantes do Grupo  
- Alberto Parker
- Eduardo Leal

---

## 🎯 1. Funcionalidade escolhida  

**Funcionalidade selecionada:**  
Busca de restaurantes  

**Descrição da funcionalidade:**  
A funcionalidade permite que o usuário pesquise restaurantes no sistema utilizando nome, tipo de comida ou filtros, retornando uma lista de resultados relacionados.

**O que o usuário espera:**  
O usuário espera encontrar resultados corretos, rápidos e relevantes de acordo com o que foi pesquisado, além de filtros funcionando corretamente e sem erros.

---

## 🔍 2. Testes Caixa-Preta (Visão do Usuário)  

**Quais testes vocês fariam sem conhecer o código?**  
Testar diferentes tipos de busca e verificar se os resultados retornados são corretos.

### 🔹 Cenários de teste  

**Cenário 1:**  
Buscar pelo nome de um restaurante existente  
→ Deve retornar o restaurante correto  

**Cenário 2:**  
Buscar por um tipo de comida (ex: “pizza”)  
→ Deve retornar restaurantes relacionados  

**Cenário 3:**  
Buscar com campo vazio  
→ Deve mostrar lista padrão ou mensagem adequada  

**Cenário 4:**  
Buscar com caracteres inválidos ou aleatórios  
→ Não deve quebrar o sistema e deve tratar o erro  

---

### 🔹 Possíveis erros identificados  
- Resultados incorretos  
- Nenhum resultado mesmo existindo dados  
- Filtros não funcionando  
- Lentidão ou travamento  
- Erros com caracteres especiais  

---

## 🔧 3. Testes Caixa-Branca (Visão do Sistema)  

**Como essa funcionalidade poderia estar implementada internamente?**  
A funcionalidade provavelmente utiliza validações de entrada, consultas ao banco de dados e estruturas condicionais para tratar diferentes tipos de busca.

### 🔹 Lógica hipotética (pseudo-código ou descrição)  

- Se o campo de busca estiver vazio → retornar lista padrão  
- Se houver texto → buscar no banco de dados  
- Se houver filtros → aplicar filtros nos resultados  
- Se não houver resultados → exibir mensagem  

---

### 🔹 Situações a serem testadas  

**Situação 1:**  
Validação de campo vazio  

**Situação 2:**  
Aplicação correta dos filtros  

**Situação 3:**  
Retorno correto dos dados do banco  

---

### 🔹 Possíveis erros identificados  
- Falha na lógica de busca  
- Condições não tratadas (if/else incorretos)  
- Problemas na consulta ao banco  
- Falta de validação de entrada  

---

## ⚖️ 4. Comparação entre as abordagens  

**Qual a principal diferença entre testar sem ver o código e com acesso ao código?**  
Testes caixa-preta analisam o comportamento do sistema sem considerar sua implementação. Já os testes caixa-branca analisam a lógica interna e o funcionamento do código.

**Que tipo de problema cada abordagem ajuda a encontrar?**

**Caixa-preta:**  
- Erros visíveis ao usuário  
- Problemas de funcionalidade  
- Resultados incorretos  

**Caixa-branca:**  
- Erros na lógica interna  
- Falhas em condições e validações  
- Problemas na estrutura do código  

---

## 💡 5. Reflexão no contexto do LocalEats  

**Qual abordagem parece mais importante neste momento do projeto?**  
A caixa-preta parece mais importante inicialmente, pois os problemas atuais estão relacionados ao comportamento do sistema.

**Apenas uma abordagem seria suficiente? Por quê?**  
Não. As duas abordagens são necessárias, pois a caixa-preta identifica os erros e a caixa-branca ajuda a entender e corrigir a causa desses erros.

---

## 🚀 Conclusão  

Com essa atividade, o grupo entendeu que existem diferentes formas de testar um sistema e que cada uma tem um objetivo específico. Os testes caixa-preta ajudam a verificar se o sistema funciona corretamente para o usuário, enquanto os testes caixa-branca ajudam a analisar a lógica interna. A combinação das duas abordagens é essencial para garantir a qualidade do sistema LocalEats.
