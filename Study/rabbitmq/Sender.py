import pika
from rabbitmq.RabbitMQ import RabbitMQ


# n RabbitMQ a message can never be sent directly to the queue,it always needs to go through an exchange.

# 简单队列测试
def singleQueueProducerTest(rabbitMQ, queueName, message):
    rabbitMQ.queue_declare(queue_name=queueName, durable=False)
    rabbitMQ.produce(routing_key=queueName, msg=message)
    print("[x]Sent'{0}'".format(message))

# 广播测试
def broadCastQueueTest(rabbitMQ, exchange, message,exchange_type):

    rabbitMQ.exchange_declare(exchange, exchange_type)
    rabbitMQ.produce(
        routing_key='',  # fanout的话为空(默认)
        msg=message,
        exchange=exchange)

if __name__ == '__main__':

    rabbitMQ = RabbitMQ(
        username="admin",
        password="admin",
        host="192.168.110.170")

    while True:
        message = input("message:").strip()
        queueName = "hello1"

        # fanout: 所有bind到此exchange的queue都可以接收消息
        broadCastQueueTest(rabbitMQ, exchange="fanout_logs", message=message,exchange_type='fanout')  # 广播测试

        # singleQueueProducerTest(rabbitMQ, queueName, message)  # 简单队列测试

    rabbitMQ.close()
