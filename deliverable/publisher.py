import paho.mqtt.client as mqtt
import time
import csv
import pandas as pd 

from averageClass import ExcelDataReader
file_path = "changed_dataLog_Doogie_220815_175620.xlsx"

sheet_name = "dataLog_Doogie_220815_175620"

columns_to_read = ["SecondsSinceEpoch  (seconds)", "BatteryStateOfCharge  (instantaneous, percent)"]

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

print(type(time_data))
print(type(mv_data))

time_data = time_data.astype(int)
mv_data = mv_data.astype(int)
print(type(time_data[0]))
print(type(mv_data[0]))

totalTime = 0
totalMV = 0
totalTimeInt = []
totalMVInt = []
for i in range(len(time_data)):
    totalTime = totalTime + time_data[i]
    totalMV = totalMV + mv_data[i]
    
    totalTimeInt[i] = time_data[i].astype(int)
    totalMVInt[i] = mv_data[i].astype(int)

print(type(totalTimeInt))
print(type(totalMVInt))

for i in range(len(time_data)):

    client.publish(timeTopic, totalMVInt[i])
    client.publish(mvTopic, totalMVInt[i])

average = totalMV / totalTime
client.publish(averageTopic, average)


# for index, row in selected_columns.iterrows():
#     time_data = row['SecondsSinceEpoch  (seconds)']
#     mvData = row['BatteryStateOfCharge  (instantaneous, percent)']

#     client.publish(timeTopic, time_data)
#     client.publish(mvTopic, mvData)
#     time.sleep(.1)

