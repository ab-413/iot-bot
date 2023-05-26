FROM python:3.10.6-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python3" ]
CMD [ "bot.py" ]