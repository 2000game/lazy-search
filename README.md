# python-blueprint

[![GitHub Actions][github-actions-badge]](https://github.com/johnthagen/python-blueprint/actions)
[![Poetry][poetry-badge]](https://python-poetry.org/)
[![Nox][nox-badge]](https://github.com/wntrblm/nox)
[![Code style: Black][black-badge]](https://github.com/psf/black)
[![Ruff][ruff-badge]](https://github.com/astral-sh/ruff)
[![Type checked with mypy][mypy-badge]](https://mypy-lang.org/)

[github-actions-badge]: https://github.com/johnthagen/python-blueprint/workflows/python/badge.svg
[poetry-badge]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json
[nox-badge]: https://img.shields.io/badge/%F0%9F%A6%8A-Nox-D85E00.svg
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[ruff-badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[mypy-badge]: https://www.mypy-lang.org/static/mypy_badge.svg



# Lazy Search

Lazy Search is a command-line application that allows users to search the web for recent news articles on arbitrary topics. The application prompts the user for a topic, searches the web for suitable news articles using the News API, and provides the user with a list of the top 15 matching news articles, a CSV file containing the full list of matching articles, and an automatically generated summary of the article headlines.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/lazy-search.git
   ```

2. Navigate to the project directory:

   ```bash
   cd lazy-search
   ```

3. Install the required dependencies:
Since the project is build with poetry, there is a poetry.lock file that contains all the dependencies. To install the dependencies, run the following command:
   ```bash
   pip install.
   ```

4. Obtain an API key from [News API](https://newsapi.org/) by registering on their website.

5. Store the API key in one of the following ways:

   - Set it as an environment variable named `NEWS_API_KEY`.
   - Create a `.env` file in the project directory and add the following line, replacing `<your-api-key>` with your actual API key:

     ```bash
     NEWS_API_KEY=<your-api-key>
     ```
   - When storing the key inside the `.env` file, you won't be able to use it systemwide. You will have to run the application from the project directory.
   - Alternatively, you can pass the API key directly using the `-k` or `--api-key` option (see below).

## Usage

To search for news articles on a specific topic, use the following command syntax:

```bash
lazy_search "Topic1" "Topic2" "TopicXX"
```

You can also specify the language using the `-l` or `--language` option:

```bash
lazy_search "Topic" -l "en"
```

or

```bash
lazy_search "Topic" --language "en"
```

### API Key

If you haven't stored the API key in the environment variables or a `.env` file, you can pass it directly using the `-k` or `--api-key` option:

```bash
lazy_search "Topic" -k "<your-api-key>"
```

or

```bash
lazy_search "Topic" --api-key "<your-api-key>"
```

### Supported Languages

Lazy Search supports the following languages for searching news articles:

- German: `de`
- English: `en`
- Spanish: `es`
- French: `fr`
- Italian: `it`
- Dutch: `nl`
- Norwegian: `no`
- Portuguese: `pt`
- Russian: `ru`
- Swedish: `se`

## Output

The application will provide the following outputs:

- A list of the top 15 matching news articles, including their titles, URLs, and publication dates, sorted by relevance with respect to the given topic.
- A CSV file named `articles.csv` containing the full list of matching articles, including their titles, URLs, and publication dates. This file is written immediately after the search.
- An automatically generated summary of the top 15 article headlines, along with a list of all named entities mentioned in the headlines, sorted by frequency.

## Example

Here's an example of how to use the Lazy Search application:

```bash
lazy_search "Artificial Intelligence" -l "en"
```

This command will search for recent news articles on the topic of "Artificial Intelligence" in English. The application will then display the top 15 matching articles, write the full list of matching articles to a CSV file, and generate a summary of the article headlines with a list of named entities.


