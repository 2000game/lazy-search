from __future__ import annotations

import csv
from pathlib import Path

from lazy_search.models import NewsResponseModel


def generate_csv(data: list[dict[str, str]], filename: str) -> None:
    with Path(filename).open("w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def generate_csv_from_news_response(news_response: NewsResponseModel, filename: str) -> None:
    articles = news_response.articles
    articles_data = [dict(article) for article in articles]
    generate_csv(articles_data, filename)
