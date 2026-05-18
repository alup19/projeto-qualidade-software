# 🧩 Atividade PBL – Aula 10  
## Testes Funcionais Automatizados – LocalEats

---

## 👥 Integrante(s)
- Alberto Parker  
- Eduardo Leal  

---

## 🔹 1. Fluxo funcional escolhido

### 📌 Fluxos:
Login de usuário e Navegação e visualização de restaurantes

🔎 **Descrição**  
Permite autenticar um usuário no sistema e navegar e visualizar os restaurates disponiveis

🎯 **Importância**  
Garante acesso seguro às funcionalidades da aplicação e para que o usuário explore opções antes de realizar pedidos

---

## 🔹 2. Teste com Codegen

### 💻 Comando utilizado

```bash
python -m playwright codegen https://local-eats-unisenac.vercel.app/
```

### 🔗 Link para o código gerado

👉 https://github.com/seu-repositorio/tests/codegen_login.py
👉 https://github.com/seu-repositorio/tests/codegen_restaurantes.py

### 🧠 Observações

- O Codegen ajudou a gerar rapidamente o fluxo inicial  
- Parte do código gerado era excessiva e pouco organizada  
- Foi necessário refatorar utilizando boas práticas e POM

---

## 🔹 3. Teste automatizado com Pytest

### 🔗 Link para os testes

👉 https://github.com/seu-repositorio/tests/test_login.py
👉 https://github.com/seu-repositorio/tests/test_login.py


### 📌 O que os testes fazem?

- Acessa o sistema LocalEats  
- Executa navegação automatizada utilizando Playwright  
- Valida o carregamento correto da aplicação

- Acessa o sistema LocalEats  
- Navega pela interface de restaurantes  
- Valida o carregamento da aplicação

---

## 🔹 4. Refatoração com Page Object Model (POM)

### 🔗 Link para Page Object

👉 https://github.com/seu-repositorio/pages/login_page.py

### 🔗 Link para teste refatorado

👉 https://github.com/seu-repositorio/tests/test_login.py

### 🧠 Melhorias realizadas

- Separação entre teste e lógica de UI  
- Código mais organizado  
- Maior reutilização  

---

## 🔹 5. Execução dos testes

### ▶️ Comando

```bash
python -m pytest
```

### 📊 Resultado

- Total de testes: 2  
- Testes passaram: 2  
- Testes falharam: 0  

### 📸 Evidência

<img width="1247" height="255" alt="Captura de tela 2026-05-18 160026" src="https://github.com/user-attachments/assets/04cb7b39-ccce-41bb-a142-fd2235e4c526" />


---

## 🔹 6. Análise crítica

### O teste quebrou em algum momento? Por quê?

Sim. Alguns testes falharam devido a seletores incorretos e mudanças na interface da aplicação.

---

### Quais seletores foram mais difíceis?

Os seletores baseados em texto foram mais frágeis, pois pequenas alterações na interface podem quebrar o teste.

---

### O Codegen ajudou ou gerou problemas?

O Codegen ajudou a criar rapidamente a estrutura inicial do teste, porém gerou código excessivo e pouco organizado, exigindo refatoração manual.

---

### O teste é confiável?

Parcialmente. O teste executa corretamente, mas ainda depende de elementos da interface que podem mudar futuramente.

---

### O que tornaria o teste mais robusto?

- Uso de seletores mais estáveis  
- Melhor tratamento de espera  
- Uso de identificadores específicos (`data-testid`)  
- Maior desacoplamento da interface

---

## 🔹 7. Reflexão

### Testes automatizados substituem testes manuais?

Não. Testes manuais continuam importantes para validar usabilidade e experiência do usuário.

---

### Vale a pena automatizar todos os fluxos?

Não necessariamente. O ideal é automatizar principalmente fluxos críticos e repetitivos.

---

### Como isso ajuda no projeto?

Os testes automatizados aumentam a confiança nas alterações realizadas no sistema e ajudam a identificar erros mais rapidamente.

---

## 💡 Conclusão

A atividade permitiu compreender na prática o funcionamento de testes funcionais automatizados utilizando Playwright, Pytest e Page Object Model.

Além disso, foi possível perceber a importância de criar testes organizados, reutilizáveis e menos frágeis para facilitar a manutenção futura.
