FROM python:3
ENV PYTHONUNBUFFERED=1
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 8000
CMD exec gunicorn api.wsgi:application --bind 0.0.0.0:8000 --certfile=/etc/letsencrypt/live/nekvinder.com/fullchain.pem --keyfile=/etc/letsencrypt/live/nekvinder.com/privkey.pem --workers 3
