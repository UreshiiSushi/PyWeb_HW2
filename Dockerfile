FROM python:alpine3.19

ENV APP /pyweb_hw2

WORKDIR ${APP}

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "main.py" ]