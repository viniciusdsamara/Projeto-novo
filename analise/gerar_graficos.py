# -*- coding: utf-8 -*-
"""Conselho de Estrategia - Analise de produtos digitais saude 50+/60+
Gera graficos a partir das notas consolidadas dos 3 analistas + dados reais da Meta Ad Library.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})

# ---------------------------------------------------------------
# DATASET CONSOLIDADO (notas 0-10 dos 3 analistas; FB ads = dado real Meta Ad Library)
# ---------------------------------------------------------------
produtos = [
    "Diabetes (plano 30d)",
    "Anti-inflamatorio",
    "Coracao / baixo sodio",
    "Mediterranea 50+",
    "Chair yoga 60+",
    "Saude ossea/osteoporose",
    "Saude intestinal",
    "Organizador remedios",
    "Jejum intermitente 50+",
    "Emagrecer/menopausa 50+",
]
demanda      = np.array([9, 8, 7, 9, 9, 6, 7, 6, 8, 8])
prova_venda  = np.array([10,8, 7, 8, 9, 6, 6, 7, 7, 7])
concorrencia = np.array([8, 6, 4, 8, 7, 5, 9, 3, 8, 9])
risco        = np.array([9, 4, 6, 3, 4, 6, 7, 1, 8, 10])
brecha       = np.array([4, 6, 5, 5, 8, 7, 6, 9, 6, 7])
facil_ia     = np.array([5, 8, 6, 9, 9, 7, 7, 10,6, 7])
upsell       = np.array([9, 8, 8, 8, 7, 8, 8, 7, 8, 9])
ticket       = np.array([13,15,10,13,12,10,15,15,12,15])
# FB ads ativos (EUA) - dado real Meta Ad Library (jun/2026). * = numero inflado por 1 anunciante
fb_ads       = np.array([323,343,192,3850,3102,1285,24395,2,60,7138])

# ---------------------------------------------------------------
# SCORE DE OPORTUNIDADE (transparente e ponderado)
# positivos: demanda x1.5, prova x1.5, brecha x1.0, facil_ia x1.0, upsell x0.5
# negativos: concorrencia x1.5, risco x2.0
# ---------------------------------------------------------------
score = (demanda*1.5 + prova_venda*1.5 + brecha*1.0 + facil_ia*1.0 + upsell*0.5
         - concorrencia*1.5 - risco*2.0)

ordem = np.argsort(score)  # crescente

def cor_score(s):
    if s >= 28: return "#1a9850"   # verde - vale muito
    if s >= 18: return "#91cf60"   # verde claro
    if s >= 12: return "#fee08b"   # amarelo
    return "#d73027"               # vermelho - evitar

# ===============================================================
# GRAFICO 1 - RANKING DE OPORTUNIDADE
# ===============================================================
fig, ax = plt.subplots(figsize=(11, 6.5))
p = [produtos[i] for i in ordem]
s = score[ordem]
cores = [cor_score(v) for v in s]
bars = ax.barh(p, s, color=cores, edgecolor="black", linewidth=0.6)
for b, v in zip(bars, s):
    ax.text(v + 0.4, b.get_y()+b.get_height()/2, f"{v:.0f}", va="center", fontweight="bold")
ax.set_xlabel("Score de Oportunidade (ponderado)  ->  maior = melhor")
ax.set_title("CONSELHO | Ranking de Oportunidade - PDFs de Saude para o publico 50+/60+\n"
             "(demanda + prova de venda + brecha + facilidade IA - concorrencia - risco de anuncio)",
             fontweight="bold", fontsize=12)
ax.axvline(0, color="black", lw=0.8)
from matplotlib.patches import Patch
leg = [Patch(facecolor="#1a9850", label="Vale muito"),
       Patch(facecolor="#91cf60", label="Vale"),
       Patch(facecolor="#fee08b", label="Neutro/cautela"),
       Patch(facecolor="#d73027", label="Evitar (risco/saturado)")]
ax.legend(handles=leg, loc="lower right", framealpha=0.95)
ax.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.savefig("/home/user/Projeto-novo/analise/1_ranking_oportunidade.png", dpi=140)
plt.close()

# ===============================================================
# GRAFICO 2 - MAPA DEMANDA x CONCORRENCIA (sweet spot)
# x = demanda (media demanda+prova), y = concorrencia INVERTIDA (10 - concorr)
# bolha = score, cor = risco de anuncio
# ===============================================================
fig, ax = plt.subplots(figsize=(11, 7.5))
x = (demanda + prova_venda) / 2
y = 10 - concorrencia            # alto = pouca concorrencia
sizes = (score - score.min() + 6) * 28
cmap = LinearSegmentedColormap.from_list("risk", ["#1a9850", "#fee08b", "#d73027"])
sc = ax.scatter(x, y, s=sizes, c=risco, cmap=cmap, vmin=0, vmax=10,
                edgecolor="black", linewidth=1.1, alpha=0.9)
# quadrante sweet spot
ax.axhspan(5.5, 10.5, xmin=(6.5-3)/ (10-3), color="#1a9850", alpha=0.06)
ax.axvline(6.5, color="gray", ls="--", lw=1)
ax.axhline(5.5, color="gray", ls="--", lw=1)
ax.text(9.6, 9.7, "SWEET SPOT\nalta demanda +\npouca concorrencia", ha="right", va="top",
        fontsize=10, color="#1a6b35", fontweight="bold")
for i, nome in enumerate(produtos):
    ax.annotate(nome, (x[i], y[i]), xytext=(0, 11), textcoords="offset points",
                ha="center", fontsize=8.5, fontweight="bold")
cb = plt.colorbar(sc, ax=ax)
cb.set_label("Risco de reprovacao/ban no anuncio (0 = seguro, 10 = altissimo)")
ax.set_xlabel("DEMANDA / prova de venda  ->")
ax.set_ylabel("POUCA concorrencia  ->  (10 - concorrencia)")
ax.set_xlim(3, 10.5); ax.set_ylim(0, 10.8)
ax.set_title("CONSELHO | Mapa de Oportunidade: Demanda x Concorrencia\n"
             "tamanho da bolha = score | cor = risco de anuncio (verde = seguro)",
             fontweight="bold", fontsize=12)
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("/home/user/Projeto-novo/analise/2_mapa_demanda_concorrencia.png", dpi=140)
plt.close()

# ===============================================================
# GRAFICO 3 - HEATMAP de todos os criterios
# ===============================================================
criterios = ["Demanda", "Prova venda", "Brecha", "Facil. IA", "Upsell",
             "Concorrencia\n(menor=melhor)", "Risco anuncio\n(menor=melhor)"]
M = np.vstack([demanda, prova_venda, brecha, facil_ia, upsell, concorrencia, risco]).T
# para colorir: concorrencia e risco invertem (alto = ruim -> vermelho)
M_color = M.copy().astype(float)
M_color[:,5] = 10 - M_color[:,5]
M_color[:,6] = 10 - M_color[:,6]
ordem_score = np.argsort(-score)  # melhores no topo
M = M[ordem_score]; M_color = M_color[ordem_score]
labels_p = [produtos[i] for i in ordem_score]

fig, ax = plt.subplots(figsize=(11, 7))
cmap2 = LinearSegmentedColormap.from_list("rg", ["#d73027", "#fee08b", "#1a9850"])
im = ax.imshow(M_color, cmap=cmap2, vmin=0, vmax=10, aspect="auto")
ax.set_xticks(range(len(criterios))); ax.set_xticklabels(criterios, fontsize=9)
ax.set_yticks(range(len(labels_p))); ax.set_yticklabels(labels_p, fontsize=9.5)
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        ax.text(j, i, f"{int(M[i,j])}", ha="center", va="center", fontsize=9, fontweight="bold")
ax.set_title("CONSELHO | Matriz completa de criterios (ordenado por oportunidade)\n"
             "verde = favoravel | vermelho = desfavoravel",
             fontweight="bold", fontsize=12)
cb = plt.colorbar(im, ax=ax, fraction=0.025)
cb.set_label("favorabilidade")
plt.tight_layout()
plt.savefig("/home/user/Projeto-novo/analise/3_matriz_criterios.png", dpi=140)
plt.close()

# ===============================================================
# GRAFICO 4 - CONCORRENCIA REAL EM ANUNCIOS (Meta Ad Library)
# ===============================================================
fig, ax = plt.subplots(figsize=(11, 6.5))
ordem_ads = np.argsort(fb_ads)
p2 = [produtos[i] for i in ordem_ads]
v2 = fb_ads[ordem_ads]
cores2 = ["#1a9850" if x < 400 else "#fee08b" if x < 3500 else "#d73027" for x in v2]
bars = ax.barh(p2, v2, color=cores2, edgecolor="black", linewidth=0.6)
ax.set_xscale("log")
for b, v in zip(bars, v2):
    ax.text(v*1.1, b.get_y()+b.get_height()/2, f"{v:,}".replace(",", "."),
            va="center", fontsize=9, fontweight="bold")
ax.set_xlabel("Anuncios ATIVOS nos EUA (escala log) - dado real Meta Ad Library, jun/2026")
ax.set_title("CONSELHO | Concorrencia REAL no trafego pago (Meta Ad Library)\n"
             "verde = pouca disputa | vermelho = saturado",
             fontweight="bold", fontsize=12)
ax.grid(axis="x", alpha=0.3, which="both")
leg2 = [Patch(facecolor="#1a9850", label="Pouca disputa (<400)"),
        Patch(facecolor="#fee08b", label="Media (400-3500)"),
        Patch(facecolor="#d73027", label="Saturado (>3500)")]
ax.legend(handles=leg2, loc="lower right")
plt.tight_layout()
plt.savefig("/home/user/Projeto-novo/analise/4_concorrencia_anuncios.png", dpi=140)
plt.close()

# ---- ranking textual para o terminal ----
print("RANKING FINAL (score de oportunidade):")
for r, i in enumerate(np.argsort(-score), 1):
    print(f"{r:2d}. {produtos[i]:30s} score={score[i]:5.1f} | demanda={demanda[i]} concorr={concorrencia[i]} risco={risco[i]} ads={fb_ads[i]}")
print("\nGraficos salvos em /home/user/Projeto-novo/analise/")
