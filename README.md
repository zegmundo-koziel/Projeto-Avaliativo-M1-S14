# Pipeline Preditivo para Análise de Risco de Crédito

## Visão Geral

Este repositório apresenta a implementação de um pipeline de Machine Learning para predição de inadimplência em operações de crédito. O objetivo é apoiar a tomada de decisão com base em critérios quantitativos e impacto financeiro, garantindo consistência técnica e reprodutibilidade.

---

## Problema de Negócio

A concessão de crédito envolve a gestão de dois riscos principais:

* **Falso Positivo (FP):** Cliente adimplente classificado como inadimplente
  *Impacto:* perda de receita por crédito negado indevidamente

* **Falso Negativo (FN):** Cliente inadimplente classificado como adimplente
  *Impacto:* prejuízo direto com perda do capital emprestado

O objetivo do modelo é minimizar o impacto financeiro total, equilibrando esses dois cenários.

---

## Base de Dados

Dataset: `credit_risk_dataset.csv`

| Variável                   | Tipo       | Descrição                                        |
| -------------------------- | ---------- | ------------------------------------------------ |
| person_age                 | Numérico   | Idade do cliente                                 |
| person_income              | Numérico   | Renda anual                                      |
| person_emp_length          | Numérico   | Tempo de emprego                                 |
| loan_amnt                  | Numérico   | Valor do empréstimo                              |
| loan_int_rate              | Numérico   | Taxa de juros                                    |
| loan_percent_income        | Numérico   | Percentual da renda comprometida                 |
| cb_person_cred_hist_length | Numérico   | Tempo de histórico de crédito                    |
| loan_status                | Categórico | Variável alvo (0 = adimplente, 1 = inadimplente) |
| comprometimento_renda      | Numérico   | Feature derivada                                 |

---

## Estrutura do Projeto

```id="d6q1hm"
/data
/notebooks
/src
/models
```

---

## Arquitetura do Pipeline

O pipeline segue boas práticas de separação e controle de vazamento de dados:

### 1. Análise Exploratória (EDA)

* Distribuição das variáveis
* Identificação de desbalanceamento
* Correlação entre variáveis
* Detecção de outliers

### 2. Tratamento de Dados

* Remoção de duplicidades
* Tratamento de valores ausentes
* Exclusão de inconsistências com base em critérios plausíveis de negócio

### 3. Feature Engineering

* Criação da variável `comprometimento_renda`

### 4. Preparação dos Dados

* Codificação de variáveis categóricas
* Divisão treino/teste (80/20 com estratificação)
* Balanceamento com SMOTE (aplicado apenas no treino)
* Padronização seletiva para modelos sensíveis à escala

### 5. Modelagem

Modelos avaliados:

* Regressão Logística (baseline)
* K-Nearest Neighbors (KNN)
* Árvore de Decisão

### 6. Validação

* Validação cruzada (k-fold)
* Avaliação com métricas: Precisão, Recall, F1-Score
* Matriz de confusão

---

## Resultados

### Desbalanceamento

* 78% adimplentes
* 22% inadimplentes

O uso de SMOTE foi necessário para balanceamento do conjunto de treino.

---

### Diagnóstico de Overfitting

A Árvore de Decisão sem restrição apresentou sobreajuste.
A configuração ideal identificada foi:

* `max_depth = 11`

---

### Comparação de Modelos

| Modelo              | Precisão (inadimplentes) | Recall | F1-Score |
| ------------------- | ------------------------ | ------ | -------- |
| Regressão Logística | (baseline)               | -      | -        |
| KNN (K=9)           | 54%                      | 79%    | ~0.64    |
| Árvore (Depth=11)   | 95%                      | 72%    | 0.82     |

---

## Análise de Impacto Financeiro

A escolha do modelo considera o impacto econômico associado aos erros:

* **FN (mais crítico):** perda direta do capital
* **FP:** perda de oportunidade de receita

O modelo de Árvore de Decisão apresentou melhor equilíbrio entre precisão e recall, reduzindo o risco de concessão indevida de crédito e mantendo a operação sustentável.

---

## Decisão de Negócio

Modelo selecionado: **Árvore de Decisão (max_depth = 11)**

**Motivos:**

* Alta precisão na identificação de inadimplentes
* Redução de falsos positivos
* Melhor equilíbrio entre risco e retorno

O modelo KNN não atende aos critérios de viabilidade operacional devido à elevada taxa de falsos positivos.

---

## Instalação e Execução

### 1. Clonar repositório

git clone https://github.com/zegmundo-koziel/Projeto-Avaliativo-M1-S14.git
cd Projeto-Avaliativo-M1-S14


### 2. Instalar dependências

pip install -r requirements.txt


### 3. Preparar dataset

* Inserir `credit_risk_dataset.csv` na raiz do projeto

### 4. Execução atual

* Abrir `main.ipynb`
* Executar as células em sequência

### 5. Evolução prevista

O pipeline será estruturado em scripts Python para execução automatizada, garantindo maior reprodutibilidade e aderência a ambientes de produção.

---

## Tecnologias Utilizadas

* Python
* Pandas / NumPy
* Scikit-learn
* Imbalanced-learn (SMOTE)
* Matplotlib / Seaborn

---

## Considerações Finais

O projeto aplica técnicas de Machine Learning com foco em:

* mitigação de risco financeiro
* controle de overfitting
* tratamento de dados desbalanceados

A abordagem prioriza decisões orientadas a impacto econômico e boas práticas de modelagem.

---

## Próximos Passos

* Estruturar pipeline com `sklearn Pipeline`
* Automatizar execução via scripts (`train.py`)
* Refinar análise de custo financeiro
* Expandir feature engineering
* Implementar monitoramento de modelo
