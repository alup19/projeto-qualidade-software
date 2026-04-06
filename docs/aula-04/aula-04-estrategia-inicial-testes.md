# Estratégia Inicial de Testes – LocalEats

## 1. Funcionalidades Principais

As principais funcionalidades do sistema LocalEats são:

1. Busca de restaurantes (por tipo de culinária, localização e preço)
2. Visualização de restaurantes (cardápio, fotos e avaliações)
3. Sistema de avaliações e comentários
4. Salvamento de favoritos
5. Recomendações personalizadas
6. Compartilhamento de experiências

---

## 2. Níveis de Teste

### 1. Busca de restaurantes

- **Teste unitário:** validação de filtros (cálculo de distância, faixa de preço, categorias)
- **Teste de integração:** integração entre API de busca, banco de dados e geolocalização
- **Teste de sistema:** usuário realiza busca com filtros e recebe resultados corretos
- **Teste de aceitação:** usuário consegue encontrar um restaurante desejado facilmente

---

### 2. Visualização de restaurantes

- **Teste unitário:** carregamento de dados (cardápio, fotos, avaliações)
- **Teste de integração:** API + banco de dados + serviço de imagens
- **Teste de sistema:** usuário acessa restaurante e visualiza todas as informações
- **Teste de aceitação:** usuário entende o restaurante e decide visitá-lo

---

### 3. Sistema de avaliações

- **Teste unitário:** criação, edição e persistência de avaliações
- **Teste de integração:** conexão entre frontend, backend e banco
- **Teste de sistema:** usuário avalia restaurante e avaliação permanece após atualização
- **Teste de aceitação:** usuário consegue registrar sua experiência com sucesso

---

### 4. Favoritos

- **Teste unitário:** salvar/remover restaurante
- **Teste de integração:** vínculo entre usuário e lista de favoritos
- **Teste de sistema:** usuário adiciona favorito e encontra depois
- **Teste de aceitação:** usuário consegue organizar seus locais preferidos

---

### 5. Recomendações personalizadas

- **Teste unitário:** lógica de recomendação baseada em histórico
- **Teste de integração:** integração com dados do usuário e comportamento
- **Teste de sistema:** sistema sugere restaurantes relevantes
- **Teste de aceitação:** usuário percebe valor nas recomendações

---

### 6. Compartilhamento de experiências

- **Teste unitário:** geração de conteúdo compartilhável
- **Teste de integração:** integração com redes sociais
- **Teste de sistema:** usuário compartilha restaurante
- **Teste de aceitação:** compartilhamento funciona corretamente

---

## 3. Prioridades e Riscos

###  Alta prioridade

**1. Busca de restaurantes**
- Impacto: se falhar, o sistema perde sua principal função
- Problema real relacionado: resultados incorretos
- Risco: usuário abandona a plataforma

**2. Visualização de restaurantes**
- Impacto: informações erradas prejudicam decisões
- Problema real: telas confusas
- Risco: perda de confiança

**3. Sistema de avaliações**
- Impacto: reputação da plataforma
- Problema real: avaliações desaparecendo
- Risco: perda de credibilidade com usuários e comerciantes

---

###  Média prioridade

**4. Recomendações personalizadas**
- Impacto: experiência do usuário
- Risco: recomendações irrelevantes reduzem engajamento

**5. Favoritos**
- Impacto: organização pessoal do usuário
- Risco: frustração, mas não impede uso total do sistema

---

###  Baixa prioridade

**6. Compartilhamento**
- Impacto: crescimento orgânico
- Risco: baixo impacto imediato na operação principal

---

## 4. Pirâmide de Testes

### Base (Maior quantidade) → Testes Unitários
- Justificativa:
  - Baixo custo
  - Execução rápida
  - Detecta erros cedo (ex: lógica de busca e recomendações)

---

### Meio → Testes de Integração
- Justificativa:
  - Importante devido às inconsistências entre web e mobile
  - Garante comunicação correta entre serviços

---

### Topo (Menor quantidade) → Testes de Sistema e Aceitação
- Justificativa:
  - Mais caros e lentos
  - Foco em fluxos críticos (ex: buscar restaurante e visualizar)
  - Devem ser bem selecionados

---

### Estratégia geral:

- Mais testes → lógica crítica (busca, avaliações)
- Menos testes → funcionalidades secundárias (compartilhamento)

---

## 5. Testes em Produção

Sim, o sistema deve utilizar testes em produção de forma controlada.

### Situações recomendadas:

**1. Testes de carga (horários de pico)**
- Problema real: lentidão
- Permite validar comportamento com usuários reais

---

**2. Feature Flags**
- Liberar funcionalidades para grupos específicos
- Ex: novas recomendações personalizadas

---

**3. Monitoramento contínuo**
- Logs e métricas de erro
- Identificação rápida de falhas (ex: avaliações sumindo)

---

**4. Testes A/B**
- Melhorar usabilidade (resolver telas confusas)

---

### Justificativa:

- Ambiente real revela problemas que testes locais não capturam
- Reduz risco de falhas críticas em larga escala
- Permite melhoria contínua da plataforma

---

## Conclusão

A estratégia de testes proposta prioriza funcionalidades críticas com base no impacto ao usuário e nos problemas reais identificados. A aplicação da pirâmide de testes garante eficiência e redução de custos, enquanto o uso controlado de testes em produção permite validar o sistema em condições reais.

Essa abordagem assegura qualidade, confiabilidade e evolução contínua da plataforma LocalEats.
