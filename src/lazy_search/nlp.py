from __future__ import annotations

from collections import Counter
from heapq import nlargest
import importlib
from string import punctuation

import spacy
from spacy.cli import download  # type: ignore
from spacy.language import Language

from lazy_search.models import ArticleLanguage, LanguageModels


class NlpLoader:
    @staticmethod
    def get_model_name(language: ArticleLanguage) -> str:
        return LanguageModels[language]

    def is_language_downloaded(self, language: ArticleLanguage) -> bool:
        model_name = self.get_model_name(language)
        return model_name in spacy.util.get_installed_models()

    def load_model(self, language: ArticleLanguage) -> Language:
        model_name = self.get_model_name(language)
        try:
            model_module = importlib.import_module(model_name)
        except ModuleNotFoundError:
            download(model_name)
            model_module = importlib.import_module(model_name)
        nlp: Language = model_module.load()
        return nlp


class NaturalLanguageProcessor:
    def __init__(self, language: ArticleLanguage = ArticleLanguage.ENGLISH) -> None:
        self.nlp_loader = NlpLoader()
        self.nlp: Language = Language()
        self.change_language(language)

    def change_language(self, language: ArticleLanguage) -> None:
        self.nlp = self.nlp_loader.load_model(language=language)

    def summarize_text(self, text: str) -> str:
        doc = self.nlp(text)
        freq_of_word: dict[str, int] = {}

        for token_word in doc:
            if (
                token_word.text.lower() not in list(self.nlp.Defaults.stop_words)
                and token_word.text.lower() not in punctuation
            ):
                if token_word.text not in freq_of_word:
                    freq_of_word[token_word.text] = 1
                else:
                    freq_of_word[token_word.text] += 1

        max_freq = max(freq_of_word.values())
        normalized_freq_of_word: dict[str, float] = {}
        for word in freq_of_word:
            normalized_freq_of_word[word] = freq_of_word[word] / max_freq

        sent_tokens = list(doc.sents)
        sent_scores = {}
        for sent in sent_tokens:
            for token_word in sent:
                if token_word.text.lower() in normalized_freq_of_word:
                    if sent not in sent_scores:
                        sent_scores[sent] = normalized_freq_of_word[token_word.text.lower()]
                    else:
                        sent_scores[sent] += normalized_freq_of_word[token_word.text.lower()]

        len_tokens = int(len(sent_tokens) * 0.2)

        summary = nlargest(n=len_tokens, iterable=sent_scores, key=sent_scores.get)  # type: ignore

        final_summary = [word.text for word in summary]

        summary_str = " ".join(final_summary)

        return summary_str

    @staticmethod
    def format_headlines(headlines: list[str]) -> str:
        formatted_headlines = []
        for headline in headlines:
            if headline[-1] not in punctuation:
                new_headline = headline + "."
                formatted_headlines.append(new_headline)
            else:
                formatted_headlines.append(headline)

        text = " ".join(formatted_headlines)
        return text

    def summarize_headlines(self, headlines: list[str]) -> str:
        text = self.format_headlines(headlines)
        summary = self.summarize_text(text)
        return summary

    def get_named_entities(self, headlines: list[str]) -> dict[str, int]:
        text = self.format_headlines(headlines)
        return self.count_entities(text)

    def count_entities(self, text: str) -> dict[str, int]:
        doc = self.nlp(text)
        named_entities = [ent.text for ent in doc.ents]
        entity_frequency = Counter(named_entities)
        sorted_entities = sorted(entity_frequency.items(), key=lambda x: x[1], reverse=True)
        return dict(sorted_entities)
