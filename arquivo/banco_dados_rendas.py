# -*- coding: utf-8 -*-
"""Banco de dados: formas de ganhar dinheiro online (renda paralela, BR).
Consolidacao de 5 analistas + subagentes. Pontuacao 0-10 por criterio.
Composite ponderado para o perfil do usuario: renda PARALELA, baixo capital,
realista, viavel do Brasil. Fontes: Workana/Glassdoor/Upwork, Gumroad dataset,
Brookings/Upwork (IA no freelance), Prolific/Outlier/italki/Preply, Hotmart/ML/Shopee.
"""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np, csv
plt.rcParams.update({"font.size":10,"font.family":"DejaVu Sans"})

# (nome, categoria, pot, custo, esforco_leve, rapidez, baixa_barreira, escala, viab_BR, renda_real)
M = [
 ("Servicos com IA (nicho)","Servico",7,7,7,8,6,7,8,"R$400-5.000/mes"),
 ("Copywriting","Servico",6,9,7,6,6,6,8,"R$300-5.000/mes"),
 ("Design grafico","Servico",6,7,6,6,5,6,8,"R$400-6.000/mes"),
 ("Edicao de video","Servico",7,5,4,6,5,6,7,"R$500-8.000/mes"),
 ("Assistente Virtual","Servico",5,9,4,8,8,3,8,"R$1.500-5.000/mes"),
 ("Social media","Servico",6,8,6,6,6,6,8,"R$500-6.000/mes"),
 ("Gestao de trafego","Servico",8,5,6,4,4,8,8,"R$500-4.000/cliente"),
 ("Reels/TikTok/Shorts","Conteudo",5,9,6,5,7,8,6,"R$0-200 fundo; marca depois"),
 ("YouTube faceless/IA","Conteudo",5,5,4,3,5,7,4,"R$0-300; so 3% monetiza"),
 ("Blog SEO + AdSense","Conteudo",6,8,5,2,5,8,4,"R$0-200; 12-18 meses"),
 ("Narracao IA (servico)","Conteudo",5,8,6,8,6,5,7,"R$0-1.500/mes"),
 ("Podcast","Conteudo",3,5,2,1,4,6,4,"~R$0; 0,1% viavel"),
 ("Etsy printables","Produto",6,9,6,5,6,8,7,"R$0-800; 65% <US$100/ano"),
 ("Templates Canva","Produto",6,10,6,4,7,8,7,"R$0-1.000/mes"),
 ("Amazon KDP low-content","Produto",5,10,6,5,6,7,6,"R$0-1.000; saturado"),
 ("Microstock IA","Produto",4,7,6,3,5,8,7,"R$0-600/mes"),
 ("Infoproduto afiliado organico","Afiliado",7,9,3,3,4,8,9,"R$0-500; 95% desistem"),
 ("Mercado Livre/Shopee afiliado","Afiliado",4,9,5,5,7,6,8,"R$50-400/mes"),
 ("Tutoria de idiomas (italki/Preply)","Microwork",5,9,6,8,6,3,8,"R$2.500-3.500 part-time"),
 ("Anotacao de dados IA (Outlier)","Microwork",5,9,6,7,6,3,5,"R$2.300-4.600 se houver tarefa; risco"),
 ("UGC creator","Microwork",5,7,5,3,5,5,5,"meses ate o 1o pagamento"),
 ("Pesquisas (so Prolific)","Microwork",2,10,7,6,9,2,6,"R$135-430/mes; resto e cilada"),
]
nomes=[m[0] for m in M]; cat=[m[1] for m in M]
arr=np.array([[m[2],m[3],m[4],m[5],m[6],m[7],m[8]] for m in M],float)
pot,custo,esf,rap,bar,esc,viab = arr.T
# pesos para o perfil: renda paralela + baixo capital + realista + Brasil
w=np.array([1.6,1.1,1.3,1.0,1.0,1.0,1.4]);
comp=(arr*w).sum(1)/w.sum()*10

cores={"Servico":"#1f77b4","Conteudo":"#9467bd","Produto":"#2ca02c","Afiliado":"#ff7f0e","Microwork":"#d62728"}

# CSV
with open("/home/user/Projeto-novo/analise/banco_dados_rendas.csv","w",newline="") as f:
    w2=csv.writer(f); w2.writerow(["metodo","categoria","potencial_renda","baixo_custo","baixo_esforco",
        "rapidez_1oR$","baixa_barreira_skill","escalabilidade","viabilidade_BR","score_composite","renda_realista"])
    for i,m in enumerate(M): w2.writerow([m[0],m[1],*[int(x) for x in arr[i]],round(comp[i],1),m[9]])

# GRAFICO 1: ranking composite
o=np.argsort(comp)
fig,ax=plt.subplots(figsize=(12,9))
b=ax.barh([nomes[i] for i in o],comp[o],color=[cores[cat[i]] for i in o],edgecolor="k",lw=.5)
for i,bb in zip(o,b): ax.text(comp[i]+0.5,bb.get_y()+bb.get_height()/2,f"{comp[i]:.0f}",va="center",fontsize=8.5)
ax.set_xlim(0,85); ax.set_xlabel("Score de adequacao ao perfil (renda paralela + baixo capital + realista + viavel BR)")
ax.set_title("CONSELHO | Formas de ganhar dinheiro online — ranqueadas para o SEU perfil\n(renda lateral, pouco dinheiro, sem precisar arriscar muito)",fontweight="bold")
from matplotlib.patches import Patch
ax.legend(handles=[Patch(facecolor=c,label=k) for k,c in cores.items()],loc="lower right",title="Categoria")
plt.tight_layout(); plt.savefig("/home/user/Projeto-novo/analise/17_rendas_ranking.png",dpi=140); plt.close()

# GRAFICO 2: scatter potencial x facilidade de comecar
facil=(custo+esf+rap+bar)/4   # facilidade de comecar (baixo custo/esforco/rapido/baixa barreira)
fig,ax=plt.subplots(figsize=(12,8))
for c in cores:
    idx=[i for i in range(len(M)) if cat[i]==c]
    ax.scatter(facil[idx],pot[idx],s=(viab[idx]*45),c=cores[c],edgecolor="k",lw=1,alpha=.85,label=c)
for i,n in enumerate(nomes):
    ax.annotate(n,(facil[i],pot[i]),xytext=(0,8),textcoords="offset points",ha="center",fontsize=7.3,fontweight="bold")
ax.axvline(np.median(facil),color="gray",ls="--",lw=1); ax.axhline(np.median(pot),color="gray",ls="--",lw=1)
ax.text(ax.get_xlim()[1],10.2,"facil de comecar + bom potencial ->",ha="right",fontsize=9,color="#1a6b35",fontweight="bold")
ax.set_xlabel("Facilidade de comecar (custo+esforco+rapidez+baixa barreira)  ->")
ax.set_ylabel("Potencial de renda  ->")
ax.set_title("CONSELHO | Potencial de renda x Facilidade de comecar\ntamanho da bolha = viabilidade no Brasil",fontweight="bold")
ax.legend(loc="lower left",title="Categoria")
plt.tight_layout(); plt.savefig("/home/user/Projeto-novo/analise/18_rendas_scatter.png",dpi=140); plt.close()

print(f"{'#':>2} {'metodo':38s}{'score':>6}{'pot':>5}{'facil':>7}{'viabBR':>7}")
for r,i in enumerate(np.argsort(-comp),1):
    print(f"{r:>2} {nomes[i]:38s}{comp[i]:6.0f}{pot[i]:5.0f}{facil[i]:7.1f}{viab[i]:7.0f}")
print("\nCSV + graficos 17,18 salvos.")
