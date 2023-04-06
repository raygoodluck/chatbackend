FROM python:3.10-alpine3.13

RUN mkdir /app
WORKDIR /app

COPY . .
RUN pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple
RUN pip3 install -r requirements.txt


EXPOSE 8000
ENV PYTHONUNBUFFERED=1 
CMD ["python3", "./manage.py", "runserver","0.0.0.0:8000"]
