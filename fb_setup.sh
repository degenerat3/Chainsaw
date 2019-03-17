# setup filebeat

curl -L -O "https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.6.2-linux-x86_64.tar.gz"
tar xzf filebeat-6.6.2-linux-x86_64.tar.gz

cd filebeat-6.6.2-linux-x86_64

read -r -d '' CONF << EOM
# Very Minimal Config for Reach FileBeat

name: "Reach"

#====== Filebeat Inputs ======
filebeat.inputs:
 - type: log
   enabled: true
   paths:
    - /tmp/reach/logs/input.log

#====== Kibana ======
setup.kibana:
 hosts: ["127.0.0.1:5601"]		# <--- KIBANA IP

#====== Logstash Output ======
output.logstash:
 hosts: "127.0.0.1:5044"		# <--- LOGSTASH IP
 #SSL stuff will go here if we implement it

logging.level: info
logg.to_files: true
logging.files:
 path: /var/log/filebeat
 name: filebeat
 keepfiles: 10
 permissions: 0644
EOM

echo "$CONF" > filebeat.yml

