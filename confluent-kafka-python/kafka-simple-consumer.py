from confluent_kafka import Consumer, KafkaError, KafkaException
import sys


def commit_completed(err, partitions):
    if err:
        print(str(err))
    else:
        print("Committed partition offsets: " + str(partitions))


conf = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "sample.consumer.foo",
    "enable.auto.commit": False,
    "auto.offset.reset": "earliest",
    "on_commit": commit_completed
}

running = True


def consume_loop(consumerObj, topics):
    try:
        consumerObj.subscribe(topics)

        while running:
            msg = consumerObj.poll(timeout=1.0)
            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                consumerObj.commit(asynchronous=False)
                # msg_process(msg)
                print("Start processing message - ", str(msg), msg.key(), msg.value())

    finally:
        # Close down consumer to commit final offsets.
        consumerObj.close()


def basic_consume_loop(consumerObj, topics):
    try:
        consumerObj.subscribe(topics)

        while running:
            msg = consumerObj.poll(timeout=1.0)
            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write("%% %s [%d] reached end at offset %d\n" %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                # msg_process(msg)
                print("Start processing message - ", str(msg), msg.key(), msg.value())
    finally:
        # Close down consumer to commit final offsets.
        consumerObj.close()


def shutdown():
    running = False


if __name__ == "__main__":
    consumer = Consumer(conf)
    topic = "kafka.learning.orders"
    basic_consume_loop(consumer, [topic])
