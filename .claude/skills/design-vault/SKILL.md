---
name: design-vault
description: Transforma dados, ideias e pedidos do usuário em um produto visual (gráfico, mapa, slides, dashboard, app, tela, diagrama) seguindo o design aprovado no vault Obsidian dele, em vez de um estilo inventado pelo agente. Lê o dicionário, as regras e a galeria de design do vault, pergunta só o que falta, propõe um rascunho, implementa e confere o render antes de entregar. Use quando o usuário invocar /design-vault, disser "segue meu design", "usa minhas paletas/regras", ou pedir algo visual novo mandando dados ou uma ideia ("tenho esse CSV e quero mostrar...", "monta uns slides sobre..."). NÃO usar para ajuste pontual em visual já existente (trocar uma cor, mover um rótulo) nem para perguntas teóricas sobre design.
---

# Design pelo Vault

O vault já guarda o gosto visual do usuário. Esta skill obriga o agente a usar esse conhecimento antes de desenhar qualquer coisa. O agente traz técnica; o vault traz o estilo e os exemplos.

## Fonte da verdade (ler, nunca copiar para cá)

Pasta `26_Design/`, na raiz do vault:

- `dicionario-design.md`: situação -> o que usar -> status.
- `regras-de-design-aprovadas.md`: estilo base, paletas e regras por tipo de peça.
- `galeria-design.md`: imagens aprovadas e rejeitadas, com o motivo. Imagens em `99_Anexos/design-galeria/`.
- Trabalho de um contexto com identidade própria (cliente, empresa, instituição): a identidade do contexto vence o estilo pessoal. Procure na pasta do contexto.

Nunca reescrever regras dentro desta skill nem no artefato gerado. Se uma regra parecer errada ou velha, avisar o usuário; não corrigir por conta própria.

**Se as três notas ainda estiverem quase vazias:** diga isso no início, siga boas práticas neutras (um destaque por peça, título com o fato, sem "cara de IA") e use o passo 6 para começar a preencher o vault com o usuário.

## Fluxo

### 1. Ler antes de falar

Ler `dicionario-design.md` e `regras-de-design-aprovadas.md` inteiros, e na galeria **abrir e olhar** as imagens do mesmo tipo de peça. Não perguntar nada que o vault já responde.

Se este modelo não consegue ver imagem, ler as linhas "Por que" da galeria e avisar logo no início que a conferência visual vai depender do usuário.

### 2. Perguntar o que falta, num lote só (no máximo 4 perguntas)

Só as que o pedido e o vault não responderam:
- público e onde vai ser visto (reunião, artigo, rede social, uso próprio);
- formato de entrega (HTML, .pptx, PNG 4:5, PNG para web, PDF);
- a mensagem ou decisão principal que o visual precisa passar;
- referência visual, se houver ("parecido com X").

### 3. Propor antes de construir

Mostrar em poucas linhas:
- o que vai fazer (tipo de gráfico ou layout) e por quê;
- quais regras, qual paleta e qual exemplo da galeria vai seguir, citando a nota;
- um rascunho barato: esboço, protótipo simples ou primeira versão com o dado real.

Esperar o ok. Referência visual se abre e se olha; nunca se descreve de memória.

### 4. Implementar

- Usar as cores, fontes e tamanhos das regras; não inventar outros.
- Se o vault tiver código base de tema (por exemplo, um `tema.R` ou `tema.py` em `26_Design/codigo/`), começar por ele.
- Chamar as skills técnicas que existirem neste agente (dataviz, frontend, Quarto, etc.), trocando a paleta genérica delas pela aprovada.

### 5. Conferir o render antes de entregar

Nada é entregue sem ter sido renderizado e olhado.

1. Renderizar no tamanho real de entrega (PNG, GIF, HTML). Em tela, tirar screenshot em desktop e em celular (375 px).
2. Abrir a imagem e passar a lista:
   - texto sobre texto, sobre linha ou sobre ponto importante;
   - texto cortado ou encostado na borda;
   - legível no tamanho real de uso;
   - idioma único (meses, datas, separador decimal);
   - título com o fato que o dado sustenta;
   - um destaque só, o resto em cinza;
   - comparado lado a lado com o exemplo aprovado da galeria: se parece mais com o rejeitado, refazer.
3. Achou problema: corrigir e voltar ao item 1.
4. Modelo sem visão: dizer claramente "não consegui olhar a imagem" e pedir ao usuário que abra antes de dar como pronto.

Na entrega, dizer em uma linha o que foi conferido.

### 6. Fechar o ciclo

Ao entregar, em no máximo 2 linhas:
- se alguma decisão nova funcionou e parece reutilizável, perguntar se vira regra em `regras-de-design-aprovadas.md` e linha no dicionário;
- se o usuário aprovou ou rejeitou a peça, perguntar se ela entra na galeria (com o "por que").

Só editar o vault com o sim dele.
