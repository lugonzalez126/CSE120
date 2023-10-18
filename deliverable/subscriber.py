import paho.mqtt.client as mqtt

broker_address = "localhost"

timeTopic = "time"
mvTopic = "mv"
averageTopic = "average"

def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")

client = mqtt.Client("Subscriber")
client.on_message = on_message
client.connect(broker_address)
client.subscribe(timeTopic)
client.subscribe(mvTopic)
client.subscribe(averageTopic)


client.loop_forever()
