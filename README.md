# Apache Kafka

### Launch Kafka & Zookeeper Container
```shell
docker-compose -f kafka-single-node.yml up -d
```
### Logging into the Kafka Container
```shell
docker exec -it kafka-broker /bin/bash
cd /opt/bitnami/kafka/bin
```
### Creating new Topics
```shell
./kafka-topics.sh \
  --bootstrap-server localhost:29092 \
  --create \
  --topic kafka.learning.tweets \
  --partitions 1 \
  --replication-factor 1

./kafka-topics.sh \
  --bootstrap-server localhost:29092 \
  --create \
  --topic kafka.learning.alerts \
  --partitions 1 \
  --replication-factor 1
```
### Listing Topics
```shell
./kafka-topics.sh \
  --bootstrap-server localhost:29092 \
  --list
```
### Getting details about a Topic
```shell
./kafka-topics.sh \
  --bootstrap-server localhost:29092 \
  --describe
```
### Publishing Messages to Topics
```shell
./kafka-console-producer.sh \
  --bootstrap-server localhost:29092 \
  --topic kafka.learning.tweets
```
### Consuming Messages from Topics
```shell
./kafka-console-consumer.sh \
  --bootstrap-server localhost:29092 \
  --topic kafka.learning.tweets \
  --from-beginning
```
### Deleting Topics
```shell
./kafka-topics.sh \
  --bootstrap-server localhost:29092 \
  --delete \
  --topic kafka.learning.alerts
```
### Kafka Setup
```shell
docker exec -it zookeeper /bin/bash
cd /opt/bitnami/zookeeper/bin
./zkCli.sh
```

* Each topic can have 1-n partitions.
* Partitions allow kafka to scale.
* Partitions have separate log file.
* Each Partition has a Leader broker.
* Enables consumers to share workloads through consumer groups.
* Partitions can be replicated.