FROM python:3.6.3

ENV SLACK_TOKEN			xoxb-1431840442353-1443065462688-o0bI8HFm7gzIRpbA6XQyOPOY

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /nestor_slack_writer

COPY ./nestor_slack_writer.py /nestor_slack_writer.py
COPY ./nestor_slack_writer.py /nestor_slack_writer.py

CMD [ "python", "/nestor_slack_writer.py" ]
