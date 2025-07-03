FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py app.py
COPY ../shared ../shared
CMD ["gunicorn", "-b", "0.0.0.0:5008", "app:app"]
