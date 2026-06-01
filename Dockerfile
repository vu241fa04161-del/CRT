FROM python:3.14

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
run python manage.py collectstatic --noinput

EXPOSE 10000

CMD ["gunicorn","CRT.wsgi:application","--bind","0.0.0.0:10000"]
