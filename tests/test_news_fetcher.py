import os

import pytest

from lazy_search.models import ArticleModel, NewsResponseModel
from lazy_search.news_fetcher import NewsFetcher
from tests.test_data import fake_news_response


def test_news_article_model() -> None:
    article = fake_news_response["articles"][0]  # type: ignore
    model = ArticleModel(**article)
    assert model.title == article["title"]


def test_news_response_model() -> None:
    model = NewsResponseModel(**fake_news_response)
    assert model.status == "ok"
    assert model.totalResults == 4107
    assert len(model.articles) == 15


@pytest.mark.skipif(not os.environ.get("NEWS_API_KEY"), reason="No API key set")
def test_basic_search() -> None:
    news_fetcher = NewsFetcher()
    results = news_fetcher.search("apple news")
    assert isinstance(results, NewsResponseModel)
