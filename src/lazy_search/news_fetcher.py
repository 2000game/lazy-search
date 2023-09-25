from __future__ import annotations

from datetime import datetime

from GoogleNews import GoogleNews
from pydantic import BaseModel


class NewsFetcher:
    def __init__(self) -> None:
        self.google_news = GoogleNews()

    def search(self, topic: str, language: str = "en") -> list[NewsModel]:
        self.google_news.set_lang(language)
        self.google_news.search(topic)
        results = self.google_news.results()
        return [NewsModel(**result) for result in results]


class NewsModel(BaseModel):
    title: str
    media: str
    datetime: datetime
    desc: str
    link: str
