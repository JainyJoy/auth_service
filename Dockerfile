FROM python:3.10-slim-bullseye
WORKDIR /auth-service
RUN apt update -y && apt upgrade -y
RUN apt install -y curl nano vim git
COPY ./requirements.txt /auth-service/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /auth-service/requirements.txt
COPY . /auth-service/
ARG HOST="0.0.0.0"
ENV APP_HOST=$HOST
ARG PORT=8000
ENV PORT_NUMBER=$PORT
EXPOSE $PORT_NUMBER
ARG DEBUG=False
ENV DEBUG_MODE=$DEBUG
ARG JWT_SECRET_KEY
ARG DB_PATH
ENV JWT_SECRET_KEY=$JWT_SECRET_KEY
ENV DB_PATH=$DB_PATH
CMD python run_app.py
