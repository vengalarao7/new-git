FROM python:3.8-slim

WORKDIR /app

ENV OWNER vengalarao

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

