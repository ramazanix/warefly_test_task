FROM python:3.10 as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10

WORKDIR /src
COPY --from=requirements-stage /tmp/requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./src/api /src/
COPY ./src/insert_data.py /src
COPY migrations.sh /src

ADD https://github.com/yutkin/Lenta.Ru-News-Dataset/releases/download/v1.1/lenta-ru-news.csv.bz2 data/lenta-ru-news.csv.bz2
RUN bunzip2 /src/data/lenta-ru-news.csv.bz2

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9090"]
