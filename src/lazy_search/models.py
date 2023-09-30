from __future__ import annotations

from enum import Enum

from pydantic import BaseModel


class ArticleLanguage(str, Enum):
    GERMAN = "de"
    ENGLISH = "en"
    SPANISH = "es"
    FRENCH = "fr"
    ITALIAN = "it"
    DUTCH = "nl"
    NORWEGIAN = "no"
    PORTUGUESE = "pt"
    RUSSIAN = "ru"
    SWEDISH = "se"


LanguageModels = {
    ArticleLanguage.GERMAN: "de_core_news_sm",
    ArticleLanguage.ENGLISH: "en_core_web_sm",
    ArticleLanguage.SPANISH: "es_core_news_sm",
    ArticleLanguage.FRENCH: "fr_core_news_sm",
    ArticleLanguage.ITALIAN: "it_core_news_sm",
    ArticleLanguage.DUTCH: "nl_core_news_sm",
    ArticleLanguage.NORWEGIAN: "nb_core_news_sm",
    ArticleLanguage.PORTUGUESE: "pt_core_news_sm",
    ArticleLanguage.RUSSIAN: "ru_core_news_sm",
    ArticleLanguage.SWEDISH: "sv_core_news_sm",
}


class NewsRequestModel(BaseModel):
    q: str
    language: str = "en"
    sort_by: str = "relevancy"
    page_size: int = 15


class ArticleModel(BaseModel):
    title: str
    url: str
    publishedAt: str  # noqa: N815


class NewsResponseModel(BaseModel):
    status: str
    totalResults: int  # noqa: N815
    articles: list[ArticleModel]
