# -*- coding: utf-8 -*-
"""Comparacao mes-a-mes (6 meses) dos 3 finalistas, R$30/dia.
Modela: curva de aprendizado do Meta (CPA pior no mes 1), melhora de criativo
(CPC cai, CVR sobe) e construcao de funil (AOV sobe com bundle+bump+upsell).
Premissas explicitas; CVR = estimativa, CPC/CPM = benchmark publicado.
"""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10,"font.family":"DejaVu Sans"})

FX=5.40; B=30.0*30/FX; MARG=0.90   # B = US$/mes (~167)
MESES=np.arange(1,7)

# finalista: (nome, cpc_r,cpc_o, cvr_r,cvr_o, aov_r,aov_o, cor)
F=[
 ("Caca-palavras LP", 0.30,0.20, 0.026,0.050, 12,22, "#1f77b4"),
 ("Devocional cristao",0.32,0.20, 0.032,0.060, 11,24, "#2ca02c"),
 ("Binder de espolio", 0.85,0.55, 0.025,0.045, 22,39, "#d62728"),
]

def curva(m):  # progресso 0->1 ao longo de 6 meses
    return (m-1)/5
def learn(m):  # penalidade de fase de aprendizado: +35% CPA no mes1 -> 1.0 no mes3+
    return {1:1.35,2:1.15}.get(m,1.0)

resumo={}
fig1,ax1=plt.subplots(figsize=(11,6.5))  # lucro acumulado
fig2,ax2=plt.subplots(figsize=(11,6.5))  # vendas/mes
fig3,ax3=plt.subplots(figsize=(11,6.5))  # ROAS/mes

print(f"Orcamento fixo: R$30/dia = US${B:.0f}/mes | margem {MARG*100:.0f}%\n")
for nome,cpcr,cpco,cvrr,cvro,aovr,aovo,cor in F:
    cum=0; cums=[]; vendas=[]; roas=[]; lucros=[]
    for m in MESES:
        f=curva(m)
        cpc=cpcr+(cpco-cpcr)*f
        cvr=cvrr+(cvro-cvrr)*f
        aov=aovr+(aovo-aovr)*f
        cpa=cpc/cvr*learn(m)
        s=B/cpa; rec=s*aov; luc=rec*MARG-B
        cum+=luc
        cums.append(cum); vendas.append(s); roas.append(rec/B); lucros.append(luc)
    resumo[nome]=dict(cum=cum,vendas=sum(vendas),roas6=np.mean(roas),lucros=lucros,cums=cums)
    ax1.plot(MESES,cums,marker="o",color=cor,lw=2.5,label=nome)
    ax2.plot(MESES,vendas,marker="s",color=cor,lw=2,label=nome)
    ax3.plot(MESES,roas,marker="^",color=cor,lw=2,label=nome)
    print(f"{nome:20s} | vendas 6m: {sum(vendas):5.0f} | lucro acum 6m: US${cum:7.0f} (R${cum*FX:7.0f}) | ROAS medio {np.mean(roas):.2f}x")

ax1.axhline(0,color="k",lw=1,ls="--"); ax1.set_xlabel("Mes"); ax1.set_ylabel("Lucro/prejuizo ACUMULADO (US$)")
ax1.set_title("FINALISTAS | Lucro acumulado em 6 meses a R$30/dia\nabaixo de 0 = ainda no vermelho; cruzamento = break-even no tempo",fontweight="bold")
ax1.legend(); ax1.grid(alpha=.3)
fig1.tight_layout(); fig1.savefig("/home/user/Projeto-novo/analise/13_finalistas_lucro_acum.png",dpi=140)

ax2.set_xlabel("Mes"); ax2.set_ylabel("Vendas no mes")
ax2.set_title("FINALISTAS | Vendas/mes a R$30/dia (melhora com criativo + funil)",fontweight="bold")
ax2.legend(); ax2.grid(alpha=.3)
fig2.tight_layout(); fig2.savefig("/home/user/Projeto-novo/analise/14_finalistas_vendas.png",dpi=140)

ax3.axhline(1,color="k",ls="--",lw=1.2); ax3.text(1.05,1.02,"ROAS 1 (empata)",fontsize=8)
ax3.set_xlabel("Mes"); ax3.set_ylabel("ROAS no mes")
ax3.set_title("FINALISTAS | ROAS mes a mes (sai do vermelho ao montar funil de AOV)",fontweight="bold")
ax3.legend(); ax3.grid(alpha=.3)
fig3.tight_layout(); fig3.savefig("/home/user/Projeto-novo/analise/15_finalistas_roas.png",dpi=140)

print("\nMES A MES (lucro do mes, US$):")
print(f"{'Mes':>4s}"+"".join(f"{n[:16]:>18s}" for n,*_ in F))
for i,m in enumerate(MESES):
    print(f"{m:>4d}"+"".join(f"{resumo[n]['lucros'][i]:>18.0f}" for n,*_ in F))
print("\nGraficos 13-15 salvos.")
