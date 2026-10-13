---
data: 2026-10-13
tags:
  - sistema/vault
  - visoes
  - bases
---
# Visões do Vault

Visões automáticas do vault, feitas com Obsidian Bases (nativo do Obsidian).

## Visões Disponíveis

- [[painel-atual|Painel atual]]
- [[linha-do-tempo.base|Linha do tempo]]

## Como Funciona

A base `linha-do-tempo.base` lista sozinha toda nota Markdown que tenha a propriedade `data` no frontmatter. O contexto de cada nota vem do nome da pasta de primeiro nível, então pastas novas aparecem sem editar a base. Os templates ficam de fora para não aparecer `{{date}}`.

```yaml
---
data: 2026-10-13
tags:
  - reuniao
---
```

## Vistas

- **Linha do tempo:** todas as notas com `data`, mais recente primeiro.
- **Cartões:** a mesma lista em cartões.
- **Por contexto:** agrupada pela pasta.
- **Por mês:** agrupada por mês.
- **Calendário:** grade do mês com cada nota no seu dia. Precisa do plugin da comunidade **Calendar Bases** (veja o `README.md` do repositório). Na primeira vez, clique na engrenagem da vista e defina `Start date` = `data`.

## Eventos Futuros

Para registrar um prazo, prova, entrega ou reunião marcada, crie a nota na pasta certa com `data:` igual à data do evento, não à de hoje. Ela entra no calendário sem nenhum passo extra.

## Links

- [[Home]]
