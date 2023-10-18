import pandas as pd

class ExcelDataReader:
    def __init__(self, file_path, sheet_name, columns_to_read):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.columns_to_read = columns_to_read
        self.df = pd.read_excel(self.file_path, sheet_name=self.sheet_name)

    def filter_columns(self):
        self.selected_columns = self.df[self.columns_to_read]

    def get_time_data(self):
        if hasattr(self, 'selected_columns'):
            return self.selected_columns['time']
        else:
            raise ValueError("Columns not yet filtered. Call filter_columns method first.")

    def get_mv_data(self):
        if hasattr(self, 'selected_columns'):
            return self.selected_columns['mv']
        else:
            raise ValueError("Columns not yet filtered. Call filter_columns method first.")


# file_path = "Test1.xlsx"
# sheet_name = "in"
# columns_to_read = ["time", "mv"]

# data_reader = ExcelDataReader(file_path, sheet_name, columns_to_read)
# data_reader.filter_columns()

# time_data = data_reader.get_time_data()
# mv_data = data_reader.get_mv_data()

# print(time_data)
# print(mv_data)

# totalTime = 0
# totalMV = 0

# for i in range(len(time_data)):


#     totalTime = totalTime + time_data[i]
#     totalMV = totalMV + mv_data[i]

# print("Total time in seconds", totalTime)
# totalTimeHours = totalTime*60*60*(10*10*10*10*10)
# print("total time in hours" , totalTimeHours)
# print("total mv," , totalMV*10*10*10)
# average = totalMV / totalTime
# print("average charge per second in volts," , average)