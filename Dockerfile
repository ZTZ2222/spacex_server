FROM python:3.9-slim

WORKDIR /usr/src/spacex/server

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install SQLite package
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Run database migrations before starting the server
RUN python spacex_project/manage.py migrate

CMD ["python", "spacex_project/manage.py", "runserver", "0.0.0.0:8000"]
