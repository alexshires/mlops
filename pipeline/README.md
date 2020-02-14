# Streaming pipeline

Kafka publisher / consumer

## mac 

https://medium.com/@Ankitthakur/apache-kafka-installation-on-mac-using-homebrew-a367cdefd273 

### Steps

1. `run_kafka.sh`
2. `kafka_commands.sh`

Producer console:
```
kafka-console-producer --broker-list localhost:9092 --topic ml_input
kafka-console-producer --broker-list localhost:9092 --topic ml_output
```
Consumer console:
```
kafka-console-consumer --bootstrap-server localhost:9092 --topic ml_input --from-beginning
kafka-console-consumer --bootstrap-server localhost:9092 --topic ml_input --from-beginning
```