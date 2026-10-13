# Vault Obsidian com IA

Um modelo de base de conhecimento pessoal em [Obsidian](https://obsidian.md), pensado para trabalhar junto com um agente de IA ([Claude Code](https://claude.com/claude-code) ou Codex). Você conta o que aconteceu do jeito que sair; o agente escolhe a pasta, nomeia o arquivo, monta o frontmatter, resume e liga a nota ao resto do vault.

O modelo traz a estrutura, as regras e as automações, **não** as notas de ninguém. Na primeira vez, o comando `/configurar-vault` pergunta quais são as suas áreas (trabalho, clientes, curso, pesquisa...) e cria as pastas certas para você.

## O que vem

- **Estrutura de pastas** numerada: contextos seus (01 a 19), pastas fixas (Estudos, Leituras, Ferramentas, Prompts, Ideias, Experiências, Design, Pessoal) e sistema (Templates, Diário, Visões, Anexos).
- **Regras do agente** em `CLAUDE.md` (Claude Code) e `AGENTS.md` (Codex e outros): nomes de arquivo, frontmatter, onde salvar cada tipo de nota, nunca misturar contextos, nunca apagar sem pedir.
- **Linha do tempo e calendário** com Obsidian Bases: toda nota com `data:` aparece sozinha, inclusive prazos futuros.
- **Painel atual**: no máximo 3 tarefas vivas por área.
- **9 modelos de nota**: reunião, diário, ideia, experiência, paper, prompt, ferramenta, snippet e nota geral.
- **Ciclo de vida das capturas**: ferramentas e leituras salvas têm 30 dias para virar `adotado`, `referencia` ou `descartado`; um script avisa quando passam do prazo.
- **Comandos**: `/configurar-vault`, `/processar-rascunhos`, `/vault-review`, `/briefing`.
- **Design**: a skill `/design-vault` faz gráficos, slides e telas seguindo as regras e a galeria que **você** aprova, em vez de um estilo genérico de IA.
- **Skills de Obsidian** ([kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)): Markdown do Obsidian, Bases, Canvas, CLI e extração de páginas web.
- **Notas de exemplo** fictícias, para ver tudo funcionando antes de começar. O `/configurar-vault` apaga se você quiser.

## Começar

1. **Pegue uma cópia:** botão **Use this template** (cria um repositório seu) ou **Code -> Download ZIP**.
2. **Abra no Obsidian:** *Abrir pasta como cofre* e escolha a pasta.
3. **Instale o plugin do calendário** (opcional, mas recomendado):
   - Configurações -> Plugins da comunidade -> ative os plugins da comunidade;
   - procure **Calendar Bases**. Se não aparecer na busca, instale o plugin **BRAT** e, nele, adicione `edrickleong/obsidian-calendar-bases`;
   - abra `90_Visoes/linha-do-tempo.base`, vá na vista **Calendário**, clique na engrenagem e defina `Start date` = `data`.
4. **Configure com o agente:** no terminal, dentro da pasta do vault:

   ```bash
   claude
   ```

   e depois digite `/configurar-vault`. Ele faz 4 perguntas, mostra o plano e só cria as pastas depois do seu ok.

   No Codex, peça: "leia `.claude/commands/configurar-vault.md` e siga os passos".

Sem agente, o vault também funciona: use os modelos em `80_Templates` e o guia `como-usar-vault.md`.

## Estrutura

```
01_..19_        seus contextos (criados pelo /configurar-vault)
20_Estudos      estudos, cursos, aulas
21_Leituras     ensaios, artigos, livros
22_Ferramentas  ferramentas e repositórios
23_Prompts      prompts versionados
24_Ideias       ideias de projeto
25_Experiencias lições aprendidas
26_Design       dicionário, regras e galeria de design
27_Pessoal      prazos, lembretes, receitas
80_Templates    modelos de nota
81_Diario       notas diárias
90_Visoes       linha do tempo, calendário, painel
99_Anexos       imagens e anexos
.claude/        comandos, skills, script de triagem e contexto do agente
```

## Privacidade

Se você versionar o **seu** vault no GitHub, deixe o repositório **privado**. A pasta `.claude/context/` guarda o que você contou ao agente sobre você.

## Créditos e licença

- Skills de Obsidian em `.claude/skills/` (exceto `design-vault`): [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills), licença MIT (`.claude/skills/LICENSE-obsidian-skills`).
- Plugin de calendário: [Calendar Bases](https://github.com/edrickleong/obsidian-calendar-bases), de Edrick Leong (não incluído, instale pelo Obsidian).
- O restante do modelo está sob licença MIT (`LICENSE`).
