import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def limites(df, coluna):
    q1 = df[coluna].quantile(0.25)
    q3 = df[coluna].quantile(0.75)
    amplitude = q3 - q1
    return q1 - 1.5 * amplitude, q3 + 1.5 * amplitude


def diagrama_caixa(df, coluna):
    plt.figure(figsize=(15, 5))
    ax = sns.boxplot(x=df[coluna])
    ax.set_xlim(limites(df, coluna))


def histograma(df, coluna):
    plt.figure(figsize=(15, 5))
    sns.distplot(df[coluna], hist=True)


def grafico_barra(df, coluna):  
    plt.figure(figsize=(15, 5))
    ax = sns.barplot(x=df[coluna].value_counts().index, y=df[coluna].value_counts())
    ax.set_xlim(limites(df, coluna))


def grafico_densidade(df, coluna):
    plt.figure(figsize=(15, 5))
    sns.kdeplot(df[coluna], shade=True, bw=0.5, color='olive')
    plt.show()


def excluir_outliers(df, coluna):
    qtde_linhas = df.shape[0]
    lim_inf, lim_sup = limites(df, coluna)
    df = df.loc[(df[coluna] >= lim_inf) & (df[coluna] <= lim_sup), :]
    linhas_removidas = qtde_linhas - df.shape[0]
    return df,  linhas_removidas


def grafico_correlacao(df):
    sns.pairplot(df)
    plt.show()


def grafico_heatmap(df):
    plt.figure(figsize=(15, 10))
    sns.heatmap(df.corr(), annot=True, cmap='Greens')
