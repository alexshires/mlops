# create topic
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic ml_input
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic ml_output


