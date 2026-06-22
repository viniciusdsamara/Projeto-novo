# -*- coding: utf-8 -*-
"""Projecao realista de 6 meses para os caminhos viaveis de renda paralela (BR).
Part-time ~10-15h/sem, comecando do ZERO, valores LIQUIDOS (pos taxa de plataforma).
Cenarios: conservador / realista / otimista. Base: dados dos 5 analistas + subagentes.
Premissa-chave (honesta): a maioria comeca em ~R$0 e leva semanas/meses; estes numeros
assumem CONSISTENCIA e que voce NAO desiste (a maioria desiste)."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10,"font.family":"DejaVu Sans"})
meses=np.arange(1,7)

# renda liquida mensal REALISTA (R$) por mes 1..6
real={
 "Tutoria idiomas (italki PT, USD)":[150,500,900,1300,1700,2000],
 "Servico com IA (nicho)":         [100,400,800,1200,1600,2000],
 "Copywriting (freelance)":        [80,300,600,900,1200,1500],
 "Gestao de trafego":              [0,0,500,1000,2000,3000],
 "Templates Canva/Etsy (organico)":[0,0,50,120,250,400],
 "Infoproduto afiliado (organico)":[0,0,50,150,300,500],
}
# bandas conservador/otimista como fator sobre o realista no mes 6 (e curva proporcional)
fator={"Tutoria idiomas (italki PT, USD)":(0.55,1.5),"Servico com IA (nicho)":(0.4,1.8),
 "Copywriting (freelance)":(0.4,1.7),"Gestao de trafego":(0.2,2.2),
 "Templates Canva/Etsy (organico)":(0.3,2.5),"Infoproduto afiliado (organico)":(0.1,3.0)}
cor={"Tutoria idiomas (italki PT, USD)":"#d62728","Servico com IA (nicho)":"#1f77b4",
 "Copywriting (freelance)":"#17becf","Gestao de trafego":"#8c564b",
 "Templates Canva/Etsy (organico)":"#2ca02c","Infoproduto afiliado (organico)":"#ff7f0e"}

# GRAFICO 19: renda mensal (realista) com banda
fig,ax=plt.subplots(figsize=(12,7.5))
for k,v in real.items():
    v=np.array(v,float); c=cor[k]
    ax.plot(meses,v,"-o",color=c,lw=2.4,label=k,zorder=3)
    lo=v*fator[k][0]; hi=v*fator[k][1]
    ax.fill_between(meses,lo,hi,color=c,alpha=0.10,zorder=1)
    ax.annotate(f"R${v[-1]:.0f}",(6,v[-1]),xytext=(6,8),textcoords="offset points",fontsize=8.5,color=c,fontweight="bold")
ax.set_xlabel("Mes"); ax.set_ylabel("Renda liquida no mes (R$)")
ax.set_title("Projecao realista de 6 meses — renda paralela do ZERO (~10-15h/sem)\nlinha = cenario realista | faixa sombreada = conservador a otimista",fontweight="bold")
ax.legend(loc="upper left",fontsize=8.6); ax.grid(alpha=.3); ax.set_xticks(meses)
plt.tight_layout(); plt.savefig("/home/user/Projeto-novo/analise/19_projecao_6meses.png",dpi=140); plt.close()

# GRAFICO 20: acumulado 6 meses (3 cenarios)
fig,ax=plt.subplots(figsize=(12,7))
ks=list(real.keys())
acc_real=np.array([sum(real[k]) for k in ks])
acc_lo=np.array([sum(np.array(real[k])*fator[k][0]) for k in ks])
acc_hi=np.array([sum(np.array(real[k])*fator[k][1]) for k in ks])
o=np.argsort(acc_real); y=np.arange(len(ks))
ax.barh(y,[acc_real[i] for i in o],color=[cor[ks[i]] for i in o],edgecolor="k",lw=.5,alpha=.9)
for j,i in enumerate(o):
    ax.errorbar(acc_real[i],j,xerr=[[acc_real[i]-acc_lo[i]],[acc_hi[i]-acc_real[i]]],fmt="none",ecolor="k",capsize=4,lw=1.3)
    ax.text(acc_hi[i]+200,j,f"realista R${acc_real[i]:.0f}\n(R${acc_lo[i]:.0f} a R${acc_hi[i]:.0f})",va="center",fontsize=8)
ax.set_yticks(y); ax.set_yticklabels([ks[i] for i in o])
ax.set_xlabel("Total acumulado em 6 meses (R$)")
ax.set_title("Quanto entra no TOTAL nos primeiros 6 meses\nbarra = realista | hastes = conservador a otimista",fontweight="bold")
ax.set_xlim(0,max(acc_hi)*1.25)
plt.tight_layout(); plt.savefig("/home/user/Projeto-novo/analise/20_acumulado_6meses.png",dpi=140); plt.close()

print(f"{'caminho':34s}{'M6 realista':>12}{'6m acumulado':>14}{'faixa 6m':>22}")
for i in np.argsort(-acc_real):
    print(f"{ks[i]:34s}{real[ks[i]][-1]:>10}R${acc_real[i]:>11.0f}   R${acc_lo[i]:.0f}-{acc_hi[i]:.0f}")
print("\nGraficos 19 e 20 salvos.")
