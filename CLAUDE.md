# CLAUDE.md - Base de Conhecimento Pessoal

> Se este vault ainda não foi configurado (a seção "Contexto do Usuário" abaixo ainda diz "a configurar"), sugira ao usuário rodar `/configurar-vault` antes de qualquer outra coisa.

## Papel do Agente

Este vault é uma base de conhecimento pessoal em Obsidian. O agente atua como organizador, bibliotecário e assistente de registro: transforma relatos em notas estruturadas e mantém cada assunto no contexto certo.

## Contexto do Usuário

%% perfil:inicio %%
- Usuário: a configurar (rode `/configurar-vault`).
%% perfil:fim %%

Detalhes mais longos sobre a pessoa e cada área ficam em `sobre-mim.md`, na raiz do vault. Leia essa nota no início de cada sessão.

## Estrutura Principal

### Contextos do usuário (01 a 19)

Cada área de vida ou trabalho com assunto próprio tem sua pasta. Estas pastas são criadas pelo `/configurar-vault`.

%% contextos:inicio %%
- `01_Exemplo_Trabalho` -> pasta de exemplo; o `/configurar-vault` substitui pelos contextos reais.
%% contextos:fim %%

### Pastas fixas

- `20_Estudos` -> estudos, cursos, aulas e conceitos.
- `21_Leituras` -> leituras gerais: ensaios, artigos, livros.
- `22_Ferramentas` -> ferramentas, frameworks e repositórios interessantes.
- `23_Prompts` -> prompts reutilizáveis e versionados.
- `24_Ideias` -> ideias de projetos, MVPs e experimentos em fase inicial.
- `25_Experiencias` -> lições aprendidas e retrospectivas.
- `26_Design` -> design e gráficos: dicionário, regras aprovadas e galeria.
- `27_Pessoal` -> vida pessoal: prazos, lembretes, datas, receitas.
- `80_Templates` -> modelos de nota.
- `81_Diario` -> notas diárias.
- `90_Visoes` -> visões automáticas (linha do tempo, calendário, painel).
- `99_Anexos` -> imagens e anexos.

## Hard Rules

- ALWAYS: responder e estruturar notas em português do Brasil.
- ALWAYS: adicionar `data` (nunca `date`) e `tags` no frontmatter de novas notas Markdown.
- ALWAYS: usar nomes de arquivo sem espaços e sem acentos, em minúsculas e com hífens, no padrão `YYYY-MM-DD-assunto.md` para notas datadas.
- ALWAYS: adicionar pelo menos um wikilink relevante, de preferência para o `README.md` da pasta.
- ALWAYS: ao criar uma nota, listá-la no topo da seção "Arquivos Desta Pasta" do `README.md` da pasta (na primeira vez, apagando o texto entre parênteses que está lá).
- ALWAYS: toda data futura citada (prazo, entrega, prova, reunião marcada) vira também uma nota própria, curta, na pasta do contexto, com `data:` igual à data do evento, nome `AAAA-MM-DD-prazo-assunto.md`, `status: agendado` e link para a nota de origem. Sem isso, o evento não aparece no calendário.
- ALWAYS: usar a pasta de contexto correta em vez de misturar assuntos.
- ALWAYS: se o contexto estiver claro, salvar direto na pasta correta; não usar Inbox.
%% regras:inicio %%
%% regras:fim %%
- NEVER: apagar conteúdo do vault sem pedido explícito.

## Fluxo de Trabalho

- Se o usuário narrar algo que aconteceu, transformar em nota estruturada no contexto correto.
- Se o usuário despejar algo cru ou ambíguo, pedir uma clarificação curta quando houver risco real de contexto errado; se for seguro inferir, salvar direto.
- Antes de criar nota, procurar se já existe uma sobre o assunto; se existir, atualizar em vez de duplicar.
- Se uma nota virar conhecimento reutilizável, incluir resumo, seções claras, links relacionados e próximas ações quando fizer sentido.
- Toda nota com `data` no frontmatter aparece em `90_Visoes/linha-do-tempo.base` (tabela e calendário).
- Evento futuro (prova, prazo, entrega, reunião marcada) vira uma nota própria com `data:` igual à data do evento, não à de hoje. Assim ele aparece no calendário.

## Tarefas Comuns

Registrar reunião:
- criar nota datada no contexto correto (modelo em `80_Templates/Template-Reuniao.md`);
- resumir pontos principais e listar pendências;
- para cada prazo citado, criar a nota de prazo datada (regra acima);
- linkar ao `README.md` da pasta e atualizar a lista dele.

Salvar prompt:
- usar `23_Prompts`;
- registrar objetivo, prompt completo, modelo testado e exemplo.

Salvar experiência:
- usar `25_Experiencias`;
- registrar contexto, o que funcionou, o que não funcionou e lições aprendidas.

Salvar descoberta de ferramenta:
- usar `22_Ferramentas`;
- registrar resumo, potencial de uso, links e status.

Salvar ideia de projeto:
- usar `24_Ideias`;
- registrar problema, ideia central, valor esperado, MVP e status.

Criar algo visual (gráfico, mapa, slides, dashboard, app, tela):
- usar a skill `design-vault`;
- ela segue `26_Design/dicionario-design.md`, `regras-de-design-aprovadas.md` e `galeria-design.md`.

## Ciclo de Vida das Capturas

- Pendente (prazo de 30 dias): `capturado`, `triagem`, `para-testar`, `testando`, `para-avaliar`, `para-estudar`, `para-ler`, `para-explorar`, `para-acompanhar`.
- Permanente (sem prazo): `referencia`, `ativo`, `adotado`.
- Encerrado: `descartado` (a nota fica na pasta, só sai das pendências).
- Toda captura nova de ferramenta, leitura ou estudo entra com um status pendente. Material claramente de consulta (lista de recursos, catálogo, guia, galeria) pode entrar direto como `referencia`.
- Ao revisar uma nota, registrar `revisado: YYYY-MM-DD` no frontmatter.
- Revisão diária no chat: depois de salvar qualquer captura, rodar `python .claude/scripts/triagem_validade.py --diario --limite 5` (na raiz do vault; se `python` não existir, usar `python3` no Mac/Linux ou `py` no Windows). Se não imprimir nada, seguir normalmente. Se imprimir uma tabela, terminar a resposta com uma única linha oferecendo revisar essas notas. Se o usuário aceitar, seguir a Parte B de `.claude/commands/processar-rascunhos.md` só para elas. Se ignorar, não insistir no mesmo dia.

## Ponto de Partida

- `Home.md` para navegação geral.
- `sobre-mim.md` para saber quem é a pessoa e o que importa em cada área.
- `README.md` de cada pasta como índice local.
- `como-usar-vault.md` para o fluxo de uso humano.
- `90_Visoes/linha-do-tempo.base` para ver tudo por data.
