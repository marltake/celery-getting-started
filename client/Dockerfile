FROM python:3.6
RUN useradd celery
WORKDIR /app
RUN pip install celery redis
COPY . .
CMD ["python", "main.py"]

