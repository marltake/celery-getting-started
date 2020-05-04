FROM python:3.6
RUN useradd celery
WORKDIR /app
RUN pip install celery redis
COPY . .
CMD ["celery", "-A", "proj", "worker", "-l", "info", "--uid", "celery"]

