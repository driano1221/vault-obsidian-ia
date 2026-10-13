#!/usr/bin/env python3
"""Registra este vault no Obsidian (se preciso) e abre o Obsidian nele.

Codigos de saida:
  0  aberto (ou pedido de abertura enviado)
  2  Obsidian nao encontrado neste computador: instale em https://obsidian.md
  3  o vault ainda nao esta registrado e o Obsidian esta aberto: feche o Obsidian e rode de novo
"""
import json
import os
import platform
import secrets
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
SISTEMA = platform.system()


def pasta_config():
    casa = Path.home()
    if SISTEMA == "Windows":
        candidatas = [Path(os.environ.get("APPDATA", casa / "AppData" / "Roaming")) / "obsidian"]
    elif SISTEMA == "Darwin":
        candidatas = [casa / "Library" / "Application Support" / "obsidian"]
    else:
        candidatas = [
            Path(os.environ.get("XDG_CONFIG_HOME", casa / ".config")) / "obsidian",
            casa / ".var" / "app" / "md.obsidian.Obsidian" / "config" / "obsidian",
            casa / "snap" / "obsidian" / "current" / ".config" / "obsidian",
        ]
    for pasta in candidatas:
        if (pasta / "obsidian.json").exists():
            return pasta
    return None


def obsidian_aberto():
    try:
        if SISTEMA == "Windows":
            saida = subprocess.run(["tasklist", "/FI", "IMAGENAME eq Obsidian.exe"],
                                   capture_output=True, text=True, errors="ignore").stdout
            return "obsidian.exe" in saida.lower()
        saida = subprocess.run(["pgrep", "-if", "obsidian"], capture_output=True, text=True).stdout
        return bool(saida.strip())
    except OSError:
        return False


def mesmo_caminho(a, b):
    return os.path.normcase(os.path.normpath(a)) == os.path.normcase(os.path.normpath(b))


def abrir_uri(uri):
    if SISTEMA == "Windows":
        os.startfile(uri)
    elif SISTEMA == "Darwin":
        subprocess.run(["open", uri], check=False)
    else:
        subprocess.run(["xdg-open", uri], check=False)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pasta = pasta_config()
    if pasta is None:
        print("Obsidian nao encontrado neste computador. Instale em https://obsidian.md, abra uma vez e rode de novo.")
        return 2

    arquivo = pasta / "obsidian.json"
    dados = json.loads(arquivo.read_text(encoding="utf-8"))
    cofres = dados.setdefault("vaults", {})
    registrado = any(mesmo_caminho(v.get("path", ""), VAULT) for v in cofres.values())

    if not registrado:
        # O Obsidian leva alguns segundos para encerrar todos os processos depois de fechado.
        for _ in range(30):
            if not obsidian_aberto():
                break
            time.sleep(1)
        else:
            print("O Obsidian esta aberto e ainda nao conhece este vault. Feche o Obsidian (todas as janelas) e rode de novo.")
            return 3
        cofres[secrets.token_hex(8)] = {"path": str(VAULT), "ts": int(time.time() * 1000)}
        arquivo.write_text(json.dumps(dados), encoding="utf-8")
        print(f"Vault registrado no Obsidian: {VAULT}")

    abrir_uri("obsidian://open?vault=" + urllib.parse.quote(VAULT.name))
    print(f"Abrindo o Obsidian no vault '{VAULT.name}'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
