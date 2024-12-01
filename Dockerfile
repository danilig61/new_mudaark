FROM python:3.11-slim-buster as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH=$PATH:/root/.local/bin

RUN apt update -y && apt install libmagic1 -y

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache -r requirements.txt

COPY .env .
COPY start.sh .
RUN chmod +x start.sh
COPY config .

CMD ["bash", "start.sh"]
