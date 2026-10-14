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

## Começar (tudo pelo Claude Code)

Você precisa só de duas coisas instaladas: o [Obsidian](https://obsidian.md) e o [Claude Code](https://claude.com/claude-code). Do resto, o agente cuida.

**1.** Abra o terminal na pasta onde quer guardar o vault (por exemplo, Documentos), rode `claude` e cole:

```text
Baixe o zip https://github.com/driano1221/vault-obsidian-ia/archive/refs/heads/master.zip,
extraia o conteúdo (sem a pasta interna extra) numa pasta chamada MeuVault aqui,
e apague o zip. Depois leia o CLAUDE.md dessa pasta e siga
.claude/commands/configurar-vault.md comigo.
```

Troque `MeuVault` pelo nome que quiser; ele vira o nome do cofre no Obsidian.

**2.** Responda as 4 perguntas do agente: quem você é, suas áreas (trabalho, clientes, curso...), se há regras de separação e se quer manter as notas de exemplo. Ele mostra o plano e só mexe em algo depois do seu ok.

**3.** O agente cria suas pastas, instala o plugin do calendário e abre o Obsidian no vault novo. Ali aparece uma única pergunta, **"Você confia no autor deste cofre?"**: clique em **Confiar no autor e habilitar plugins**. É o único clique da instalação.

**4.** Para o dia a dia, abra o terminal **dentro** da pasta do vault e rode `claude`. Assim as regras e os comandos `/` carregam sozinhos.

```bash
cd MeuVault
claude
```

## O que pedir no dia a dia

Fale normalmente, como contaria a alguém:

| Você diz | O agente faz |
|---|---|
| "tive reunião com a Marina, decidimos X, a entrega é dia 20" | nota da reunião na pasta certa + nota do prazo no calendário |
| "achei essa ferramenta: [link], quero testar" | captura em Ferramentas, com 30 dias para virar adotada, referência ou descartada |
| "li esse artigo: [link]" | nota em Leituras com resumo |
| "tive uma ideia: ..." | nota em Ideias com problema, ideia central e próximo passo |
| "o que eu tenho de prazo esta semana?" | busca nas notas com data |
| "abre no Obsidian" / "quero ver o calendário" | abre o Obsidian no vault |
| `/briefing <tema>` | junta tudo o que o vault sabe sobre um tema |
| `/processar-rascunhos` | revisa notas soltas e capturas paradas há mais de 30 dias |
| `/vault-review` | relatório de notas órfãs, links faltando e nomes fora do padrão |
| `/design-vault faz um gráfico com esse CSV` | gráfico, slide ou tela seguindo as suas regras de design |
| `/configurar-vault` | acrescenta ou renomeia áreas depois; `/configurar-vault apagar exemplos` limpa os exemplos |

No Codex, o arquivo de regras é o `AGENTS.md`; para configurar, peça "leia `.claude/commands/configurar-vault.md` e siga os passos".

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
.claude/        comandos, skills e script de triagem do agente
sobre-mim.md    quem você é e suas áreas (preenchida pelo /configurar-vault)
```

## Privacidade

Se você versionar o **seu** vault no GitHub, deixe o repositório **privado**. A nota `sobre-mim.md` guarda o que você contou ao agente sobre você.

## Créditos e licença

- Skills de Obsidian em `.claude/skills/` (exceto `design-vault`): [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills), licença MIT (`.claude/skills/LICENSE-obsidian-skills`).
- Plugin de calendário: [Calendar Bases](https://github.com/edrickleong/obsidian-calendar-bases), de Edrick Leong (não incluído no repositório; o script `.claude/scripts/instalar_calendario.py` baixa a versão mais recente do GitHub do autor).
- O restante do modelo está sob licença MIT (`LICENSE`).
