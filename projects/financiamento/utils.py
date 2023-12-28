import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.ticker as mtick


def saldo_devedor_por_mes(mes, taxa_de_juros_ao_mes, prazo_em_meses):
    return 1 - (mes-1)/prazo_em_meses


def juros_por_mes(mes, taxa_de_juros_ao_mes, prazo_em_meses):
    return taxa_de_juros_ao_mes * saldo_devedor_por_mes(mes, taxa_de_juros_ao_mes, prazo_em_meses)


def valor_total_pago(fracao_entrada, taxa_de_juros_ao_mes, prazo_em_meses):
    return fracao_entrada + (1 - fracao_entrada)* (1 + taxa_de_juros_ao_mes * (prazo_em_meses+1)/2 )


def parcela_sobre_valor_financiado(mes, taxa_de_juros_ao_mes, prazo_em_meses):
    return 1/prazo_em_meses + juros_por_mes(mes, taxa_de_juros_ao_mes, prazo_em_meses)


def parcela_sobre_valor_do_imovel(fracao_entrada, mes, taxa_de_juros_ao_mes, prazo_em_meses):
    return (1 - fracao_entrada) * parcela_sobre_valor_financiado(mes, taxa_de_juros_ao_mes, prazo_em_meses)


def converte_para_taxa_mensal(taxa_anual):
    return (1 + taxa_anual)**(1/12)-1


def calcula_valor_presente(parcelas, taxa_livre_de_risco):
    valor_presente = (parcelas/(1+taxa_livre_de_risco)**np.arange(1,len(parcelas)+1)).sum()
    return valor_presente


def simula_financiamento(valor_do_imovel, valor_da_entrada, taxa_de_juros_ao_ano, prazo_em_meses):
    valor_do_financiamento = valor_do_imovel - valor_da_entrada
    fracao_entrada = valor_da_entrada/valor_do_imovel
    taxa_de_juros_ao_mes = converte_para_taxa_mensal(taxa_de_juros_ao_ano)

    meses = np.arange(1, prazo_em_meses + 1)
    saldo_devedor = saldo_devedor_por_mes(meses, taxa_de_juros_ao_mes, prazo_em_meses)
    juros = saldo_devedor * taxa_de_juros_ao_mes
    amortizacao = 1/prazo_em_meses
    parcelas = amortizacao + juros
    
    Saldo_devedor = valor_do_financiamento * saldo_devedor
    Juros = valor_do_financiamento * juros
    Parcelas = valor_do_financiamento * parcelas
    Amortizacao = valor_do_financiamento * amortizacao  
    
    return pd.DataFrame(
        data = {
         'mes': meses,
         'parcela': Parcelas,
         'amortizacao': Amortizacao, 
         'juros': Juros,
         'saldo_devedor': Saldo_devedor            
        }
    )