# Chainsaw
Process callbacks from client tools, parse and send to ELK

## Server
The server is a dockerized flask server with endpoints to receive JSON from various redteam tools.  For now, it will be ScavengerPro and Campfire.  The flask app will take that JSON, parse it into a log file (which will be easier for logstash to process), then use filebeat to ship that log file to our redteam ELK stack.

## Environment Variables
You can set the following environment variables to change the way that REACH will act

- `FLASK_HOST` The IP that Flask will listen on. Defaults to `0.0.0.0`
- `FLASK_PORT` The port that Flask will listen on. Defaults to `5000`
- `FLASK_DEBUG` Whether or not Flask should run in Debug mode. Defaults to True
- `SYSLOG_HOST` The syslog host to send the logs to
- `SYSLOG_PORT` The syslog port to send the logs to
- `LOGFILE` If not using syslog, write the logs to this file
