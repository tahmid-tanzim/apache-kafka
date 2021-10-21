from confluent_kafka import Producer
import socket
import random

conf = {
    "bootstrap.servers": "localhost:9092",
    "client.id": socket.gethostname()
}


def acknowledged(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s - %s" % (str(msg.key()), str(msg.value())))


if __name__ == "__main__":
    producer = Producer(conf)
    topic = "kafka.learning.orders"

    for _ in range(10):
        random_float = round(random.uniform(9.9, 999.9), 2)
        print(random_float)
        producer.produce(topic, key=f"KEY-{random_float}", value=f"VALUE-{random_float}", callback=acknowledged)
        # Wait up to 1 second for events. Callbacks will be invoked during
        # this method call if the message is acknowledged.
        producer.poll(1)


