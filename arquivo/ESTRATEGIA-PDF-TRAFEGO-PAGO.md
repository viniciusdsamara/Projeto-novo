# Estratégia: Vender PDFs em Dólar com Tráfego Pago

> Documento de estratégia gerado a partir do debate do "Conselho" (5 especialistas).
> Meta declarada: investir ~R$30/dia (~US$5,50/dia) em tráfego pago e captar pelo menos 1 venda de US$20/dia.
> Data: 2026-06-22.

---

## 0. Veredito honesto (leia antes de tudo)

A meta literal — **1 venda de US$20 por dia, já no Dia 1, com US$5,50/dia em tráfego frio** — **não fecha na matemática.** Não é pessimismo, é aritmética:

- US$5,50/dia ÷ CPC de ~US$1,50 = **~3,7 cliques/dia**.
- A 1,5% de conversão (venda direta a frio), isso dá **1 venda a cada ~18 dias**.
- O CPA real fica em ~US$100 para vender um produto de US$20 → prejuízo de ~US$80/venda.
- Pior: US$5,50/dia é pouco demais para o algoritmo do Meta sair da fase de aprendizado (precisa de ~50 conversões/semana).

**Como tornar a meta viável** (consenso do conselho): não mude a meta, mude a **estrutura**:

1. **Aumente o valor por venda (AOV)** com order bump + upsell → de US$20 para ~US$45 por pedido. Isso é o ajuste nº 1.
2. **Use Pinterest como motor principal** (orgânico + pago barato), não Meta para venda direta a frio.
3. **Trate os primeiros US$150–300 como custo de aprendizado**, não como compra de vendas.
4. **Escale o orçamento com o lucro.** A meta de 1 venda/dia é alcançável em **60–90 dias**, não no Dia 1.

---

## 1. Onde vender (plataforma) — receber em dólar sendo brasileiro

| Plataforma | Taxa | Líquido em US$20 | Como o BR recebe | Order bump/Upsell | Veredito |
|---|---|---|---|---|---|
| **Payhip (Free)** | 5% + processador | **~US$18** | PayPal (USD) / Payoneer | ✅ Nativo | ⭐ **Escolha primária** |
| Lemon Squeezy | 5% + $0,50 (+intl) | ~US$17 | PayPal / bank payout | ✅ | Secundária (cuida de VAT/imposto por você) |
| Gumroad | **10%** | ~US$17,50 | PayPal (Stripe não opera no BR) | ❌ Sem upsell | Evitar como padrão |
| Etsy (downloads) | ~6,5% + taxas | ~US$17 | **Payoneer obrigatório** | ❌ (sem checkout próprio) | Só se for aposta 100% orgânica |

**Recomendação:** **Payhip** no plano Free. Menor taxa com funil completo (landing + order bump + upsell + cupom nativos), recebimento em USD via PayPal/Payoneer e ainda aceita Pix/Mercado Pago para ampliar conversão.

- **Por que NÃO Gumroad por padrão:** taxa dobrada (10%), sem order bump/upsell e sem Conversions API confiável.
- **Por que NÃO Etsy para este caso:** apesar do tráfego orgânico embutido, você perde controle de checkout, pixel e upsell — incompatível com escalar via tráfego pago de US$20.
- **Recebimento:** PayPal (USD) ou Payoneer (USD) → sacar para conta no Brasil. Use Wise para melhorar o câmbio no saque.

---

## 2. O que vender (nicho) — onde há volume com concorrência sã

Para ticket de ~US$20, o que vence é **especificidade + formato acionável** (workbook/planner/template), não ebook genérico. *"Um nicho com 10.000 compradores desesperados vence um tema com 1 milhão de curiosos."*

### Ranking de nichos para começar

| # | Nicho | Ticket | Formato que vende | Concorrência | Por quê |
|---|-------|--------|-------------------|--------------|---------|
| 1 | **IA/ChatGPT workflows por profissão** (corretor, contador, coach, nutricionista) | US$17–30 | Guia + pack de prompts | **Baixa** | +420% de crescimento, alta intenção, ainda cedo = melhor risco/retorno |
| 2 | **Finanças pessoais para um segmento** (freelancers, casais, Gen Z) | US$15–27 | Workbook + planilha/planner | Média | Demanda evergreen, blindada a crise, margem ~72% |
| 3 | **Meal plans nichados** (mediterrânea, low-carb família) | US$12–20 | Planner + receituário | Baixa | Recompra, produção barata |
| 4 | **Side hustle por segmento** (pais, 9-to-5) | US$19–27 | Guia + checklist + planilha | Média | Alto volume de busca |
| 5 | Produtividade / Notion second-brain | US$15–25 | Template Notion + guia | Média-alta | Vende em volume (Gumroad) |
| 6 | Saúde mental por demografia | US$12–20 | Workbook + journal | Baixa-média | +220%, alto valor emocional |
| 7 | Planners/printables (Etsy) | US$8–18 | Printable A4 | **Alta** | Volume gigante, porém saturado |

### Apostas firmes
1. **IA workflows por profissão** (principal) — melhor equação volume × baixa concorrência.
2. **Finanças pessoais para um segmento** (segura) — evergreen, ticket de US$20 é o ponto doce.
3. **Meal plans nichados** (baixo esforço, recompra) — bom segundo produto.

**Regra de ouro:** cruze dois nichos para fugir da concorrência mantendo a demanda — ex.: "IA para nutricionistas", "finanças para artistas".

---

## 3. A oferta (empacotamento + preço)

Ninguém paga US$20 por "um arquivo". Paga por **um resultado entregue num kit**.

- **Bundle, não PDF solto:** guia principal (15–30 págs, design limpo no Canva) + checklist + worksheet/planner + **template editável (Canva/Notion)** — alto valor percebido, custo zero.
- **Ancoragem de valor:** "Guia US$27 + Templates US$19 + Checklist US$11 = **US$57**, hoje por **US$19**".
- **Charm pricing:** use **US$19** (não US$20). Mostre sempre "De US$57 por US$19".
- **Garantia incondicional de 7–14 dias** — destrava conversão; reembolso real em produto de US$20 é baixíssimo.

### Estrutura de funil (o que viabiliza o budget baixo)
```
Anúncio (Pinterest/Meta)
   ↓
Checkout direto (Payhip)  ← NÃO mande para captura de e-mail primeiro
   ├─ Order bump: "+US$9 adicione [pack extra]"   (30–40% aceitam)
   └─ Upsell 1-clique pós-compra: US$29 (versão expandida / mini-curso / 10 templates)
   ↓
AOV-alvo: ~US$45 (2–3x o preço do PDF)  ← é isso que torna o tráfego frio sustentável
   ↓
E-mail entra DEPOIS da compra (entrega + sequência de upsell e review)
```

---

## 4. O tráfego (canal + estrutura)

Com US$5/dia, **Meta para venda direta a frio é o caminho mais difícil que existe** (CPM caro, ~2 cliques/dia, nunca sai da fase de aprendizado).

### Canal principal: Pinterest
- CPM US$6–8, CPC US$0,10–1,50 (2–3x mais barato que Meta/TikTok).
- Usuário em "modo planejamento" = alta intenção de compra, ideal para templates/planners/guias.
- Pins têm cauda longa de meses → **orgânico forte + ~US$3–5/dia pago compostam.**

### Estrutura de campanha com budget baixo
- **ABO, não CBO** (CBO fragmenta budget pequeno).
- **1 ad set, 3–4 criativos, público amplo** (deixe o algoritmo segmentar).
- Objetivo inicial: **Traffic/cliques**, não Sales (você não terá conversões suficientes para o algoritmo aprender em Sales).
- **Pixel + Conversions API (CAPI)** instalados ANTES do primeiro dólar — >50% das conversões de browser não são rastreadas; CAPI recupera 30–40%.
- **Esqueça retargeting no início** — sem pool de audiência ele não funciona. Ligue depois (reduz CPA 40–70%).

### Criativos
- **Vídeo vertical UGC 15–30s** com o produto visível nos primeiros 5s (formato campeão 2025/26).
- **Carrossel before/after** como segundo formato.
- Imagem estática para teste barato inicial.
- **Um ângulo por criativo.**

### Ângulos de copy / headlines prontas
- Dor/solução: *"Cansado de [dor]? Esse kit resolve em [tempo]."*
- Before/after: *"De [estado ruim] para [estado desejado] — sem [obstáculo]."*
- Curiosidade: *"Ninguém te conta isso sobre [tema]…"*
- Objeção antecipada (alta conversão): *"Achei que era furada — até testar por uma semana."*

### Prova social do zero
- **Beta gratuito:** entregue de graça a 15–30 pessoas do nicho em troca de depoimento honesto.
- Screenshots dos templates em uso, prints de antes/depois.
- E-mail automático pós-compra pedindo review com micro-incentivo. (Testemunhos elevam conversão ~34%.)

---

## 5. A matemática (cenários)

Com US$5,50/dia em tráfego:

| Cenário | CPC | Cliques/dia | Conversão | Vendas/dia | Vendas/mês |
|---|---|---|---|---|---|
| Pessimista | US$2,00 | 2,75 | 1,0% | 0,028 | ~0,8 |
| Realista | US$1,50 | 3,67 | 1,5% | 0,055 | ~1,6 |
| Otimista | US$1,00 | 5,50 | 3,0% | 0,165 | ~5 |

- **CPA-alvo máximo** para o negócio se pagar: **≤ US$18** (ROAS 1x). Saudável: **≤ US$10–12**.
- Com AOV de ~US$45 (bump+upsell) em vez de US$20, o mesmo CPA passa a caber — é o que muda o jogo.

---

## 6. Plano de execução em fases (90 dias)

### Fase 0 — Preparação (Semana 1)
- [ ] Escolher nicho (recomendado: IA workflows por profissão **ou** finanças por segmento).
- [ ] Produzir o bundle (guia + checklist + worksheet + template Canva/Notion).
- [ ] Criar conta Payhip + PayPal/Payoneer (recebimento USD).
- [ ] Montar landing/checkout no Payhip com order bump (+US$9) e upsell (US$29).
- [ ] Instalar Pixel + CAPI.
- [ ] Conseguir 15–30 depoimentos via beta gratuito.

### Fase 1 — Validação (Semanas 2–4, ~US$5/dia)
- [ ] Pinterest orgânico (5–10 pins/dia) + US$3–5/dia pago, ABO/Traffic, 3–4 criativos.
- [ ] Meta: validar ângulos e criativos, não esperar lucro. Custo de aprendizado.
- [ ] Medir CTR, CPC, taxa de checkout, AOV. Matar criativos ruins.

### Fase 2 — Otimização (Semanas 5–8)
- [ ] Dobrar nos criativos/ângulos vencedores.
- [ ] Ligar retargeting (audiência já existe).
- [ ] Ajustar order bump/upsell para subir o AOV.
- [ ] Começar sequência de e-mail pós-compra.

### Fase 3 — Escala (Semanas 9–12+)
- [ ] Reinvestir lucro: subir orçamento para US$15–25/dia (mínimo para o algoritmo aprender em Sales).
- [ ] Migrar objetivo para Conversions/Sales.
- [ ] Lançar 2º produto (cross/upsell, ex.: meal plans nichados).
- [ ] **Meta de 1 venda/dia torna-se realista aqui**, com AOV otimizado.

---

## 7. Resumo das discordâncias do conselho (transparência)

- **Cético financeiro:** a meta no Dia 1 com US$5,50/dia é inviável; corrija ticket/funil antes de escalar.
- **Tráfego pago:** Meta a frio queima dinheiro com esse budget; comece no Pinterest e trate os primeiros ~US$300 como aprendizado.
- **Plataforma:** evite o "óbvio" Gumroad; Payhip dá mais margem e funil completo.
- **Nicho:** evite Etsy printables genéricos (saturado); aposte em micro-nichos de IA e finanças.
- **Oferta:** o lucro não vem da 1ª venda — vem do order bump + upsell. AOV ~US$45 é o que sustenta o tráfego frio.

**Consenso final:** a meta é alcançável, mas em ~90 dias e com a estrutura acima — não como "US$20 a frio no Dia 1".

---

### Fontes principais
Tráfego: AdAmigo (CPM/CPC 2026), Madgicx, Stackmatix, AdBacklog (Pinterest), DigitalApplied (TikTok), PPC.land (Pixel+CAPI), Mako Metrics (CPA).
Plataformas: Gumroad Help/Fees, Payhip Pricing, Lemon Squeezy Docs, Etsy/Payoneer, Sellfy.
Nicho: Outfy (Etsy), Accio (Gumroad 2025), SellTheTrend, Inkfluence AI, SavingsGrove.
Unit economics: WordStream 2025, Trendtrack, AdAmigo 2026, Lucky Orange, Wonderful (Learning Phase).
Oferta/funil: FunnelKit, Stan.store, getwpfunnels, Intuit (charm pricing), Cinerads (UGC), Metalla (hooks), MailerLite.
