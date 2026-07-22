FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir flask pillow gunicorn

COPY app.py /app/app.py

USER 65534:65534

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--timeout", "30", "app:app"]
