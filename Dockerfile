FROM python:3.12

RUN mkdir /blog

WORKDIR /blog

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /blog/docker/*.sh

CMD ["gunicorn", "src.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]
