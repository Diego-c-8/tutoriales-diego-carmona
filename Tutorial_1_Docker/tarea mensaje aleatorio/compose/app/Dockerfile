FROM python:3.9.1

ENV SLACK_TOKEN		xoxb-1425339281412-1419229594530-YqjkXwqHUjaQ75TCXXWhI85a
ENV MONGO_HOST          localhost
ENV MONGO_PORT         	"mongodb://mongo:27017/"


COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./astolfobot_app.py /astolfobot_app.py
COPY ./astolfobot.py /astolfobot.py

CMD [ "python", "/astolfobot_app.py"]
