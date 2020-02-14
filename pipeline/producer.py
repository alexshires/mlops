"""
Basic Kafka producer
"""

from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(retries=5)

# load test data
data = []

# Asynchronous by default
for data_point in data:
    future = producer.send('ml_input', data_point)
