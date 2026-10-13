Faca uma varredura completa do vault (todas as pastas, exceto `.claude`, `.obsidian` e `80_Templates`, mais os arquivos da raiz) e produza um relatorio com:

1. **Conexoes sugeridas**: pares de notas que deveriam ter wikilinks entre si, com justificativa breve.
2. **Notas sem frontmatter**: arquivos `.md` sem bloco YAML inicial.
3. **Notas orfas**: notas sem wikilinks de entrada ou saida.
4. **Notas candidatas a divisao**: notas longas ou misturando assuntos.
5. **Notas candidatas a consolidacao**: notas muito parecidas que poderiam virar uma nota principal.
6. **Problemas de padronizacao**: nomes de arquivo com espaco/acento, tags inconsistentes ou contextos misturados contra as regras do `CLAUDE.md`.

Apresente o relatorio completo e pergunte ao usuario quais acoes deseja executar antes de modificar qualquer arquivo.
