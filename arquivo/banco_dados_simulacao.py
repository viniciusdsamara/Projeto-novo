# -*- coding: utf-8 -*-
"""BANCO DE DADOS + SIMULACAO investimento->retorno por produto.
Consolidacao de 11+ analistas. Fontes: WordStream/TripleWhale/Madgicx (CPC/CPM/CVR),
Meta Ad Library ao vivo (concorrencia paga), Etsy/Amazon/Gumroad/ClickBank (preco/AOV),
AARP/Pew/CDC/National Gardening Survey (demografia).
ATENCAO: CPC/CPM = benchmark publicado (DADO). CVR clique->compra = ESTIMATIVA ancorada
em mediana e-commerce 1,57%. Validar com pixel proprio.
"""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np, csv
from matplotlib.patches import Patch
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans"})

FX = 5.40
B_DIA_BRL = 30.0
B_MES_USD = B_DIA_BRL*30/FX     # ~167
MARGEM = 0.90                   # apos taxa plataforma+pagamento+reembolso

# ---------- BANCO DE DADOS (12 produtos: 10 publico maduro + 2 wildcards) ----------
# campos: nome, idade, genero%F, comprador!=usuario, demanda, prova, conc_paga_real,
# risco_anuncio, brecha, facil_ia, aov_bump(real), aov_bundle(otim),
# cpc_real, cvr_real, cpc_otim, cvr_otim, fb_ads_reais, publico_tam(1-3)
P = [
 ("Chair Yoga senior",        "50-65","75","parcial",9,9,5,6,8,9, 12,22, 0.55,0.016, 0.35,0.030, 3102, 3),
 ("Prevencao de quedas",      "45-60","70","SIM",    8,7,4,7,7,9, 10,20, 0.80,0.014, 0.50,0.028, 240, 2),
 ("Jogos cognitivos (LP)",    "50-70","65","parcial",9,8,2,6,4,8, 11,22, 0.42,0.022, 0.28,0.040, 5, 3),
 ("Binder de espolio",        "50-68","70","misto",  9,9,3,3,6,7, 22,39, 0.85,0.025, 0.55,0.045, 298, 2),
 ("Organizador cuidador",     "45-60","59","SIM",    8,6,2,4,7,8, 16,30, 0.75,0.020, 0.48,0.038, 7, 3),
 ("Devocional cristao",       "30-60","80","nao",    9,8,8,5,4,9, 11,24, 0.32,0.032, 0.20,0.060, 579, 3),
 ("Caca-palavras (LP)",       "45-65","70","parcial",8,9,2,2,5,6, 12,22, 0.30,0.026, 0.20,0.050, 71, 3),
 ("Planejador jardinagem",    "35-60","65","nao",    8,6,2,2,7,9, 10,20, 0.45,0.022, 0.30,0.042, 7, 3),
 ("Plano anti-inflamatorio",  "35-60","70","nao",    8,8,7,9,6,8, 13,30, 0.80,0.017, 0.50,0.032, 343, 3),
 ("Genealogia",               "55-70","60","parcial",8,8,2,3,6,9, 14,32, 0.50,0.023, 0.33,0.043, 50, 2),
 ("ADHD planner (wild)",      "25-45","75","nao",    9,9,4,3,6,8, 17,35, 0.50,0.022, 0.40,0.035, 120, 3),
 ("Autocuidado/journal (wild)","20-40","80","nao",   9,8,5,4,6,8, 18,31, 0.45,0.022, 0.40,0.035, 200, 3),
]
nomes = [p[0] for p in P]
demanda   = np.array([p[4] for p in P]); prova = np.array([p[5] for p in P])
conc_paga = np.array([p[6] for p in P]); risco = np.array([p[7] for p in P])
brecha    = np.array([p[8] for p in P]); facil = np.array([p[9] for p in P])
aov_real  = np.array([p[10] for p in P],float); aov_otim = np.array([p[11] for p in P],float)
cpc_r=np.array([p[12] for p in P]); cvr_r=np.array([p[13] for p in P])
cpc_o=np.array([p[14] for p in P]); cvr_o=np.array([p[15] for p in P])
fb_ads=np.array([p[16] for p in P]); tam=np.array([p[17] for p in P])

# ---------- SIMULACAO ----------
cpa_r = cpc_r/cvr_r                  # custo por venda - cenario frio realista
cpa_o = cpc_o/cvr_o                  # custo por venda - funil otimizado
breakeven_aov = cpa_r/MARGEM         # ticket minimo p/ nao ter prejuizo (realista)
roas_r = aov_real/cpa_r              # ROAS bruto realista
roas_o = aov_otim/cpa_o              # ROAS bruto otimizado

def projeta(B, cpa, aov):
    vendas = B/cpa
    receita = vendas*aov
    lucro = receita*MARGEM - B
    return vendas, receita, lucro

# no orcamento do usuario (R$30/dia = ~$167/mes)
v_r,rec_r,luc_r = projeta(B_MES_USD, cpa_r, aov_real)
v_o,rec_o,luc_o = projeta(B_MES_USD, cpa_o, aov_otim)
# investimento p/ 30 vendas/mes (1/dia) no cenario realista
inv_30 = 30*cpa_r

# ---------- EXPORTA CSV ----------
csv_path="/home/user/Projeto-novo/analise/banco_dados_nichos.csv"
with open(csv_path,"w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["produto","idade_dominante","genero_%F","comprador!=usuario","demanda_0-10",
        "prova_venda_0-10","concorrencia_paga_real_0-10","risco_anuncio_0-10","brecha_0-10",
        "facilidade_IA_0-10","AOV_real_US$","AOV_bundle_US$","CPC_real","CVR_real","CPA_real_US$",
        "breakeven_AOV_US$","ROAS_real","ROAS_otim","ads_ativos_meta","invest_p/30vendas_US$/mes"])
    for i,p in enumerate(P):
        w.writerow([p[0],p[1],p[2],p[3],demanda[i],prova[i],conc_paga[i],risco[i],brecha[i],
            facil[i],aov_real[i],aov_otim[i],round(cpc_r[i],2),cvr_r[i],round(cpa_r[i],1),
            round(breakeven_aov[i],1),round(roas_r[i],2),round(roas_o[i],2),fb_ads[i],round(inv_30[i])])

# ---------- SCORE DE VIABILIDADE EM TRAFEGO PAGO (0-100) ----------
def nrm(x): return (x-x.min())/(x.max()-x.min())
viab = (nrm(roas_o)*32 + (demanda/10)*14 + (brecha/10)*12 + (facil/10)*8
        + ((10-conc_paga)/10)*14 + ((10-risco)/10)*20)
# penaliza quem nao alcanca breakeven nem com bundle otimizado
pen = np.clip(breakeven_aov-aov_otim,0,None)*1.5
viab = np.clip(viab-pen,0,100)

ordem=np.argsort(viab)
def corv(s): return "#1a9850" if s>=70 else "#91cf60" if s>=58 else "#fee08b" if s>=45 else "#d73027"

# ===== GRAFICO A: Score de viabilidade =====
fig,ax=plt.subplots(figsize=(11.5,7))
b=ax.barh([nomes[i] for i in ordem],viab[ordem],color=[corv(viab[i]) for i in ordem],edgecolor="k",lw=.6)
for i,bb in zip(ordem,b):
    ax.text(viab[i]+0.6,bb.get_y()+bb.get_height()/2,
            f"{viab[i]:.0f} | ROAS otim {roas_o[i]:.1f}x | risco {risco[i]}",va="center",fontsize=8.5)
ax.set_xlim(0,100); ax.set_xlabel("Score de Viabilidade em Trafego Pago (0-100)")
ax.set_title("BANCO DE DADOS | Viabilidade em trafego pago dos 12 nichos\n(ROAS potencial + demanda + brecha + facil.IA + baixa concorrencia paga + baixo risco)",fontweight="bold")
ax.legend(handles=[Patch(facecolor="#1a9850",label="Forte"),Patch(facecolor="#91cf60",label="Bom"),
    Patch(facecolor="#fee08b",label="Marginal"),Patch(facecolor="#d73027",label="Fraco")],loc="lower right")
plt.tight_layout(); plt.savefig("/home/user/Projeto-novo/analise/8_score_viabilidade.png",dpi=140); plt.close()

# ===== GRAFICO B: break-even AOV vs AOV alcancavel =====
fig,ax=plt.subplots(figsize=(11.5,7))
idx=np.argsort(breakeven_aov); y=np.arange(len(P))
ax.barh(y-0.2,[breakeven_aov[i] for i in idx],0.4,label="Ticket de break-even (CPC realista)",color="#d73027")
ax.barh(y+0.2,[aov_otim[i] for i in idx],0.4,label="AOV alcancavel c/ bundle+bump+upsell",color="#1a9850")
ax.set_yticks(y); ax.set_yticklabels([nomes[i] for i in idx])
ax.set_xlabel("US$ por venda")
ax.set_title("BANCO DE DADOS | Para dar lucro, a BARRA VERDE precisa passar a VERMELHA\nverde<vermelho = inviavel mesmo com bundle (ex.: prevencao de quedas, anti-inflamatorio)",fontweight="bold")
ax.legend(loc="lower right")
plt.tight_layout(); plt.savefig("/home/user/Projeto-novo/analise/9_breakeven_vs_aov.png",dpi=140); plt.close()

# ===== GRAFICO C: ROAS dois cenarios =====
fig,ax=plt.subplots(figsize=(11.5,7))
idx=np.argsort(roas_o); y=np.arange(len(P))
ax.barh(y-0.2,[roas_r[i] for i in idx],0.4,label="Cenario FRIO realista",color="#f08c00")
ax.barh(y+0.2,[roas_o[i] for i in idx],0.4,label="Funil OTIMIZADO (bundle+criativo vencedor)",color="#1a9850")
ax.axvline(1.0,color="k",ls="--",lw=1.5); ax.text(1.02,0.3,"ROAS 1 (empata)",rotation=90,fontsize=8)
ax.set_yticks(y); ax.set_yticklabels([nomes[i] for i in idx]); ax.set_xlabel("ROAS (receita / gasto)")
ax.set_title("BANCO DE DADOS | ROAS por produto: frio (realista) vs funil otimizado\nquase tudo perde no frio; so devocional/caca-palavras/jogos chegam perto de empatar",fontweight="bold")
ax.legend(loc="lower right")
plt.tight_layout(); plt.savefig("/home/user/Projeto-novo/analise/10_roas_dois_cenarios.png",dpi=140); plt.close()

# ===== GRAFICO D: investimento p/ 1 venda/dia (30/mes) =====
fig,ax=plt.subplots(figsize=(11.5,7))
idx=np.argsort(inv_30)
cores=["#1a9850" if inv_30[i]<450 else "#fee08b" if inv_30[i]<900 else "#d73027" for i in idx]
b=ax.barh([nomes[i] for i in idx],[inv_30[i] for i in idx],color=cores,edgecolor="k",lw=.6)
for i,bb in zip(idx,b):
    ax.text(inv_30[i]+8,bb.get_y()+bb.get_height()/2,f"US${inv_30[i]:.0f} (R${inv_30[i]*FX:.0f})/mes",va="center",fontsize=8)
ax.axvline(B_MES_USD,color="blue",ls="--",lw=1.5); ax.text(B_MES_USD+4,0.2,f"seu orcamento atual\nR$900 (US${B_MES_USD:.0f})/mes",fontsize=8,color="blue")
ax.set_xlabel("Investimento/mes para captar ~30 vendas (1/dia) no CPA realista")
ax.set_title("SIMULACAO | Quanto investir para 1 venda/dia, por produto (cenario realista)\nseu orcamento atual so chega perto disso em devocional e caca-palavras",fontweight="bold")
ax.legend(handles=[Patch(facecolor="#1a9850",label="< US$450/mes"),Patch(facecolor="#fee08b",label="US$450-900"),
    Patch(facecolor="#d73027",label="> US$900/mes")],loc="lower right")
plt.tight_layout(); plt.savefig("/home/user/Projeto-novo/analise/11_investimento_1venda_dia.png",dpi=140); plt.close()

# ===== GRAFICO E: matriz viabilidade (bolha) =====
fig,ax=plt.subplots(figsize=(11.5,7.5))
from matplotlib.colors import LinearSegmentedColormap
cm=LinearSegmentedColormap.from_list("c",["#1a9850","#fee08b","#d73027"])
sc=ax.scatter(roas_o,10-risco,s=(demanda*tam*14),c=conc_paga,cmap=cm,vmin=0,vmax=10,edgecolor="k",lw=1,alpha=.9)
ax.axvline(1.5,color="gray",ls="--"); ax.axhline(6,color="gray",ls="--")
ax.text(ax.get_xlim()[1],10.3,"SWEET SPOT: ROAS alto + risco baixo ->",ha="right",fontsize=9,color="#1a6b35",fontweight="bold")
for i,n in enumerate(nomes):
    ax.annotate(n,(roas_o[i],10-risco[i]),xytext=(0,9),textcoords="offset points",ha="center",fontsize=7.8,fontweight="bold")
cb=plt.colorbar(sc); cb.set_label("Concorrencia paga REAL (verde=vazia, vermelho=lotada)")
ax.set_xlabel("ROAS potencial (funil otimizado) ->"); ax.set_ylabel("Seguranca de anuncio (10 - risco) ->")
ax.set_title("BANCO DE DADOS | Matriz de decisao: retorno x seguranca x concorrencia\ntamanho da bolha = demanda x tamanho de publico",fontweight="bold")
plt.tight_layout(); plt.savefig("/home/user/Projeto-novo/analise/12_matriz_decisao.png",dpi=140); plt.close()

# ---------- RANKING TEXTUAL ----------
print("="*100)
print("RANKING POR VIABILIDADE EM TRAFEGO PAGO")
print("="*100)
print(f"{'#':2s} {'produto':26s}{'viab':>5s}{'ROAS_frio':>10s}{'ROAS_otim':>10s}{'CPA$':>7s}{'breakeven$':>11s}{'risco':>6s}{'inv/30v':>9s}")
for r,i in enumerate(np.argsort(-viab),1):
    print(f"{r:2d} {nomes[i]:26s}{viab[i]:5.0f}{roas_r[i]:10.2f}{roas_o[i]:10.2f}{cpa_r[i]:7.1f}{breakeven_aov[i]:11.1f}{risco[i]:6d}{inv_30[i]:9.0f}")
print(f"\nOrcamento usuario: R$30/dia = US${B_MES_USD:.0f}/mes. Margem liquida {MARGEM*100:.0f}%.")
print(f"CSV salvo em {csv_path}")
print("Graficos 8-12 salvos.")
