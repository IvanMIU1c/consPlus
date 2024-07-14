FROM python:3.10.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFIRED 1

WORKDIR /usr/src/cons_plus

RUN pip install --upgrade pip
RUN apt-get -y update
#RUN apt-get -y install sqlite3
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt
COPY . /usr/src/cons_plus
RUN sed -i 's/\r$//g' /usr/src/cons_plus/entrypoint.sh && chmod +x /usr/src/cons_plus/entrypoint.sh
RUN python3 manage.py

ENTRYPOINT ["/usr/src/cons_plus/entrypoint.sh"]
