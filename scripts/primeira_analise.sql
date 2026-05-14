-- Consultando os produtos que mais faturam (Top 5)
SELECT 
    produto, 
    COUNT(id_venda) AS total_vendas,
    SUM(valor_bruto) AS receita_total
FROM vendas_julho
WHERE status = 'paid'
GROUP BY produto
ORDER BY receita_total DESC
LIMIT 5;

-- Analisando a taxa de conversão por método de pagamento
SELECT 
    forma_pagamento,
    COUNT(*) AS total_tentativas,
    SUM(CASE WHEN status = 'paid' THEN 1 ELSE 0 END) AS vendas_confirmadas,
    (SUM(CASE WHEN status = 'paid' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS taxa_conversao_porcentagem
FROM vendas_julho
GROUP BY forma_pagamento;
