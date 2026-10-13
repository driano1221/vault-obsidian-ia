## Parte A - Rascunhos

Leia as notas recentes do vault e os arquivos com `status: rascunho` nas pastas de contexto e, para cada uma:

1. Confirme a pasta de destino correta, usando a seção "Estrutura Principal" do `CLAUDE.md` (contextos do usuário e pastas fixas).

2. Proponha um plano de ação completo:
   - nota original;
   - destino sugerido (pode ser a pasta atual, se já estiver correta);
   - nome de arquivo sugerido, sem espaços e sem acentos, no padrão `YYYY-MM-DD-slug.md`;
   - frontmatter YAML proposto com `data` (nunca `date`) e `tags`;
   - wikilinks para notas relacionadas já existentes no vault;
   - resumo de 3 linhas.

3. Antes de mover, renomear ou modificar qualquer arquivo, apresente o plano e pergunte ao usuário se pode prosseguir.

4. Após aprovação, execute: mova/renomeie os arquivos, adicione ou atualize o frontmatter e insira os wikilinks sugeridos.

5. Notas antigas já processadas ou substituídas não devem ser alteradas; apenas aponte duplicidades ou conflitos de contexto.

## Parte B - Capturas vencidas

Capturas com status pendente (`capturado`, `triagem`, `para-testar`, `testando`, `para-avaliar`, `para-estudar`, `para-ler`, `para-explorar`, `para-acompanhar`) têm prazo de 30 dias. Notas de referência (`referencia`, `ativo`, `adotado`) não têm prazo e não entram aqui.

1. Rode o script e use a saída como lista de trabalho:

   ```text
   python .claude/scripts/triagem_validade.py
   ```

   Ele lista cada captura vencida com dias sem revisão, quais pastas de projeto ou diário linkam para ela e uma sugestão inicial. O prazo pode ser trocado com `--dias N`.

2. Leia cada nota listada e confirme ou corrija a sugestão, com uma justificativa de uma linha baseada no conteúdo e nos links:
   - `adotado`: foi testada e entrou em uso real; deve existir link de/para o projeto ou experiência onde é usada.
   - `referencia`: material de consulta permanente (listas, catálogos, guias, bibliotecas de design, cursos que valem consultar), mesmo sem ter sido testado.
   - `descartado`: não serviu, ficou obsoleta ou não há motivo para consultar de novo.
   - `manter`: ainda faz sentido testar ou estudar em breve; continua com o status pendente atual.
   Na dúvida entre `referencia` e `descartado`, sugira `referencia`. Nunca sugira `descartado` só pela idade da nota.

3. Apresente uma tabela numerada (nota, status atual, dias, sugestão, justificativa) e deixe o usuário responder em lote, por exemplo `1-5 referencia, 7 descartado, resto ok`. Não altere nada antes da resposta.

4. Após aprovação, edite apenas o frontmatter de cada nota:
   - troque `status:` pelo valor decidido (em `manter`, preserve o status atual);
   - adicione ou atualize `revisado: YYYY-MM-DD` com a data de hoje, o que reinicia o prazo;
   - em `adotado`, pergunte em qual projeto a ferramenta é usada se não houver link, e adicione o wikilink nas duas notas.

5. Nunca mova, renomeie ou apague notas nesta parte. `descartado` permanece na pasta original.

6. Ao final, informe quantas notas foram para cada status e quantas pendências restam no prazo (`python .claude/scripts/triagem_validade.py --todas`).

