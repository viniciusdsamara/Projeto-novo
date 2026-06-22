# -*- coding: utf-8 -*-
"""Simulacao realista de vendas - Chair Yoga 60+ via Meta Ads, R$30/dia.
Sem floreio: benchmarks de mercado, 3 cenarios + Monte Carlo de variancia.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

np.random.seed(7)
plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})

# ---------------- PREMISSAS (declaradas) ----------------
FX = 5.40                 # R$ por US$ (premissa)
BUDGET_BRL = 30.0
BUDGET_USD = BUDGET_BRL / FX      # ~5.56/dia
DIAS = 90

# Benchmarks cold traffic Meta, EUA, publico 50+, produto digital low-ticket
# (CPC link click; conversao clique->compra; AOV com order bump/upsell)
cenarios = {
    "Otimista":  dict(cpc=0.50, conv=0.035, aov=20, cor="#1a9850"),
    "Realista":  dict(cpc=0.90, conv=0.020, aov=17, cor="#f08c00"),
    "Pessimista":dict(cpc=1.50, conv=0.010, aov=15, cor="#d73027"),
}

print(f"Orcamento: R${BUDGET_BRL:.0f}/dia = US${BUDGET_USD:.2f}/dia (FX={FX})")
print(f"Mensal: R${BUDGET_BRL*30:.0f} = US${BUDGET_USD*30:.0f}\n")
print(f"{'Cenario':12s}{'cliques/dia':>12s}{'vendas/dia':>12s}{'1 venda a cada':>16s}{'CPA US$':>10s}{'receita/dia':>12s}{'lucro/dia':>11s}{'ROAS':>7s}")
resumo = {}
for nome, c in cenarios.items():
    clicks = BUDGET_USD / c["cpc"]
    sales = clicks * c["conv"]
    cpa = BUDGET_USD / sales if sales > 0 else float("inf")
    rev = sales * c["aov"]
    lucro = rev - BUDGET_USD
    roas = rev / BUDGET_USD
    dias_p_venda = 1/sales
    resumo[nome] = dict(sales=sales, rev=rev, lucro=lucro, roas=roas, cpa=cpa)
    print(f"{nome:12s}{clicks:12.1f}{sales:12.3f}{dias_p_venda:14.1f}d{cpa:10.2f}{rev:12.2f}{lucro:+11.2f}{roas:7.2f}x")

# ===============================================================
# GRAFICO 1 - 90 dias: gasto acumulado x receita acumulada
# ===============================================================
fig, ax = plt.subplots(figsize=(11, 6.5))
dias = np.arange(1, DIAS+1)
gasto = dias * BUDGET_USD
ax.plot(dias, gasto, "k--", lw=2, label="Gasto acumulado (R$30/dia)")
for nome, c in cenarios.items():
    sales_d = BUDGET_USD / c["cpc"] * c["conv"]
    rev = dias * sales_d * c["aov"]
    ax.plot(dias, rev, color=c["cor"], lw=2.5, label=f"Receita - {nome} (ROAS {resumo[nome]['roas']:.2f}x)")
ax.fill_between(dias, gasto, dias*(BUDGET_USD/cenarios['Realista']['cpc']*cenarios['Realista']['conv'])*cenarios['Realista']['aov'],
                where=(gasto > dias*(BUDGET_USD/cenarios['Realista']['cpc']*cenarios['Realista']['conv'])*cenarios['Realista']['aov']),
                color="red", alpha=0.06)
ax.set_xlabel("Dias de campanha")
ax.set_ylabel("US$ acumulado")
ax.set_title("SIMULACAO | 90 dias: Gasto x Receita (cold traffic, R$30/dia)\n"
             "linha preta = quanto voce gastou | so o cenario OTIMISTA fica acima dela",
             fontweight="bold", fontsize=12)
ax.legend(loc="upper left", framealpha=0.95)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("/home/user/Projeto-novo/analise/5_sim_90dias.png", dpi=140)
plt.close()

# ===============================================================
# GRAFICO 2 - FRONTEIRA DE BREAK-EVEN (o que precisa ser verdade)
# eixo x = CPC, eixo y = conversao; cor = lucro mensal US$ (AOV realista 17)
# ===============================================================
AOV = 17
cpc_grid = np.linspace(0.30, 1.80, 200)
conv_grid = np.linspace(0.005, 0.06, 200)
CPC, CONV = np.meshgrid(cpc_grid, conv_grid)
sales_day = (BUDGET_USD / CPC) * CONV
lucro_mes = (sales_day * AOV - BUDGET_USD) * 30
fig, ax = plt.subplots(figsize=(11, 7))
cmap = LinearSegmentedColormap.from_list("pl", ["#d73027", "#fee08b", "#1a9850"])
vmax = np.abs(lucro_mes).max()
im = ax.pcolormesh(CPC, CONV*100, lucro_mes, cmap=cmap, vmin=-vmax, vmax=vmax, shading="auto")
cs = ax.contour(CPC, CONV*100, lucro_mes, levels=[0], colors="black", linewidths=2.5)
ax.clabel(cs, fmt="BREAK-EVEN", fontsize=10)
# marcadores dos cenarios
for nome, c in cenarios.items():
    ax.scatter(c["cpc"], c["conv"]*100, s=160, color=c["cor"], edgecolor="black", zorder=5)
    ax.annotate(nome, (c["cpc"], c["conv"]*100), xytext=(8,6), textcoords="offset points",
                fontweight="bold", fontsize=10)
cb = plt.colorbar(im, ax=ax); cb.set_label("Lucro/prejuizo MENSAL (US$) a R$30/dia")
ax.set_xlabel("CPC - custo por clique (US$)  ->  menor = melhor")
ax.set_ylabel("Taxa de conversao do clique em venda (%)  ->  maior = melhor")
ax.set_title("SIMULACAO | O que precisa ser VERDADE para dar lucro\n"
             "acima da linha preta = lucro | abaixo = prejuizo (AOV=US$17)",
             fontweight="bold", fontsize=12)
plt.tight_layout()
plt.savefig("/home/user/Projeto-novo/analise/6_break_even.png", dpi=140)
plt.close()

# ===============================================================
# GRAFICO 3 - MONTE CARLO: como as vendas REALMENTE chegam (cenario realista)
# 5000 simulacoes de um mes (30 dias), vendas ~ Poisson
# ===============================================================
c = cenarios["Realista"]
lam_dia = BUDGET_USD / c["cpc"] * c["conv"]   # ~0.124 vendas/dia
N = 5000
vendas_mes = np.random.poisson(lam_dia*30, N)
fig, ax = plt.subplots(figsize=(11, 6.2))
vals, counts = np.unique(vendas_mes, return_counts=True)
ax.bar(vals, counts/N*100, color="#f08c00", edgecolor="black")
media = vendas_mes.mean()
ax.axvline(media, color="black", ls="--", lw=2, label=f"media = {media:.1f} vendas/mes")
ax.axvline(30, color="#1a9850", ls="-", lw=2.5, label="META: 30 vendas/mes (1/dia)")
ax.set_xlabel("Vendas em 1 mes (30 dias)")
ax.set_ylabel("% das simulacoes")
ax.set_title("SIMULACAO | Cenario REALISTA: distribuicao de vendas/mes (5.000 simulacoes)\n"
             "a meta de 1 venda/dia (verde) esta MUITO longe da realidade a R$30/dia",
             fontweight="bold", fontsize=12)
ax.set_xlim(-0.5, 31)
ax.legend()
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("/home/user/Projeto-novo/analise/7_montecarlo.png", dpi=140)
plt.close()

prob_0 = (vendas_mes==0).mean()*100
print(f"\nMonte Carlo (realista): media {media:.1f} vendas/mes; "
      f"P(0 vendas no mes)={prob_0:.0f}%; P(>=30 vendas)={(vendas_mes>=30).mean()*100:.1f}%")
print("Graficos 5,6,7 salvos.")
