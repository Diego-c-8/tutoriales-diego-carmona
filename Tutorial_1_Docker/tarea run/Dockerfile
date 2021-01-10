FROM python:3.9.1

ENV SLACK_TOKEN         xoxb-1425339281412-1419229594530-YqjkXwqHUjaQ75TCXXWhI85a

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./jamesbot_app.py /jamesbot_app.py

COPY ./jamesbot.py /jamesbot.py

COPY ./jamesbot_test.py /jamesbot_test.py

CMD [ "python", "/jamesbot_test.py"]
