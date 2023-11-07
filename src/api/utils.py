from clickhouse_driver import Client


client = Client('clickhouse-server')


def get_popular_words() -> list[dict[str, str | int]]:
    result = []
    data, columns = client.execute("select arrayJoin(splitByChar(' ', replaceRegexpAll(text, '[.,]', ' '))) as word, count() as count "
                                   "from (select text from news) group by word order by count desc limit 1, 100",
                                   with_column_types=True)

    columns = [col[0] for col in columns]
    for row in data:
        json = dict(zip(columns, [value for value in row]))
        result.append(json)

    return result
