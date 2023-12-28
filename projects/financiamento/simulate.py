from utils import *
import streamlit as st


prazo_em_meses = 360 # 30 anos
taxa_de_juros_ao_ano = 0.1139
taxa_livre_de_risco = converte_para_taxa_mensal(0.1341)
taxa_de_juros_ao_mes = converte_para_taxa_mensal(taxa_de_juros_ao_ano)

valor_do_imovel = 520000
valor_da_entrada = 300000

valor_do_financiamento = valor_do_imovel - valor_da_entrada
fracao_entrada = valor_da_entrada/valor_do_imovel

df = simula_financiamento(valor_do_imovel, valor_da_entrada, taxa_de_juros_ao_ano, prazo_em_meses)

st.dataframe(df, hide_index=True)
