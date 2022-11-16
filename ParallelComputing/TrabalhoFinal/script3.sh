# Stopping the kafka and zookeeper services
systemctl stop kafka
systemctl stop zookeeper

# Opening the server.properties file
vi /opt/kafka_2.13-3.3.1/config/server.properties