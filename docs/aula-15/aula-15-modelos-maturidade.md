# Aula 15 – Modelos de Maturidade
 
## Integrantes
 
- Alberto Ucker Parker
- Eduardo Leal

---
 
# 1. Diagnóstico de Maturidade
 
| Critério | Sim | Parcial | Não |
|-----------|-----|---------|-----|
| Os requisitos são documentados? | | X | |
| Existe controle de mudanças? | | | X |
| Há atividades de teste definidas? | | X | |
| Os defeitos são registrados? | | | X |
| O processo de desenvolvimento é conhecido por toda a equipe? | X | | |
| As tarefas são planejadas e acompanhadas regularmente? | | X | |
| Existe padronização para implementação de funcionalidades? | | X | |
| Os testes são executados antes da entrega das funcionalidades? | | X | |
| Há revisão de código ou validação por outro integrante da equipe? | | X | |
| A equipe utiliza ferramentas para gerenciamento das atividades? | X | | |
| Os artefatos do projeto são organizados e versionados? | X | | |
| Existe rastreabilidade entre requisitos e funcionalidades? | | | X |
| A equipe realiza retrospectivas ou reuniões de melhoria? | | X | |
| Existem métricas para acompanhar a qualidade? | | | X |
 
### Nível de maturidade estimado
 
**Nível 2 – Gerenciado (CMMI) / Nível G – Gerenciado (MPS.BR)**
 
### Justificativa
 
A equipe do LocalEats demonstra características de um processo no nível **Gerenciado**, pois utiliza ferramentas de versionamento (Git/GitHub) e mantém os artefatos organizados no repositório, além de possuir ao menos uma noção compartilhada do processo entre os membros. Os requisitos existem, mas de forma parcial e informal, sem rastreabilidade formal entre eles e as funcionalidades implementadas. Há indícios de testes antes das entregas e alguma revisão entre integrantes, porém sem padronização definida. Por outro lado, não existe controle formal de mudanças, os defeitos não são registrados sistematicamente e não há métricas de qualidade estabelecidas. Isso impede a equipe de avançar para o nível **Definido**, onde os processos seriam documentados, padronizados e aplicados de forma consistente. O cenário atual é típico de equipes acadêmicas em desenvolvimento: há consciência sobre boas práticas, uso básico de ferramentas, mas ainda falta formalização, rastreabilidade e monitoramento contínuo da qualidade.
 
---
 
# 2. Lacunas Identificadas
 
| Lacuna | Impacto |
|--------|---------|
| Ausência de rastreabilidade entre requisitos e funcionalidades | Dificulta o controle de mudanças e a verificação de cobertura dos requisitos implementados |
| Falta de registro formal de defeitos | Impede a análise de padrões de falha e a melhoria preventiva do processo |
| Inexistência de métricas de qualidade | Impossibilita acompanhar a evolução do projeto e identificar gargalos de forma objetiva |
| Controle de mudanças ausente | Alterações no escopo ocorrem sem avaliação de impacto, aumentando o risco de retrabalho |
| Processo de testes sem padronização formal | Gera inconsistência na cobertura de testes entre funcionalidades entregues |
 
---
 
# 3. Propostas de Melhoria
 
| Melhoria | Benefício |
|----------|-----------|
| Criar e manter um documento de requisitos versionado com IDs rastreáveis | Permite vincular cada funcionalidade a um requisito, facilitando controle de escopo e mudanças |
| Adotar um template simples de registro de defeitos (ex.: issue no GitHub com labels) | Centraliza os problemas encontrados, possibilita análise de recorrência e melhora a priorização de correções |
| Definir métricas básicas de qualidade (ex.: taxa de defeitos por entrega, cobertura de testes) | Torna o progresso do projeto mensurável e apoia decisões baseadas em dados |
| Formalizar um checklist de revisão de código entre os integrantes antes de cada merge | Reduz a introdução de defeitos no código principal e distribui o conhecimento entre a equipe |
| Estabelecer um processo mínimo de controle de mudanças (ex.: abertura de issue antes de alterar requisitos) | Garante que impactos sejam avaliados antes da implementação, reduzindo retrabalho |
 
---
 
## Conclusão
 
O processo atual do LocalEats apresenta características consolidadas de um nível **Gerenciado** (CMMI Nível 2 / MPS.BR Nível G), com uso de versionamento, algum planejamento de tarefas e consciência coletiva do processo. Entretanto, a ausência de rastreabilidade, métricas e controle formal de defeitos e mudanças são barreiras claras para avançar ao nível **Definido**. A adoção das melhorias propostas — especialmente o registro estruturado de requisitos, defeitos e métricas simples — permitiria à equipe evoluir para um processo mais previsível, consistente e com maior qualidade nas entregas.