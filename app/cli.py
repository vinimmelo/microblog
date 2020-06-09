# coding: utf-8
import click

from app import app
import os


@app.cli.group()
def translate():
    """Comando de tradução para linha de comando"""
    pass


@translate.command()
def update():
    if os.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
        raise RuntimeError("comando de extração falhou")
    if os.system("pybabel update -i messages.pot -d app/translations"):
        raise RuntimeError("comando de update falhou")
    os.remove("messages.pot")


@translate.command()
def compile():
    if os.system("pybabel compile -d app/translations"):
        raise RuntimeError("erro de compilação")


@translate.command()
@click.argument("lang")
def init(lang):
    if os.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
        raise RuntimeError("comando de extração falhou")
    if os.system("pybabel init -i messages.pot -d app/translations -l " + lang):
        raise RuntimeError("comando de inicialização falhou")
    os.remove("messages.pot")
