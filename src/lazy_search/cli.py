#!/usr/bin/env python3

from typing import Annotated

from rich.console import Console
from typer import Argument, Typer

from lazy_search.lib import factorial

app = Typer(add_completion=False)


@app.command()
def main(topic: Annotated[str, Argument(min=0, help="The topic you want to search for")]) -> None:
    """Search the web for a given topic and generate summary as well as a report of the top 15 articles"""
    print(f"Your topic was: {topic}")


# Allow the script to be run standalone (useful during development).
if __name__ == "__main__":
    app()
