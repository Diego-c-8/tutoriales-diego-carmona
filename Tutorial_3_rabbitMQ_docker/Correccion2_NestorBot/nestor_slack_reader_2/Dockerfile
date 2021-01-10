FROM python:3.6.3

ENV SLACK_TOKEN			xoxb-1431840442353-1443065462688-o0bI8HFm7gzIRpbA6XQyOPOY
ENV SLACK_SIGNING_SECRET		bef3f652429985e7dcccc37e3a8e964b

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_slack_reader_2

COPY ./nestor_slack_reader_2.py /nestor_slack_reader_2.py

CMD [ "python", "/nestor_slack_reader_2.py" ]
