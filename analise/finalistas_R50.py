# -*- coding: utf-8 -*-
"""Finalistas: R$30/dia vs R$50/dia (6 meses). Orcamento maior reduz um pouco a
penalidade da fase de aprendizado (mais conversoes/semana => otimiza mais rapido)."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10,"font.family":"DejaVu Sans"})

FX=5.40; MARG=0.90; MESES=np.arange(1,7)
F=[("Caca-palavras LP",0.30,0.20,0.026,0.050,12,22,"#1f77b4"),
   ("Devocional cristao",0.32,0.20,0.032,0.060,11,24,"#2ca02c"),
   ("Binder de espolio",0.85,0.55,0.025,0.045,22,39,"#d62728")]

def curva(m): return (m-1)/5
def learn(m,reais_dia):
    # R$50/dia => mais volume => penalidade de aprendizado menor e some 1 mes antes
    if reais_dia>=50: return {1:1.25,2:1.07}.get(m,1.0)
    return {1:1.35,2:1.15}.get(m,1.0)

def roda(nome,cpcr,cpco,cvrr,cvro,aovr,aovo,reais_dia):
    B=reais_dia*30/FX; cum=0; cums=[]; vendas=[]; lucros=[]; roas=[]
    for m in MESES:
        f=curva(m); cpc=cpcr+(cpco-cpcr)*f; cvr=cvrr+(cvro-cvrr)*f; aov=aovr+(aovo-aovr)*f
        cpa=cpc/cvr*learn(m,reais_dia); s=B/cpa; rec=s*aov; luc=rec*MARG-B
        cum+=luc; cums.append(cum); vendas.append(s); lucros.append(luc); roas.append(rec/B)
    return dict(B=B,cum=cum,cums=cums,vendas=sum(vendas),lucros=lucros,roas=np.mean(roas))

# ===== GRAFICO: lucro acumulado, R30 (tracejado) vs R50 (cheio) =====
fig,ax=plt.subplots(figsize=(11.5,7))
print(f"{'Produto':20s}{'verba':>8s}{'vendas6m':>10s}{'lucro6m US$':>13s}{'lucro6m R$':>12s}{'ROAS':>7s}{'breakeven':>11s}")
res={}
for nome,cpcr,cpco,cvrr,cvro,aovr,aovo,cor in F:
    r30=roda(nome,cpcr,cpco,cvrr,cvro,aovr,aovo,30)
    r50=roda(nome,cpcr,cpco,cvrr,cvro,aovr,aovo,50)
    res[nome]=(r30,r50)
    ax.plot(MESES,r30["cums"],ls="--",color=cor,lw=1.8,alpha=.7,label=f"{nome} — R$30")
    ax.plot(MESES,r50["cums"],ls="-",color=cor,lw=2.8,label=f"{nome} — R$50")
    # mes de break-even acumulado
    be30=next((m for m,c in zip(MESES,r30["cums"]) if c>0),"-")
    be50=next((m for m,c in zip(MESES,r50["cums"]) if c>0),"-")
    for tag,r,be in [("R$30",r30,be30),("R$50",r50,be50)]:
        print(f"{nome:20s}{tag:>8s}{r['vendas']:>10.0f}{r['cum']:>13.0f}{r['cum']*FX:>12.0f}{r['roas']:>7.2f}{'mes '+str(be):>11s}")
ax.axhline(0,color="k",ls=":",lw=1)
ax.set_xlabel("Mes"); ax.set_ylabel("Lucro acumulado (US$)")
ax.set_title("FINALISTAS | R$30/dia (tracejado) vs R$50/dia (cheio) — 6 meses\nR$50 acelera a saida do vermelho e amplia o lucro mais que proporcionalmente",fontweight="bold")
ax.legend(fontsize=8,ncol=1,loc="upper left"); ax.grid(alpha=.3)
plt.tight_layout(); plt.savefig("/home/user/Projeto-novo/analise/16_finalistas_R30_vs_R50.png",dpi=140)

print("\nMES A MES (lucro do mes a R$50/dia, US$):")
print(f"{'Mes':>4s}"+"".join(f"{n[:16]:>18s}" for n,*_ in F))
for i,m in enumerate(MESES):
    print(f"{m:>4d}"+"".join(f"{res[n][1]['lucros'][i]:>18.0f}" for n,*_ in F))
print("\nGrafico 16 salvo.")
