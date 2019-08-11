import pika


class RabbitMQ(object):

    def __init__(self, username, password, host, port=5672):
        self.host = str(host)
        self.port = int(port)
        self.crt = pika.PlainCredentials(username, password)
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(host=self.host,
                                                                      port=self.port, credentials=self.crt))
        self.channel = self.conn.channel()

    def queue_declare(self, queue_name, durable=False, exclusive=False):
        queue = self.channel.queue_declare(queue=queue_name,
                                           durable=durable,
                                           exclusive=exclusive)
        return queue

    def queue_bind(self, queue_name, exchange):
        self.channel.queue_bind(queue=queue_name, exchange=exchange)

    def exchange_declare(self, exchange='logs', exchange_type='direct'):
        exchange = self.channel.exchange_declare(
            exchange,
            exchange_type)

    def produce(self, routing_key, msg, exchange=''):
        self.channel.basic_publish(exchange=exchange,
                                   routing_key=routing_key,
                                   body=msg,
                                   properties=pika.BasicProperties(
                                       delivery_mode=2  # make message persistent
                                   ))

    def set_qos(self):
        self.channel.basic_qos(prefetch_count=1)

    def callback(cls, ch, method, properties, body):
        print(" [x] Received %r " % body)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def consume(self, queue_name, callback=None, auto_ack=False):
        if callback == None:
            self.channel.basic_consume(
                queue=queue_name,
                on_message_callback=self.callback,
                auto_ack=False)
        else:
            self.channel.basic_consume(
                queue=queue_name,
                on_message_callback=callback,
                auto_ack=auto_ack)
        self.channel.start_consuming()

        def msg_count(self, queue_name, is_durable=True):
            queue = self.channel.queue_declare(queue=queue_name, durable=is_durable)
            count = queue.method.message_count
            return count

        def close(self):
            self.conn.close()
