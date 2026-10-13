Faça uma varredura completa do vault (todas as pastas, exceto `.claude`, `.obsidian` e `80_Templates`, mais os arquivos da raiz) e produza um relatório com:

1. **Conexões sugeridas**: pares de notas que deveriam ter wikilinks entre si, com justificativa breve.
2. **Notas sem frontmatter**: arquivos `.md` sem bloco YAML inicial.
3. **Notas órfãs**: notas sem wikilinks de entrada ou saída.
4. **Notas candidatas a divisão**: notas longas ou misturando assuntos.
5. **Notas candidatas a consolidação**: notas muito parecidas que poderiam virar uma nota principal.
6. **Problemas de padronização**: nomes de arquivo com espaço/acento, tags inconsistentes ou contextos misturados contra as regras do `CLAUDE.md`.

Apresente o relatório completo e pergunte ao usuário quais ações deseja executar antes de modificar qualquer arquivo.
