"""
Consumer for scoring
1. reads from 'ml-input' topic
2. calls Seldon API
3. writes results to 'ml-output' topic
"""

from kafka import KafkaProducer, KafkaConsumer
from pipeline.utils import get_pipeline_config, construct_api
import logging
import json

logger = logging.getLogger(__name__)
config = get_pipeline_config()


def score_data(data_point):
    """
    score the data
    :param data_point: JSON of data
    :return:
    """
    # TODO: implement scoring
    model_api = config["apis"]["model"]
    api_url = construct_api(model_api)
    logger.debug("calling API: %s", api_url)
    data_result = data_point
    logger.debug("input: %s, result: %s", data_point, data_result)
    return data_result


if __name__ == "__main__":
    logger.debug("running ML engine")
    # set up consumer
    input_topic = config["topics"]["ml-input"]
    output_topic = config["topics"]["ml-output"]
    producer = KafkaProducer(retries=5)
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
        # score message
        data_result = score_data(data_point=message.value)
        # send downstream (1-1 logic here)
        try:
            future = producer.send(output_topic, data_result)
        except:  # TODO: improve
            logger.error("data send failed: %s, %s", output_topic, data_result)
