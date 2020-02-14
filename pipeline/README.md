# Streaming pipeline

Kafka publisher / consumer

## websites

https://medium.com/@Ankitthakur/apache-kafka-installation-on-mac-using-homebrew-a367cdefd273 
https://medium.com/@mukeshkumar_46704/consume-json-messages-from-kafka-using-kafka-pythons-deserializer-859f5d39e02c

### Steps

1. `run_kafka.sh`
2. `kafka_commands.sh`
3. `python scripts/run_input_producer.py`
4. `python scripts/run_ml_engine.py`
5. `python scripts/run_output_consumer.py`

Producer console:
```
kafka-console-producer --broker-list localhost:9092 --topic ml-input
kafka-console-producer --broker-list localhost:9092 --topic ml-output
```
Consumer console:
```
kafka-console-consumer --bootstrap-server localhost:9092 --topic ml-input --from-beginning
kafka-console-consumer --bootstrap-server localhost:9092 --topic ml-output --from-beginning
```