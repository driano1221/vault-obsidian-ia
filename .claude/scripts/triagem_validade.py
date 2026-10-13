#!/usr/bin/env python3
"""Lista capturas pendentes que passaram do prazo e a evidencia de uso de cada uma."""
import argparse
import datetime as dt
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]

PENDENTES = {
    "capturado", "triagem", "para-testar", "testando", "para-avaliar",
    "para-estudar", "para-ler", "para-explorar", "para-acompanhar",
}
IDEIAS = "24_Ideias"
DIARIO = "81_Diario"
IGNORAR = {".claude", ".obsidian", ".recall", ".trash", "80_Templates", "90_Visoes", "vendor", "node_modules"}
# Contextos do usuario sao as pastas 01_ a 19_; ideias e experiencias tambem contam como uso real.
CONTEXTO = re.compile(r"^(0[1-9]|1[0-9])_")
EXTRAS = {IDEIAS, "25_Experiencias"}


def eh_projeto(pasta):
    return bool(CONTEXTO.match(pasta)) or pasta in EXTRAS


PISTA_REFERENCIA = re.compile(
    r"lista|biblioteca|catalogo|galeria|referencia|recursos|sites|blogs|livros|videos|paletas|guia|cheatsheet"
    r"|awesome|top-\d|repositorios",
    re.I,
)

ESTADO = VAULT / ".claude" / "triagem-estado.json"

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---", re.S)
WIKILINK = re.compile(r"\[\[([^\]|#]+)")
TITULO = re.compile(r"^#\s+(.+)$", re.M)


def campo(frontmatter, nome):
    m = re.search(rf"^{nome}:\s*(.+?)\s*$", frontmatter, re.M)
    return m.group(1).strip("'\" ") if m else None


def para_data(valor):
    try:
        return dt.date.fromisoformat(valor[:10])
    except (TypeError, ValueError):
        return None


def carregar_notas():
    notas = {}
    for caminho in VAULT.rglob("*.md"):
        rel = caminho.relative_to(VAULT)
        if any(parte in IGNORAR for parte in rel.parts):
            continue
        texto = caminho.read_text(encoding="utf-8-sig", errors="ignore").replace("\r\n", "\n")
        m = FRONTMATTER.match(texto)
        notas[rel] = {
            "texto": texto,
            "fm": m.group(1) if m else "",
            "mtime": dt.date.fromtimestamp(caminho.stat().st_mtime),
        }
    return notas


def links_de_entrada(notas):
    por_nome = defaultdict(list)
    for rel in notas:
        por_nome[rel.stem.lower()].append(rel)
    entrada = defaultdict(set)
    for origem, nota in notas.items():
        for alvo in WIKILINK.findall(nota["texto"]):
            for destino in por_nome.get(Path(alvo.strip()).stem.lower(), []):
                if destino != origem:
                    entrada[destino].add(origem)
    return entrada


def sugerir(rel, titulo, usada_em):
    if usada_em - {DIARIO, IDEIAS}:
        return "adotado?"
    if IDEIAS in usada_em:
        return "manter? (ligada a ideia)"
    if PISTA_REFERENCIA.search(f"{rel.stem} {titulo}"):
        return "referencia?"
    return "decidir"


def triar(prazo, incluir_todas):
    hoje = dt.date.today()
    notas = carregar_notas()
    entrada = links_de_entrada(notas)
    resultado = []
    for rel, nota in notas.items():
        status = campo(nota["fm"], "status")
        if status not in PENDENTES:
            continue
        base = para_data(campo(nota["fm"], "revisado")) or para_data(campo(nota["fm"], "data")) or nota["mtime"]
        dias = (hoje - base).days
        if dias < prazo and not incluir_todas:
            continue
        usada_em = {o.parts[0] for o in entrada[rel] if eh_projeto(o.parts[0]) or o.parts[0] == DIARIO}
        m = TITULO.search(nota["texto"])
        titulo = m.group(1).strip() if m else rel.stem
        resultado.append({
            "nota": rel.as_posix(),
            "titulo": titulo,
            "status": status,
            "dias": dias,
            "usada_em": sorted(usada_em),
            "sugestao": sugerir(rel, titulo, usada_em),
        })
    return sorted(resultado, key=lambda r: -r["dias"])


def ja_ofereceu_hoje():
    try:
        estado = json.loads(ESTADO.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    return estado.get("ultima_oferta") == dt.date.today().isoformat()


def registrar_oferta():
    ESTADO.write_text(json.dumps({"ultima_oferta": dt.date.today().isoformat()}), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dias", type=int, default=30, help="prazo sem revisao (padrao: 30)")
    parser.add_argument("--todas", action="store_true", help="incluir pendencias ainda no prazo")
    parser.add_argument("--json", action="store_true", help="saida em JSON")
    parser.add_argument("--limite", type=int, help="mostrar no maximo N notas")
    parser.add_argument("--diario", action="store_true", help="nao imprime nada se ja ofereceu revisao hoje")
    args = parser.parse_args()

    sys.stdout.reconfigure(encoding="utf-8")
    if args.diario and ja_ofereceu_hoje():
        return
    itens = triar(args.dias, args.todas)
    total = len(itens)
    itens = itens[: args.limite] if args.limite else itens
    if args.diario and itens:
        registrar_oferta()

    if args.json:
        print(json.dumps(itens, ensure_ascii=False, indent=2))
        return

    if not itens:
        return
    print(f"{total} capturas pendentes com {args.dias}+ dias sem revisao (mostrando {len(itens)})\n")
    print("| # | Nota | Status | Dias | Linkada por | Sugestao |")
    print("|---|---|---|---|---|---|")
    for i, r in enumerate(itens, 1):
        usada = ", ".join(r["usada_em"]) or "-"
        print(f"| {i} | [[{r['nota'][:-3]}\\|{r['titulo']}]] | {r['status']} | {r['dias']} | {usada} | {r['sugestao']} |")


if __name__ == "__main__":
    main()
