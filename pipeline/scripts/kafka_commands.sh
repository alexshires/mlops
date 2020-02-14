# create topic locally
#TODO: link up to global pipeline config
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic ml-input
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic ml-output


