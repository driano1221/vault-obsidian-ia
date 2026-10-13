---
data: 2026-10-13
tags:
  - design
  - indice
status: ativo
---
# Dicionário de Design - Quando Usar o Quê

Guia de decisão rápida: situação, o que usar, status e onde está a regra. Consultar aqui antes de criar qualquer coisa visual do zero. Se já existe template ou paleta aprovada, usar a aprovada.

> [!important] Com agente, use `/design-vault`: ele lê este dicionário, as [[regras-de-design-aprovadas|regras]] e a [[galeria-design|galeria]], pergunta o que falta, propõe um rascunho e confere o resultado antes de entregar.

As regras em si moram em [[regras-de-design-aprovadas]]; aqui só se aponta para elas, para não existirem duas versões.

## Árvore de Decisão Rápida

1. **É gráfico de dados?** -> seção Gráficos
2. **É mapa?** -> seção Mapas
3. **É apresentação?** -> seção Slides
4. **É diagrama ou fluxo?** -> Mermaid por padrão (diagrama como código dentro da nota)
5. **É tela, app ou dashboard?** -> seção Telas
6. **É cor ou paleta?** -> [[regras-de-design-aprovadas#Paletas|paletas]]

## Gráficos

| Quando | Use | Status | Regra / detalhe |
|---|---|---|---|
| (exemplo) gráfico em Python para relatório | matplotlib + estilo aprovado | para-testar | [[regras-de-design-aprovadas#Gráficos]] |

## Mapas

| Quando | Use | Status | Regra / detalhe |
|---|---|---|---|

## Slides

| Quando | Use | Status | Regra / detalhe |
|---|---|---|---|

## Telas e Dashboards

| Quando | Use | Status | Regra / detalhe |
|---|---|---|---|

## Glossário de Uma Linha

- **"Padrão IA":** estética genérica que denuncia tela feita por IA (gradiente roxo, cartões com emoji, tudo centralizado). Descreva aqui o que você considera "cara de IA" para o agente evitar.
- **Mermaid:** diagramas como código dentro do Markdown, renderizados pelo Obsidian.

## Manutenção

- Ferramenta nova de design entra como `para-testar` aqui e ganha nota própria nesta pasta.
- Regra que se repetir em mais de uma peça vira linha aqui e em [[regras-de-design-aprovadas]].

## Links Relacionados

- [[26_Design/README|Design]]
- [[Home]]
