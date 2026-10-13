Configure este vault para a pessoa que está usando. Ele veio de um modelo com uma pasta de exemplo (`01_Exemplo_Trabalho`) e notas fictícias de demonstração; o objetivo é trocar isso pelas áreas reais dela, sem que ela precise editar nada à mão.

Argumentos opcionais: $ARGUMENTS

## 1. Ver o estado atual

- Leia `CLAUDE.md`, `Home.md`, `80_Templates/Template-Nota-Diaria.md` e `.claude/exemplos.txt`.
- Se o bloco `<!-- perfil:inicio -->` do `CLAUDE.md` já tiver um nome (não diz "a configurar"), o vault já foi configurado. Pergunte se a pessoa quer **acrescentar contextos**, **renomear algum** ou **refazer o perfil**, e faça só isso.

## 2. Perguntar, em um lote só

Faça estas perguntas de uma vez, em linguagem simples, com um exemplo em cada:

1. **Como posso te chamar, e o que você faz?** (ex.: "Ana, designer freelancer e estudante de pós em UX")
2. **Quais são as grandes áreas da sua vida que geram anotações?** Uma por linha, com uma frase sobre cada. São coisas que não devem se misturar: empregos, clientes, curso, pesquisa, um projeto grande. (ex.: "Cliente Acme: sites institucionais"; "Pós UX: disciplinas e TCC")
3. **Tem alguma regra de separação?** (ex.: "nunca misturar Cliente Acme com Cliente Beta na mesma nota", "o que é da pesquisa X é confidencial")
4. **Quer manter as notas de exemplo** para ver como o vault funciona, **ou apagar** e começar limpo?

Não pergunte o que já respondeu nos argumentos. As pastas fixas (Estudos, Leituras, Ferramentas, Prompts, Ideias, Experiências, Design, Pessoal) já existem; só crie contexto novo para o que não cabe nelas.

## 3. Propor o plano e esperar o ok

Mostre numa tabela:

| Pasta | O que guarda |
|---|---|
| `01_Nome_Curto` | frase da pessoa |

Regras para os nomes:
- numeração de `01` a `19`, na ordem que ela citou;
- sem espaços nem acentos, palavras com inicial maiúscula separadas por `_` (ex.: `02_Pos_UX`, `03_Cliente_Acme`);
- curtos: até três palavras.

Diga também o que acontece com a pasta e as notas de exemplo (manter ou apagar, segundo a resposta 4). **Não crie nem apague nada antes do ok.**

## 4. Executar

Depois do ok:

1. **Criar cada pasta de contexto** com um `README.md`:

   ```markdown
   ---
   data: AAAA-MM-DD (hoje)
   tags:
     - indice
     - <nome-do-contexto-em-minusculas-com-hifens>
   ---
   # <Nome legível>

   <frase da pessoa sobre o contexto>

   ## Arquivos Desta Pasta

   (o agente acrescenta aqui cada nota nova, a mais recente no topo)

   ## Links

   - [[Home]]
   ```

2. **Atualizar os blocos marcados**, trocando só o que está entre os marcadores e mantendo os marcadores:
   - `CLAUDE.md`, bloco `perfil`: nome, o que a pessoa faz e as áreas, em 2 a 4 linhas;
   - `CLAUDE.md`, bloco `contextos`: uma linha por pasta, no formato `` - `01_Nome` -> descrição. ``;
   - `CLAUDE.md`, bloco `regras`: uma linha `- NEVER: ...` por regra de separação da resposta 3. Se não houver, deixe vazio;
   - `Home.md`, bloco `contextos`: `- [[01_Nome/README|Nome legível]]` para cada pasta;
   - `80_Templates/Template-Nota-Diaria.md`, bloco `contextos`: uma subseção `### Nome legível` com `- [ ] ` embaixo, para cada contexto.

3. **Escrever `.claude/context/perfil.md`** com o que a pessoa contou (quem é, áreas, regras), para o agente ter contexto nas próximas sessões. Se ela tiver falado mais de uma área em detalhe, crie um arquivo por área em `.claude/context/`.

4. **Notas de exemplo:**
   - **Se ela pediu para apagar:** apague os arquivos listados em `.claude/exemplos.txt`, a pasta `01_Exemplo_Trabalho` (se o nome não foi reaproveitado) e o próprio `exemplos.txt`. Depois, tire do `90_Visoes/painel-atual.md` as tarefas de exemplo e deixe uma seção vazia por contexto.
   - **Se pediu para manter:** não toque nelas. Avise que dá para rodar `/configurar-vault apagar exemplos` depois.

5. **Conferir:**
   - todo wikilink novo aponta para um arquivo que existe;
   - nenhum bloco marcado ficou duplicado;
   - `90_Visoes/linha-do-tempo.base` não precisa mudar, porque o contexto vem do nome da pasta.

## 5. Fechar

Responda curto:
- as pastas criadas;
- o que mudou no `CLAUDE.md`, no `Home.md` e no modelo de diário;
- os próximos passos manuais, que só ela pode fazer no Obsidian:
  - instalar o plugin **Calendar Bases**, que dá a vista Calendário;
  - na primeira vez que abrir a vista Calendário, definir `Start date` = `data`;
  - opcional: preencher `26_Design` aos poucos.

Termine sugerindo um primeiro uso real, por exemplo: "me conta algo que aconteceu hoje em uma dessas áreas que eu transformo na primeira nota".
