import pika
from rabbitmq.RabbitMQ import RabbitMQ


# n RabbitMQ a message can never be sent directly to the queue,it always needs to go through an exchange.

# 简单队列消费测试
def singleQueueConsumerTest(rabbitMQ, queue_name):
    rabbitMQ.consume(queue_name=queue_name, auto_ack=True)


# 广播测试
def broadCastQueueTest(rabbitMQ, exchange):
    # 不指定queue名字(为了收广播),rabbit会随机分配一个queue名字,
    # exclusive=True会在使用此queue的消费者断开后,自动将queue删除
    result = rabbitMQ.queue_declare(queue_name="", exclusive=True)
    # fanout: 所有bind到此exchange的queue都可以接收消息
    queue_name = result.method.queue
    print("queue_name: ", queue_name)

    # 把声明的queue绑定到交换器exchange上
    rabbitMQ.queue_bind(queue_name=queue_name, exchange=exchange)
    rabbitMQ.consume(queue_name=queue_name, auto_ack=True)


if __name__ == '__main__':
    rabbitMQ = RabbitMQ(
        username="admin",
        password="admin",
        host="192.168.110.170")

    queue_name = "hello1"

    broadCastQueueTest(rabbitMQ, exchange="fanout_logs")  # 广播测试)
    #
    # singleQueueConsumerTest(rabbitMQ,queue_name) # 简答队列消费测试

    rabbitMQ.close()
