# Plano de Vendas por Afiliação — Tráfego Pago, sem aparecer

> Documento de trabalho. Foco único: **validar um sistema de venda por afiliação com tráfego
> pago**, sem marca pessoal e multi-oferta. Tudo que não for afiliação está fora deste plano.
> Data: 2026-06-22.

## O que é este plano
Validar um **sistema de vendas por afiliação com tráfego pago**, **sem marca pessoal** (você não
aparece) e **multi-oferta** (não depende de um único produto). O ativo que se constrói é o
**método de testar e escalar qualquer oferta** — não um produto específico.

Modelo em uma linha: **anúncio barato → bridge page → oferta de afiliado → tracker decide o que
matar e o que escalar.**

---

## A realidade (dados, não promessa)
- ~95% das campanhas de mídia paga não dão ROI; ~95% dos afiliados desistem antes de lucrar.
- Mediana de iniciante: US$0–500/mês nos primeiros 6-12 meses.
- O que separa quem sobrevive: **tráfego barato (errar barato) + tracker desde o dia 1 +
  disciplina de matar/escalar por dado.** O plano inteiro é desenhado em torno disso.
- Esperar **prejuízo nos primeiros 1-3 meses** é normal e está orçado.

---

## O funil (igual para toda oferta)
```
Anúncio (native/push)  →  Bridge/presell page  →  Oferta do vendor  →  conversão
                                  └─ tracker (postback S2S) registra tudo
```
- **Bridge page é obrigatória:** exigida pelas redes (compliance) e converte muito mais
  (dados: ~16% vs ~1% no link direto). É um **template reutilizável** — troca-se headline/ângulo/
  oferta para cada teste.
- **Tracker antes do 1º dólar:** sem ele você fica cego e queima budget sem saber por quê.

---

## Stack (com dados)

### Tráfego — começar pelo barato e afiliado-friendly
| Rede | Tipo | CPC/CPM | Afiliado? | Orç. mín. | Risco ban |
|---|---|---|---|---|---|
| **PropellerAds** | push/pop | CPC US$0,005–0,5 | ✅ nativo | US$10-30/dia | 🟢 baixo |
| **Taboola/Teads** | native | CPC US$0,18–0,60 | ✅ permissivo | US$10-30/dia | 🟢 baixo |
| Adsterra | pop/push | CPM US$0,5–1,5 | ✅ nativo | dep. US$100 | 🟢 baixo |
| ~~Meta / Google~~ | tier 1 | CPC US$2–4+ | ❌ hostil 2026 | — | 🔴 alto |

→ **Começar:** PropellerAds (pop) ou Taboola (native). Meta/Google ficam fora no início.

### Redes de afiliado (a oferta)
| Rede | Foco | Payout | Quando paga |
|---|---|---|---|
| **Digistore24** | software/IA, recorrente | 10-60% + rebill | 3x/semana |
| **ClickBank** | nutra, digital | 50-85% ou US$50-200 CPA | ~2 semanas |
| **MaxBounty / CPAGrip** | CPA (saúde, dating) | US$10-300/ação | Net-15/30 |

### Ferramentas
- **Tracker:** Binom (US$49/mês, ilimitado) ou **BeMob grátis** (até 100k eventos).
- **Bridge/landing:** Carrd ou Leadpages + domínio (~US$10/ano).

---

## Ofertas para começar (portfólio multi-produto)
Rodar **4-5 ofertas em paralelo**, em 2 lanes:
- **Lane principal (white-hat):** 2-3 ofertas de **software/IA recorrente (Digistore24)** —
  EPC US$1,60–3,40, zero restrição de anúncio, recorrência = receita que compõe. É a lane mais
  limpa e sustentável.
- **Lane secundária (maior payout):** 1-2 ofertas **nutra/biz-opp (ClickBank/CPA)** em push/
  native — payout US$120-200, mas exige bridge honesta e mais cuidado de compliance.

Critério de entrada: **payout cobre o CPA esperado**; preferir **híbrido (CPA inicial + rebill)** —
recorrência pura não cobre o custo de aquisição em mídia paga.

→ **Evitar:** crypto, finance e gambling (regulação inviável para solo em 2026).

---

## Economia e capital (números reais)
- Tráfego barato (CPC US$0,005–0,5) deixa testar com **US$10-15/dia** e ainda gerar cliques
  suficientes para ler dados rápido.
- **Breakeven ROAS** depende da margem: oferta 50% margem → breakeven 200% ROAS (US$2 por US$1).
  ROAS mediano de campanha viva ≈ 2:1; alvo 3:1+.
- **Budget de teste por oferta ≈ CPA × 5-7**, rodado por 3-7 dias por variação.
- **Capital de validação:** reservar **~US$1.000-2.000 em 8-12 semanas** (tracker + lander +
  budget de 4-5 ofertas). Abaixo de ~US$1k é aposta.

---

## Execução (fases com critério de avanço)
**Fase 0 — Montagem (sem. 1-2):** abrir 1 rede de tráfego + Digistore24 + ClickBank + 1 rede CPA;
configurar tracker com postback; comprar domínio e montar o template de bridge.
→ *Avança quando:* tracker registrando cliques de teste + ≥3 ofertas aprovadas.

**Fase 1 — Testes (sem. 3-6):** subir 4-5 ofertas no funil, US$10-15/dia, coletar CTR / conversão
da bridge / CPA. Matar quem não dá sinal dentro do budget.
→ *Avança quando:* dados limpos por oferta + ≥1 oferta com sinal de conversão.

**Fase 2 — Achar a vencedora (sem. 7-10):** iterar ângulo/criativo/geo nas promissoras; cortar o
resto.
→ *Avança quando:* **1 oferta no breakeven ou positivo, de forma repetível** (o método funcionou).

**Fase 3 — Escalar (sem. 11+):** aumentar budget, abrir mais geos/fontes na vencedora; entrar
novas ofertas no pipeline e repetir o ciclo.

---

## Regras e riscos (não ignorar)
- **Bridge honesta, sem cloaking enganoso** — além de violar as redes, é insustentável.
- **Divulgação de afiliado** sempre (exigência legal/plataforma).
- **Reservar o capital de teste de uma vez** — entrar sem caixa para 8-12 semanas é a causa nº1
  de desistir no meio.
- **Ler tudo pelo tracker** — decisão por dado, nunca por achismo.

---

## Checklist operacional (para tocar a Fase 0)
- [ ] Escolher rede de tráfego inicial: **PropellerAds** (pop, mais barato p/ começar) ou Taboola.
- [ ] Criar conta e aprovar-se em: Digistore24, ClickBank, 1 rede CPA (MaxBounty/CPAGrip).
- [ ] Contratar tracker (BeMob grátis no início) e configurar **postback S2S** com a rede de afiliado.
- [ ] Registrar domínio + subir hospedagem da bridge (Carrd/Leadpages).
- [ ] Montar **template de bridge page** (headline, prova, escassez, CTA) reutilizável.
- [ ] Selecionar as 4-5 ofertas do portfólio inicial (preencher `analise/ofertas_shortlist.md`).
- [ ] Definir o caixa de validação (US$1.000-2.000) e o teto diário por oferta.

> SaaS, produto próprio e qualquer coisa além de afiliação estão **fora deste plano** — só depois
> que este método estiver validado e dando lucro repetível.
