"""
Output consumer
recieves and publishes messages
"""
from kafka import KafkaConsumer
from pipeline.utils import get_pipeline_config
import logging, json

logger = logging.getLogger(__name__)
config = get_pipeline_config()


def read_output(topic: str = config["topics"]["ml-output"]) -> None:
    """
    read the output and print for a given topic
    :return:
    """
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=["localhost:9092"],
        value_deserializer=lambda m: json.loads(m.decode("ascii")),
    )
    for message in consumer:
        logger.debug(
            "%s:%d:%d: key=%s value=%s",
            message.topic,
            message.partition,
            message.offset,
            message.key,
            message.value,
        )
