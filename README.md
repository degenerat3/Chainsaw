# Reach
Process callbacks from client tools, parse and send to ELK

## Server
The server is a dockerized flask server with endpoints to receive JSON from various redteam tools.  For now, it will be ScavengerPro and Campfire.  The flask app will take that JSON, parse it into a log file (which will be easier for logstash to process), then use filebeat to ship that log file to our redteam ELK stack.


