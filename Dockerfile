FROM python:3.10.13-slim

WORKDIR /app

# Copy requirements FIRST for layer caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of code after
COPY . .

CMD ["python", "-m", "server.app"]
