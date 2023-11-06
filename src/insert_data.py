from datetime import datetime
from clickhouse_driver import Client
from csv import DictReader


def iter_csv(filename: str):
    converters = {'date': lambda x: datetime.strptime(x, '%Y/%m/%d')}

    with open(filename, 'r') as f:
        reader = DictReader(f)
        for line in reader:
            yield {k: converters[k](v) if k in converters else v for k, v in line.items()}


if __name__ == '__main__':
    settings = {'input_format_null_as_default': True}
    client = Client('localhost', settings=settings)
    client.execute(
        'CREATE TABLE IF NOT EXISTS news '
            '('
                'url String, '
                'title String, '
                'text String, '
                'topic String, '
                'tags String, '
                'date Date'
           ') Engine = MergeTree ORDER BY date'
    )
    client.execute('INSERT INTO news VALUES', iter_csv('/src/data/lenta-ru-news.csv'))
