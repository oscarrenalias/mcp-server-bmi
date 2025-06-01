# syntax=docker/dockerfile:1
FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir uv && \
    uv sync

CMD ["uv", "run", "bmi_server.py"]
