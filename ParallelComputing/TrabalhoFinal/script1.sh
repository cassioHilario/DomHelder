yum -y update
yum install java-1.8.0-openjdk
wget https://downloads.apache.org/kafka/3.3.1/kafka_2.13-3.3.1.tgz
tar -xzf kafka_2.13-3.3.1.tgz
mv kafka_2.13-3.3.1 /opt
cd /opt/kafka_2.13-3.3.1
# Adding kafka user
useradd kafka
chown -R kafka:kafka /opt/kafka_2.13-3.3.1

# Creating kafka service and zookeeper service

# Creating kafka service
cat << EOF > /etc/systemd/system/kafka.service
[Unit]  
Description=Apache Kafka  
Requires=zookeeper.service  
After=zookeeper.service   

[Service]  
Type=simple   

User=kafka  
Group=kafka   

ExecStart=/opt/kafka_2.13-3.3.1/bin/kafka-server-start.sh /opt/kafka_2.13-3.3.1/config/server.properties  
ExecStop=/opt/kafka_2.13-3.3.1/bin/kafka-server-stop.sh   

[Install]  
WantedBy=multi-user.target  

EOF

chmod 777 /etc/systemd/system/kafka.service

# Creating zookeeper service
cat << EOF > /etc/systemd/system/zookeeper.service

[Unit]  
Description=zookeeper  
After=syslog.target network.target   

[Service]  
Type=simple   

User=kafka  
Group=kafka   

ExecStart=/opt/kafka_2.13-3.3.1/bin/zookeeper-server-start.sh /opt/kafka_2.13-3.3.1/config/zookeeper.properties  
ExecStop=/opt/kafka_2.13-3.3.1/bin/zookeeper-server-stop.sh   

[Install]  
WantedBy=multi-user.target

EOF

chmod 777 /etc/systemd/system/zookeeper.service

# Editing  /opt/kafka_2.12-3.1.0/bin/kafka-server-start.sh to reduce kafka heap size
sed -i 's/export KAFKA_HEAP_OPTS="-Xmx1G -Xms1G"/export KAFKA_HEAP_OPTS="-Xmx512M -Xms128M"/g' /opt/kafka_2.13-3.3.1/bin/kafka-server-start.sh

# Starting zookeeper and kafka services
systemctl start zookeeper
systemctl start kafka

sleep 5

 # Checking status of zookeeper and kafka services
systemctl status zookeeper
systemctl status kafka

# Creating topic
cd /opt/kafka_2.13-3.3.1/bin
./kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 4 --topic clientes

# Listing topics
./kafka-topics.sh --list --bootstrap-server localhost:9092

# Checking logs
ls -l /tmp/kafka-logs

# Install kafka-python
pip3 install kafka-python
