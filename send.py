# Source: https://www.rabbitmq.com/tutorials/tutorial-one-python.html

import pika
import time
import os
import sys


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    print("Connecting to RabbitMQ...")

    payload = 'currentGame.json'
    curr_game = open(payload, 'r')

    # listen for file to be populated
    print("Waiting for current game results...")
    while os.stat(payload).st_size == 0:
        time.sleep(5)

    print("Sending request to add current game result...")
    curr_game.close()

    channel.queue_declare(queue='cs361_queue')

    channel.basic_publish(exchange='',
                        routing_key='cs361_queue',
                        body=payload)
    print(" [x] Message sent: ", payload)
    # connection.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)