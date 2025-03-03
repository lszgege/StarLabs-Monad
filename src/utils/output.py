import os
from rich.console import Console
from rich.text import Text
from tabulate import tabulate
from rich.table import Table
from rich import box
from typing import List
from prompt_toolkit import Application
from prompt_toolkit.layout import Layout, Window, HSplit
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style


def show_logo():
    """Отображает стильный логотип STARLABS"""
    # Очищаем экран
    os.system("cls" if os.name == "nt" else "clear")

    console = Console()

    # Создаем звездное небо со стилизованным логотипом
    logo_text = """
✦ ˚ . ⋆   ˚ ✦  ˚  ✦  . ⋆ ˚   ✦  . ⋆ ˚   ✦ ˚ . ⋆   ˚ ✦  ˚  ✦  . ⋆   ˚ ✦  ˚  ✦  . ⋆ ✦ ˚ 
. ⋆ ˚ ✧  . ⋆ ˚  ✦ ˚ . ⋆  ˚ ✦ . ⋆ ˚  ✦ ˚ . ⋆  ˚ ✦ . ⋆ ˚  ✦ ˚ . ⋆  ˚ ✦ . ⋆  ˚ ✦ .✦ ˚ . 
·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚ ⋆｡⋆｡. ★ ·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚ ·˚ ★ ·˚
         ____                                       ____                       
        /\  _`\                  __                /\  _`\                     
        \ \,\L\_\  _____   _ __ /\_\    ___      __\ \ \/\ \     __      ___   
         \/_\__ \ /\ '__`\/\`'__\/\ \ /' _ `\  /'_ `\ \ \ \ \  /'__`\   / __`\ 
           /\ \L\ \ \ \L\ \ \ \/ \ \ \/\ \/\ \/\ \L\ \ \ \_\ \/\ \L\.\_/\ \L\ \ 
           \ `\____\ \ ,__/\ \_\  \ \_\ \_\ \_\ \____ \ \____/\ \__/.\_\ \____/
            \/_____/\ \ \/  \/_/   \/_/\/_/\/_/\/___L\ \/___/  \/__/\/_/\/___/ 
                     \ \_\                       /\____/                     
                      \/_/                       \_/__/                       
·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚ ⋆｡⋆｡. ★ ·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚·˚ ⋆｡⋆｡.
. ⋆ ˚ ✧  . ⋆ ˚  ✦ ˚ . ⋆  ˚ ✦ . ⋆ ˚  ✦ ˚ . ⋆  ˚ ✦ . ⋆ ˚  ✦ ˚ . ⋆  ˚ ✦ . ⋆  ˚ ✦ .. ⋆  ˚ 
✦ ˚ . ⋆   ˚ ✦  ˚  ✦  . ⋆ ˚   ✦  . ⋆ ˚   ✦ ˚ . ⋆   ˚ ✦  ˚  ✦  . ⋆   ˚ ✦  ˚  ✦  . ⋆  ✦
"""

    # Создаем градиентный текст
    gradient_logo = Text(logo_text)
    gradient_logo.stylize("bold bright_cyan")

    # Выводим с отступами
    console.print(gradient_logo)
    print()


def show_dev_info():
    """Displays development and version information"""
    console = Console()

    # Создаем красивую таблицу
    table = Table(
        show_header=False,
        box=box.DOUBLE,
        border_style="bright_cyan",
        pad_edge=False,
        width=49,
        highlight=True,
    )

    # Добавляем колонки
    table.add_column("Content", style="bright_cyan", justify="center")

    # Добавляем строки с контактами
    table.add_row("✨ SpringDao Monad Bot 1.0 ✨")
    table.add_row("─" * 43)
    table.add_row("")
    table.add_row("💬 vx公众号: lszgege77 ")
    table.add_row("👤 telegram:  @keepCalm88")
    table.add_row("SpringDao 欢迎你的加入！")

    # Выводим таблицу с отступом
    print("   ", end="")
    print()
    console.print(table)
    print()