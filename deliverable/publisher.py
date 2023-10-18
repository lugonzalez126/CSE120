import paho.mqtt.client as mqtt
import time
import csv
import pandas as pd 

from averageClass import ExcelDataReader
file_path = "Test1.xlsx"

sheet_name = "in"

columns_to_read = ["time", "mv"]

df = pd.read_excel(file_path, sheet_name=sheet_name)

# Filter the DataFrame to include only the specified columns
selected_columns = df[columns_to_read]


broker_address = "localhost"

timeTopic = "time" 
mvTopic = "mv"
averageTopic = "average"

client = mqtt.Client("Publisher")

client.connect(broker_address)
#counter_test = 0;

data_reader = ExcelDataReader(file_path, sheet_name, columns_to_read)
data_reader.filter_columns()

time_data = data_reader.get_time_data()
mv_data = data_reader.get_mv_data()

print(time_data)
print(mv_data)

totalTime = 0
totalMV = 0

for i in range(len(time_data)):


    totalTime = totalTime + time_data[i]
    totalMV = totalMV + mv_data[i]

average = totalMV / totalTime
client.publish(averageTopic, average)

for index, row in selected_columns.iterrows():
    time_data = row['time']
    mvData = row['mv']

    client.publish(timeTopic, time_data)
    client.publish(mvTopic, mvData)
    time.sleep(.1)

#while True:
    #message = input("Counter: ")
#    client.publish(topic, str(counter_test))

#    counter_test = counter_test + 1
#    if (counter_test == 10):
#        counter_test = 0
#    time.sleep(2)


