# FROM python:3.9-slim-buster

# COPY ./requirements.txt /app/requirements.txt

# WORKDIR /app

# RUN pip install -r requirements.txt

# COPY . /app

# EXPOSE 8080

# # CMD python 'core.py'

# CMD [ "python3", "core.py" ]

# # ENTRYPOINT FLASK_APP=/app/core.py flask run --host=0.0.0.0

FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["core.py"]
