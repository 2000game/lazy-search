from pathlib import Path

from lazy_search.utils import generate_csv


def test_csv_generator(tmp_path: Path) -> None:
    data = [{"name": "John", "age": "28"}, {"name": "Mary", "age": "25"}]
    path = tmp_path / "test.csv"
    generate_csv(data, str(path))

    with Path(path).open() as f:
        assert f.read() == "name,age\nJohn,28\nMary,25\n"
