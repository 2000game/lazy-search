from __future__ import annotations

from lazy_search.models import ArticleLanguage
from lazy_search.nlp import NaturalLanguageProcessor, NlpLoader


class TestNlpLoader:
    def test_get_model_name(self) -> None:
        nlp_loader = NlpLoader()
        assert nlp_loader.get_model_name(ArticleLanguage.ENGLISH) == "en_core_web_sm"

    def test_is_language_downloaded(self) -> None:
        nlp_loader = NlpLoader()
        assert nlp_loader.is_language_downloaded(ArticleLanguage.ENGLISH) is True
        assert nlp_loader.is_language_downloaded(ArticleLanguage.RUSSIAN) is False

    def test_load_model(self) -> None:
        nlp_loader = NlpLoader()
        nlp = nlp_loader.load_model(ArticleLanguage.ENGLISH)
        assert nlp is not None


class TestNaturalLanguageProcessor:
    def test_change_language(self) -> None:
        nlp = NaturalLanguageProcessor(language=ArticleLanguage.ENGLISH)
        assert nlp.nlp.lang == "en"
        nlp.change_language(ArticleLanguage.GERMAN)
        assert nlp.nlp.lang == "de"

    def test_format_headlines(self) -> None:
        nlp = NaturalLanguageProcessor(language=ArticleLanguage.ENGLISH)
        headlines = ["This is a headline", "This is another headline"]
        formatted_headlines = nlp.format_headlines(headlines)
        assert formatted_headlines == "This is a headline. This is another headline."
