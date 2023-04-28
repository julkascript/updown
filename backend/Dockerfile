FROM python

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && apt-get install -y postgresql-client

RUN pip install -r requirements.txt

COPY . /app/

RUN chmod 755 startup.sh

ENTRYPOINT ["sh",  "startup.sh"]