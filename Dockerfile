FROM alpine:latest
RUN apk add --update python3 tzdata
RUN apk add --no-cache bash

# Set the timezone
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

# Set up the data directories for the app
COPY . /app
RUN mkdir -p /tmp/reach/logs
RUN touch /tmp/reach/logs/input.log
RUN bash fb_setup.sh

# Run the app
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
