#!/usr/bin/env python3
"""Instala o plugin Calendar Bases (vista Calendario da linha do tempo) neste vault.

Baixa a versao mais recente direto do GitHub do autor
(https://github.com/edrickleong/obsidian-calendar-bases) e a ativa em
.obsidian/community-plugins.json. O Obsidian pede, na primeira abertura,
para confiar no autor do cofre: so assim os plugins rodam.
"""
import json
import sys
import urllib.request
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
REPO = "edrickleong/obsidian-calendar-bases"
ID = "calendar-bases"
ARQUIVOS = ("main.js", "manifest.json", "styles.css")


def baixar(url):
    pedido = urllib.request.Request(url, headers={"User-Agent": "vault-obsidian-ia"})
    with urllib.request.urlopen(pedido, timeout=60) as resposta:
        return resposta.read()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    versao = json.loads(baixar(f"https://api.github.com/repos/{REPO}/releases/latest"))
    anexos = {a["name"]: a["browser_download_url"] for a in versao["assets"]}
    faltando = [a for a in ("main.js", "manifest.json") if a not in anexos]
    if faltando:
        print(f"A versao {versao['tag_name']} nao tem {faltando}; nada foi instalado.")
        return 1

    destino = VAULT / ".obsidian" / "plugins" / ID
    destino.mkdir(parents=True, exist_ok=True)
    for nome in ARQUIVOS:
        if nome in anexos:
            (destino / nome).write_bytes(baixar(anexos[nome]))

    lista = VAULT / ".obsidian" / "community-plugins.json"
    ativos = json.loads(lista.read_text(encoding="utf-8")) if lista.exists() else []
    if ID not in ativos:
        ativos.append(ID)
        lista.write_text(json.dumps(ativos, indent=2), encoding="utf-8")

    print(f"Calendar Bases {versao['tag_name']} instalado e ativado.")
    print("Na primeira abertura, o Obsidian pergunta se voce confia no autor do cofre: clique em 'Confiar no autor e habilitar plugins'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
