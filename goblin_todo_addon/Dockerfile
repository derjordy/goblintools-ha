FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl unzip wget gnupg && \
    pip install --no-cache-dir playwright flask && \
    playwright install --with-deps chromium

WORKDIR /app
COPY run.py /app/run.py
COPY requirements.txt /app/requirements.txt
COPY options.py /app/options.py

CMD ["python", "run.py"]