FROM python:3.6

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY manage.py .
COPY polityper/ ./polityper/
COPY teams/ ./teams/

COPY docker-entrypoint.sh .
CMD ["/bin/bash", "docker-entrypoint.sh"]