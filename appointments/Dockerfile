FROM python:3.10.13-alpine

LABEL name="Flask Appointments"

# Create app directory
WORKDIR /app

EXPOSE 7070

# ENV MONGO_URL="mongodb://localhost:27017/"
# ENV MONGO_USERNAME="test"
# ENV MONGO_PASSWORD="123"
# testing new version
# testing new version2

RUN pip install flask \
    pip install flask_cors \
    pip install pymongo


COPY app.py ./

CMD [ "python3", "./app.py" ]