# Banco de Dados — Venda de PDFs via Tráfego Pago (pesquisa profunda, 11+ analistas)

> Mercado EUA, venda em US$. Consolidação de 11+ agentes de pesquisa (demanda, demografia,
> concorrência ao vivo na Meta Ad Library, AOV multi-plataforma, benchmarks de funil, risco/plataforma).
> **Honestidade de dados:** CPC/CPM = benchmark publicado (DADO). CVR clique→compra = ESTIMATIVA
> ancorada na mediana de e-commerce (1,57%). Contagens de venda do Etsy = snippets reais; receita
> por loja = estimativa de ferramentas (EverBee). Validar com pixel próprio antes de escalar.

## 1. Premissas financeiras
- Orçamento do usuário: **R$30/dia = ~US$167/mês** (câmbio R$5,40).
- Margem líquida digital: **90%** (após Payhip 5% + pagamento ~3,5% + reembolso ~1,5%).
- CPA (custo por venda) = CPC ÷ CVR. Break-even AOV = CPA ÷ margem.

## 2. Ranking por viabilidade em tráfego pago (12 nichos)

| # | Produto | Viab (0-100) | ROAS frio | ROAS otimizado | CPA real | Break-even US$ | Risco anúncio | Invest/30 vendas |
|---|---|---|---|---|---|---|---|---|
| 1 | Caça-palavras letra grande | 72 | 1.04 | 5.50 | $11.5 | $12.8 | 2 | $346/mês |
| 2 | Devocional cristão | 69 | 1.10 | 7.20 | $10.0 | $11.1 | 5 | $300/mês |
| 3 | Genealogia | 67 | 0.64 | 4.17 | $21.7 | $24.2 | 3 | $652/mês |
| 4 | Binder de espólio | 60 | 0.65 | 3.19 | $34.0 | $37.8 | 3 | $1.020/mês |
| 5 | ADHD planner (wildcard) | 59 | 0.75 | 3.06 | $22.7 | $25.3 | 3 | $682/mês |
| 6 | Planejador de jardinagem | 59 | 0.49 | 2.80 | $20.5 | $22.7 | 2 | $614/mês |
| 7 | Jogos cognitivos letra grande | 54 | 0.58 | 3.14 | $19.1 | $21.2 | 6 | $573/mês |
| 8 | Autocuidado/journal (wildcard) | 54 | 0.88 | 2.71 | $20.5 | $22.7 | 4 | $614/mês |
| 9 | Organizador de cuidador | 38 | 0.43 | 2.38 | $37.5 | $41.7 | 4 | $1.125/mês |
| 10 | Chair Yoga sênior | 24 | 0.35 | 1.89 | $34.4 | $38.2 | 6 | $1.031/mês |
| 11 | Plano anti-inflamatório | 2 | 0.28 | 1.92 | $47.1 | $52.3 | 9 | $1.412/mês |
| 12 | Prevenção de quedas | 0 | 0.17 | 1.12 | $57.1 | $63.5 | 7 | $1.714/mês |

Dados completos por produto (demografia, gênero, AOV, ads ativos): ver `banco_dados_nichos.csv`.

## 3. Conclusões cruzadas (o que os dados dizem, sem floreio)

1. **Tráfego pago para PDF de ticket baixo só fecha a conta com AOV alto.** O piso de CPA no
   Meta é ~US$30 (benchmark publicado). Produto de US$7–15 não paga esse CPA. A correção é
   **bundle + order bump + upsell** para levar o AOV a US$25–40 — confirmado por múltiplos analistas.
2. **No cenário frio realista, quase tudo perde** (ROAS < 1). Só **devocional** e **caça-palavras**
   chegam a empatar, por terem o CPC mais baixo + CVR mais alta (público de impulso, baixo custo).
3. **Os campeões de demanda do início (chair yoga, diabetes, emagrecimento) são fracos em tráfego
   pago**: CPC alto (saúde), risco de banimento alto, e break-even acima do ticket realista.
4. **"Quem compra" raramente é "quem usa".** Caça-palavras, prevenção de quedas e chair yoga são
   comprados por filhas de 45–60 para pais de 70+. O criativo fala com o comprador, não o usuário.
5. **Público que mais consome (não só idade):** devocional (mulheres 30–60, autocompra, público
   gigante e barato), autocuidado/ADHD (mulheres 20–45, viral no TikTok/Reels), caça-palavras/jogos
   (presente para idosos, comprador 45–65).

## 4. Veredito de viabilidade
- **Entrar primeiro (melhor relação retorno × segurança × concorrência):** Caça-palavras letra
  grande, Devocional cristão, Genealogia.
- **Alto teto com bundle:** Binder de espólio (AOV até US$39), ADHD planner.
- **Evitar como entrada:** Prevenção de quedas e anti-inflamatório (break-even US$52–63 + risco de
  ban) — inviáveis no orçamento atual.

## 5. Stack operacional recomendada
- Plataforma: **Payhip** (5% por venda, sem mensalidade) + **Etsy** em paralelo para hobbies (tráfego orgânico).
- Pagamento: **PayPal Guest Checkout + cartão (Stripe)**, checkout de 1 página.
- Disclaimers obrigatórios (saúde/espólio) e checkbox de "compra não reembolsável".
- Sequência de lançamento por risco: hobbies/jogos → espólio/cuidador → saúde.

## 6. Fontes principais
WordStream/Triple Whale/Madgicx/LocaliQ (benchmarks Meta 2025/26); Meta Ad Library ao vivo (jun/2026);
Etsy/Amazon/Gumroad/ClickBank/Stan/Payhip (preço, AOV, prova de venda); AARP, Pew, CDC, National
Gardening Survey, US Census (demografia). URLs detalhadas nos relatórios de cada analista.
