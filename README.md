# 📊 Análise de Performance: Vendas de Infoprodutos e Estratégia LATAM

Este projeto apresenta uma análise profunda dos dados de vendas do meu negócio digital (hospedado na Kiwify), com o objetivo de identificar padrões de consumo e validar a viabilidade de expansão para o mercado hispanófono (América Latina).

## 🎯 Objetivo do Negócio
Otimizar o retorno sobre investimento (ROI) em anúncios e identificar quais produtos do portfólio possuem maior potencial de escala internacional. Esta análise não é apenas teórica; ela guia decisões reais de investimento em tráfego e tradução de conteúdo.

## 🛠️ Metodologia Aplicada
1. **Extração e Proteção de Dados:** Exportação de dados da Kiwify e tratamento via Python para anonimização (removendo CPFs, E-mails e nomes de clientes), garantindo conformidade com a LGPD.
2. **Tratamento em Excel:** Organização dos dados brutos em um ambiente estruturado para facilitar a leitura e geração de indicadores (KPIs).
3. **Análise Comparativa:** Avaliação mensal (iniciando em Julho/2025) de faturamento, taxas de conversão e métodos de pagamento.

## 📈 Insights Estratégicos (Julho 2025)
* **Produto Estrela:** *Metodologias Ativas com IA* responde por mais de 53% do faturamento.
* **Comportamento de Checkout:** 79,1% das compras são via PIX. Isso aponta um desafio logístico para o mercado LATAM, onde será necessário implementar gateways que aceitem métodos locais de outros países.
* **Conversão de Vendas:** A taxa de 76,7% indica uma boa intenção de compra, mas as 25 transações pendentes sugerem a necessidade de uma automação de recuperação de carrinho.

## 📁 Estrutura do Repositório
* `/dados-brutos`: Base CSV exportada diretamente da plataforma (anonimizada).
* `/analises-excel`: Planilhas estruturadas com tabelas dinâmicas e indicadores mensais.
* `/scripts`: (Em breve) Códigos em SQL e Python para automação das análises futuras.

---
**Próximos Passos:** - [ ] Análise comparativa Agosto vs. Julho.
- [ ] Mapeamento geográfico detalhado dos leads internacionais.
- [ ] Definição do orçamento de teste para o mercado hispanófono.
