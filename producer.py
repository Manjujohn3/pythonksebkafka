from kafka import KafkaProducer
import random
import time

bootstrap_server = ["localhost:9092"]

topic = "kseb"

producer = KafkaProducer(bootstrap_servers = bootstrap_server)

producer = KafkaProducer()

jsonData = {}

def senddata():
    data = random.randint(1,10)
    jsonData = "{'consumerid':2,'unit':"+str(data)+"}"
    message = producer.send(topic, bytes(str(jsonData),"utf-8"))
    print(jsonData)
    metadata = message.get()
    time.sleep(5)

while True:
    senddata() 

