# Source: https://www.rabbitmq.com/tutorials/tutorial-one-python.html

import pika, os, sys
import GameSaver

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    print("Connecting to RabbitMQ...")

    channel.queue_declare(queue='cs361_queue')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        GameSaver.saveGame(body.decode())
        print(" [x] Game saved.")
        

    channel.basic_consume(queue='cs361_queue',
                        auto_ack=True,
                        on_message_callback=callback)

    print(' [*] Waiting for messages... To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)