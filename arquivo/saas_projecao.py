# -*- coding: utf-8 -*-
"""SaaS / micro-SaaS: projecao realista 24 meses (3 cenarios) + caixa acumulado vs servico.
Base: 5 analistas. Cambio US$1=R$5,40. Premissa: fundador solo em paralelo, do zero.
Cenarios calibrados pelos benchmarks: ~70% morre (~R$0), ~25% realista, ~5% sucesso."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10,"font.family":"DejaVu Sans"})

m24=np.arange(1,25)
# MRR mensal (R$) por cenario
fracasso=np.array([0,0,30,50,50,30,0,0,0,0,0,0]+[0]*12,float)          # ~70%: morre no vale 18m
realista=np.array([0,50,150,300,600,1000,1400,1900,2400,3000,3600,4300, # ~25%
                   5000,5700,6500,7200,7900,8600,9200,9700,10100,10400,10600,10800],float)
sucesso=np.array([0,200,600,1200,2200,4000,6000,8500,11000,13500,16000,18500, # ~5%
                  22000,26000,30000,34000,38000,43000,47000,51000,54000,57000,59000,61000],float)

fig,ax=plt.subplots(figsize=(12,7.5))
ax.plot(m24,sucesso,"-o",color="#2ca02c",lw=2.3,ms=3,label="Sucesso (~5% chegam aqui)")
ax.plot(m24,realista,"-o",color="#1f77b4",lw=2.3,ms=3,label="Realista (~25% sobrevivem)")
ax.plot(m24,fracasso,"-o",color="#d62728",lw=2.3,ms=3,label="Fracasso provavel (~70%) — morre")
for y,c,lbl in [(sucesso,"#2ca02c","R$61k/m"),(realista,"#1f77b4","R$10,8k/m"),(fracasso,"#d62728","R$0")]:
    ax.annotate(lbl,(24,y[-1]),xytext=(5,0),textcoords="offset points",fontsize=8.5,color=c,fontweight="bold",va="center")
ax.axvline(6,ls=":",color="gray"); ax.axvline(12,ls=":",color="gray"); ax.axvline(18,ls=":",color="gray")
ax.text(18,ax.get_ylim()[1]*0.0+1500,"  vale dos 18m\n  (92% morrem ate aqui)",fontsize=8,color="#d62728")
ax.set_xlabel("Mes"); ax.set_ylabel("MRR — receita recorrente mensal (R$)")
ax.set_title("SaaS solo bootstrapped — projecao realista de MRR (24 meses)\no caso MAIS PROVAVEL e a linha vermelha (zero)",fontweight="bold")
ax.legend(loc="upper left"); ax.grid(alpha=.3); ax.set_xticks([1,3,6,9,12,15,18,21,24])
plt.tight_layout(); plt.savefig("/home/user/Projeto-novo/analise/21_saas_mrr_24m.png",dpi=140); plt.close()

# CAIXA ACUMULADO 12 meses: SaaS (investimento+burn-receita) vs Tutoria de idiomas
rev_saas=realista[:12]
invest=3000.0; burn=600.0
caixa_saas=np.cumsum(rev_saas-burn) - invest
tut=np.array([150,500,900,1300,1700,2000,2300,2400,2500,2500,2500,2500],float)
caixa_tut=np.cumsum(tut)
fig,ax=plt.subplots(figsize=(12,7))
ax.axhline(0,color="k",lw=1)
ax.plot(np.arange(1,13),caixa_saas,"-o",color="#1f77b4",lw=2.6,label="SaaS (realista): -R$3k investido + R$600/m de custo")
ax.plot(np.arange(1,13),caixa_tut,"-o",color="#d62728",lw=2.6,label="Tutoria de idiomas (servico, do gr. anterior)")
ax.fill_between(np.arange(1,13),caixa_saas,0,where=(caixa_saas<0),color="#1f77b4",alpha=.12)
# ponto de equilibrio SaaS
be=np.where(caixa_saas>=0)[0]
if len(be): ax.annotate(f"SaaS volta ao zero\nso no mes {be[0]+1}",(be[0]+1,0),xytext=(be[0]+1,-2500),fontsize=9,color="#1f77b4",ha="center",arrowprops=dict(arrowstyle="->",color="#1f77b4"))
ax.annotate(f"R${caixa_saas[-1]:,.0f}".replace(",","."),(12,caixa_saas[-1]),xytext=(6,0),textcoords="offset points",color="#1f77b4",fontweight="bold",fontsize=9)
ax.annotate(f"R${caixa_tut[-1]:,.0f}".replace(",","."),(12,caixa_tut[-1]),xytext=(6,0),textcoords="offset points",color="#d62728",fontweight="bold",fontsize=9)
ax.set_xlabel("Mes"); ax.set_ylabel("Caixa ACUMULADO no bolso (R$)")
ax.set_title("O que importa: caixa no bolso em 12 meses\nSaaS fica MESES no vermelho; servico e positivo desde o mes 1",fontweight="bold")
ax.legend(loc="upper left"); ax.grid(alpha=.3); ax.set_xticks(np.arange(1,13))
plt.tight_layout(); plt.savefig("/home/user/Projeto-novo/analise/22_caixa_saas_vs_servico.png",dpi=140); plt.close()

print("SaaS MRR realista: M6=R$%.0f  M12=R$%.0f  M24=R$%.0f"%(realista[5],realista[11],realista[23]))
print("Caixa SaaS 12m: R$%.0f  | Caixa Tutoria 12m: R$%.0f"%(caixa_saas[-1],caixa_tut[-1]))
print("SaaS volta ao zero no mes:", (be[0]+1) if len(be) else ">12")
print("Graficos 21,22 salvos.")
