from __future__ import annotations

import os

from dotenv import load_dotenv
from newsapi import NewsApiClient

from lazy_search.models import ArticleLanguage, NewsRequestModel, NewsResponseModel

load_dotenv()


class NewsFetcher:
    def __init__(self, api_key: str | None = "") -> None:
        if api_key == "":
            api_key = os.environ.get("NEWS_API_KEY")
        self.news_api = NewsApiClient(api_key=api_key)

    def search(
        self, topic: str, language: ArticleLanguage = ArticleLanguage.ENGLISH
    ) -> NewsResponseModel:
        request_model = NewsRequestModel(q=topic, language=language)
        response = self.news_api.get_everything(**dict(request_model))
        return NewsResponseModel(**response)
