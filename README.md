# 🏭 Sistema de Gestão de Peças — Controle de Qualidade Industrial

> **Disciplina:** Algoritmos e Lógica de Programação
> **Instituição:** UniFECAF
> **Desafio:** Automação Digital — Gestão de Peças, Qualidade e Armazenamento

---

## 👨‍🎓 Identificação

| Campo | Informação |
|---|---|
| **Aluno** | Gabriel Barbosa Silva |
| **Curso** | Algoritmos e Lógica de Programação |
| **Professor** | Fernando Leonid |
| **Tutora** | Patricia Miscolcz de Oliveira Ampese |
| **Instituição** | UniFECAF |

---

## 📋 Sobre o Projeto

Este sistema simula um processo de inspeção de qualidade industrial desenvolvido em Python.
Cada peça produzida é avaliada automaticamente com base em critérios pré-definidos. As peças aprovadas são organizadas em caixas de até 10 unidades. Ao final, o sistema gera um relatório consolidado completo.

---

## ✅ Critérios de Aprovação

| Atributo | Condição aceita |
|---|---|
| Peso | Entre 95g e 105g |
| Cor | Azul ou Verde |
| Comprimento | Entre 10cm e 20cm |

---

## 📁 Estrutura do Projeto

```
/
├── sistema_pecas.py   # Código-fonte principal
└── README.md          # Documentação do projeto
```

---

## ▶️ Como Rodar o Programa

### Pré-requisitos
- Python 3.x instalado ([download aqui](https://www.python.org/downloads/))

### Passo a passo

**1. Clone o repositório:**
```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

**2. Execute o programa:**
```bash
python sistema_pecas.py
```
> No Linux/macOS, use `python3 sistema_pecas.py`

---

## 🖥️ Menu do Sistema

```
=======================================================
  SISTEMA DE CONTROLE DE QUALIDADE INDUSTRIAL
=======================================================
  1. Cadastrar nova peça
  2. Listar peças aprovadas/reprovadas
  3. Remover peça cadastrada
  4. Listar caixas fechadas
  5. Gerar relatório final
  0. Sair do sistema
=======================================================
```

---

## 📌 Exemplos de Entrada e Saída

### Exemplo 1 — Peça APROVADA

```
Escolha uma opção: 1

  CADASTRAR NOVA PEÇA
  ID da peça gerado automaticamente: #1
  Informe o peso da peça (em gramas): 100
  Informe a cor da peça: azul
  Informe o comprimento da peça (em cm): 15

  ✅ Peça #1 APROVADA!
```

### Exemplo 2 — Peça REPROVADA (múltiplos motivos)

```
Escolha uma opção: 1

  CADASTRAR NOVA PEÇA
  ID da peça gerado automaticamente: #2
  Informe o peso da peça (em gramas): 80
  Informe a cor da peça: vermelho
  Informe o comprimento da peça (em cm): 25

  ❌ Peça #2 REPROVADA!
     • Peso fora do padrão (80.0g — aceito: 95g a 105g)
     • Cor inválida ('vermelho' — aceito: azul ou verde)
     • Comprimento fora do padrão (25.0cm — aceito: 10cm a 20cm)
```

### Exemplo 3 — Relatório Final

```
=======================================================
  RELATÓRIO FINAL CONSOLIDADO
=======================================================

  📊 RESUMO GERAL:
     Total de peças cadastradas : 3
     Total de peças aprovadas   : 2
     Total de peças reprovadas  : 1
     Caixas fechadas            : 0
     Caixa atual (em aberto)    : 2/10 peças
     Taxa de aprovação          : 66.7%

  ❌ MOTIVOS DE REPROVAÇÃO:
     • Peso fora do padrão: 1 ocorrência(s)
     • Cor inválida: 1 ocorrência(s)
     • Comprimento fora do padrão: 1 ocorrência(s)
=======================================================
```

### Exemplo 4 — Caixa fechada automaticamente

Ao cadastrar a 10ª peça aprovada, o sistema fecha a caixa automaticamente:
```
  ✅ Peça #10 APROVADA!
  📦 Caixa 1 fechada com 10 peças!
```

---

## 🧠 Lógica do Sistema

- **Funções** — cada funcionalidade está isolada em sua própria função
- **Condicionais (`if/elif/else`)** — usados para avaliar os critérios de qualidade
- **Listas** — armazenam peças cadastradas, caixa atual e caixas fechadas
- **Dicionários** — cada peça é um dicionário com seus atributos
- **Loop `while`** — mantém o menu em execução até o usuário sair
- **Variáveis globais** — compartilham o estado entre as funções

---

*Projeto acadêmico desenvolvido para o curso de Tecnologia — UniFECAF.*
