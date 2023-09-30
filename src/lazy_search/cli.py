#!/usr/bin/env python3

from typing import Annotated

from rich import print
from rich.console import Console
from rich.table import Table
import typer
from typer import Argument, Typer

from lazy_search.models import ArticleLanguage
from lazy_search.news_fetcher import NewsFetcher
from lazy_search.nlp import NaturalLanguageProcessor, NlpLoader
from lazy_search.utils import generate_csv_from_news_response

app = Typer(add_completion=False)


def validate_langauge_input(language: str) -> str:
    if language not in ArticleLanguage.__members__.values():
        raise UnsupportedLanguageException(language)
    return language


topic_annotation = Annotated[list[str], Argument(min=0, help="The topic you want to search for")]
language_typer_option = typer.Option(
    "en",
    "--language",
    "-l",
    help="The language you want to search for",
    callback=validate_langauge_input,
)
api_key_typer_option = typer.Option("", "--api-key", "-k", help="The api key for the news api")


@app.command()
def main(
    topics: topic_annotation,
    language: str = language_typer_option,
    api_key: str = api_key_typer_option,
) -> None:
    """Search the web for a given topic or multiple and generate summary as well as a report of the top 15 articles"""
    console = Console()

    nlp_loader = NlpLoader()
    if not nlp_loader.is_language_downloaded(ArticleLanguage(language)):
        print(
            "[bold orange_red1][INFO] Language not downloaded, downloading now... [/bold orange_red1]"
        )
    nlp = NaturalLanguageProcessor(language=ArticleLanguage(language))
    news_fetcher = NewsFetcher(api_key=api_key)

    for topic in topics:
        response = news_fetcher.search(topic=topic, language=ArticleLanguage(language))
        articles = response.articles
        table = Table(
            title=f"Articles for topic: {topic}", show_header=True, header_style="bold magenta"
        )
        table.add_column("Title", style="dim")
        table.add_column("Published At", style="dim")
        table.add_column("URL", style="dim")
        for article in articles:
            table.add_row(article.title, article.publishedAt, article.url)
        console.print(table)

        print("[bold orange_red1][INFO] Generating csv... [/bold orange_red1]")
        generate_csv_from_news_response(response, f"{topic}.csv")

        print("[bold orange_red1][INFO] Generating summary... [/bold orange_red1]")
        headlines = [article.title for article in articles]
        summary = nlp.summarize_headlines(headlines)
        print(summary)

        print("[bold orange_red1][INFO] Curating named entities... [/bold orange_red1]")
        named_entities = nlp.get_named_entities(headlines)
        print(named_entities)


class UnsupportedLanguageException(typer.BadParameter):
    def __init__(self, language: str):
        supported_languages = ", ".join(ArticleLanguage.__members__.values())
        message = f"Language '{language}' is not supported. Supported languages are: {supported_languages}"
        super().__init__(message)


# Allow the script to be run standalone (useful during development).
if __name__ == "__main__":
    app()
