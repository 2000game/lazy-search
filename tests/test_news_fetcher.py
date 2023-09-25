from datetime import datetime

from lazy_search.news_fetcher import NewsFetcher, NewsModel

fake_news_results = [
    {
        "title": "This 2023 Python Bootcamp Is $10 Right Now",
        "media": "Lifehacker",
        "date": "9 mins ago",
        "datetime": datetime(2023, 9, 25, 16, 40, 18, 571550),
        "desc": "",
        "link": "https://lifehacker.com/this-2023-python-bootcamp-is-10-right-now-1850863052&ved=2ahUKEwjWmpX"
        "-gMaBAxVaSPEDHXTsDYgQxfQBegQIBhAC&usg=AOvVaw3ztPjby09zC7aj89UxeeFJ",
        "img": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",
    },
    {
        "title": "The Python on Hardware Newsletter: subscribe for free #CircuitPython #Python #RaspberryPi "
        "@micropython @ThePSF",
        "media": "Adafruit Blog",
        "date": "1 hour ago",
        "datetime": datetime(2023, 9, 25, 15, 49, 26, 714939),
        "desc": "",
        "link": "https://blog.adafruit.com/2023/09/25/the-python-on-hardware-newsletter-subscribe-for-free"
        "-circuitpython-python-raspberrypi-micropython-thepsf-15/&ved=2ahUKEwjWmpX"
        "-gMaBAxVaSPEDHXTsDYgQxfQBegQICRAC&usg=AOvVaw29EyWjtyZDaaj8phTLUOew",
        "img": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",
    },
]


def test_news_model() -> None:
    fake_data = fake_news_results[0]
    NewsModel(**fake_data)


def test_basic_search() -> None:
    news_fetcher = NewsFetcher()
    results = news_fetcher.search("python")
    assert len(results) > 0
    assert all(isinstance(result, NewsModel) for result in results)
