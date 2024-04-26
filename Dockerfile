FROM python:3.11.4

RUN useradd microblog

WORKDIR /home/microblog

COPY app/requirements.txt requirements.txt
RUN python3 -m venv venv
RUN venv/bin/pip install setuptools
RUN venv/bin/python -m pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY microblog.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP microblog.py
ENV DATABASE_URL localhost


RUN chown -R microblog:microblog ./
USER microblog

RUN . venv/bin/activate && flask translate compile

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
