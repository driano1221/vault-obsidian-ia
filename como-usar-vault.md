---
data: 2026-10-13
tags:
  - sistema/vault
  - guia
---
# Como Usar Este Vault

## A ideia central

Você **conta** o que aconteceu, do jeito que sair, e o agente (Claude Code ou Codex) **organiza**: escolhe a pasta, dá nome ao arquivo, monta o frontmatter, resume e liga a nota ao resto. O Obsidian é onde você **lê e navega**.

Três regras fazem tudo funcionar:

1. **Cada assunto tem sua pasta de contexto.** Trabalho, cliente, curso e pesquisa não se misturam.
2. **Toda nota tem `data` e `tags`.** Com `data`, ela aparece sozinha na linha do tempo e no calendário.
3. **Toda nota tem pelo menos um link.** No mínimo, para o `README` da pasta. Nota sem link se perde.

## O dia a dia

### 1. Contar

No terminal, dentro da pasta do vault, abra o agente (`claude`) e fale normalmente:

> tive reunião com a Marina da padaria, decidimos começar pela página de encomendas e preciso mandar a proposta até dia 20

### 2. O agente organiza

Ele cria `01_.../AAAA-MM-DD-reuniao-...md` com resumo, decisões e pendências. Se houver um prazo, cria **também** uma nota datada no dia do prazo, que aparece no calendário. No fim, atualiza o `README` da pasta. Se não der para saber o contexto, ele pergunta antes.

### 3. Você navega

- [[Home]]: o mapa.
- [[90_Visoes/linha-do-tempo.base|Linha do tempo]]: tudo por data, com vistas de tabela, por contexto, por mês e calendário.
- [[90_Visoes/painel-atual|Painel atual]]: no máximo 3 tarefas vivas por área.

## Tipos de nota

| O que aconteceu | Onde vai | Modelo |
|---|---|---|
| Reunião, aula, entrega, conversa de trabalho | pasta do contexto | `Template-Reuniao` |
| Prazo ou evento futuro | pasta do contexto, com `data:` = dia do evento | (nota curta) |
| Achei uma ferramenta ou repositório | `22_Ferramentas` | `Template-ProjetoExterno` |
| Li um artigo, livro ou ensaio | `21_Leituras` | `Template-Nota-Geral` |
| Li um paper técnico | `20_Estudos` ou o contexto da pesquisa | `Template-Paper` |
| Prompt que funcionou | `23_Prompts` | `Template-Prompt` |
| Tive uma ideia de projeto | `24_Ideias` | `Template-Ideia-Projeto` |
| Terminei algo e aprendi uma lição | `25_Experiencias` | `Template-Experiencia` |
| Trecho de código que resolve um problema | pasta do contexto | `Template-Snippet-Tecnico` |
| O dia | `81_Diario` (botão de nota diária) | `Template-Nota-Diaria` |

## Ciclo de vida das capturas

Ferramentas, leituras e estudos entram com um status **pendente**: `capturado`, `para-testar`, `para-ler`, `para-estudar` etc. Ficam 30 dias nesse estado. Depois disso, o agente oferece uma revisão rápida (uma vez por dia, no máximo) e cada captura vira:

- `adotado`: entrou em uso real;
- `referencia`: material de consulta permanente;
- `descartado`: não serviu (a nota fica, só sai da lista).

Isso evita o cemitério de links salvos que nunca foram abertos de novo.

## Comandos do agente

| Comando | O que faz |
|---|---|
| `/configurar-vault` | personaliza o vault: cria as suas pastas e reescreve as regras do agente |
| `/processar-rascunhos` | organiza notas soltas e revisa capturas com mais de 30 dias |
| `/vault-review` | relatório de notas órfãs, sem frontmatter, duplicadas ou mal nomeadas |
| `/briefing <tema>` | junta tudo o que o vault sabe sobre um tema |
| `/design-vault` | cria gráfico, slide ou tela seguindo o seu design aprovado |

## Sem agente

O vault também funciona à mão: use os modelos em `80_Templates` (`Ctrl+P` -> "Inserir modelo"), siga as três regras do começo e mantenha os `README` atualizados.

## Links

- [[Home]]
- [[CLAUDE|Regras do agente]]
