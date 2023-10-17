import paho.mqtt.client as mqtt
import time
import csv
import pandas as pd 

file_path = "Test1.xlsx"

sheet_name = "in"

columns_to_read = ["time", "chrg"]

df = pd.read_excel(file_path, sheet_name=sheet_name)

# Filter the DataFrame to include only the specified columns
selected_columns = df[columns_to_read]


broker_address = "localhost"

topic = "test_test" 

client = mqtt.Client("Publisher")

client.connect(broker_address)
#counter_test = 0;

for index, row in selected_columns.iterrows():
    time_data = row['time']
    chrg_data = row['chrg']
    dataToSend = str(time_data) + ", " + str(chrg_data)
    client.publish(topic, dataToSend)
    time.sleep(.1)

#while True:
    #message = input("Counter: ")
#    client.publish(topic, str(counter_test))

#    counter_test = counter_test + 1
#    if (counter_test == 10):
#        counter_test = 0
#    time.sleep(2)


