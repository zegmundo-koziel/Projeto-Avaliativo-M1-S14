# ==============================================================================
# ESTRUTURAÇÃO DO PROJETO DE MACHINE LEARNING
# ==============================================================================

# --- FASE 1 & 2: Análise Exploratória, Tratamento e Limpeza (Data Prep) ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- FASE 1: Análise Exploratória de Dados (EDA) ---

# Carregar o arquivo CSV para um DataFrame do Pandas
df = pd.read_csv('credit_risk_dataset.csv')

# Exibir as primeiras 5 linhas para verificar se os dados carregaram corretamente
print("--- Primeiras Linhas do Dataset ---")
print(df.head())

# Exibir informações gerais sobre o tipo das colunas e dados nulos
print("\n--- Informações Gerais do Dataset ---")
print(df.info())
