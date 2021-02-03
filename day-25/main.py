# with open("weather_data.csv", "r") as data:
#     cleanedData = []
#
#     for line in data.readlines():
#         newline = line.replace("\n", "")
#         cleanedData.append(newline)
#
#     print(cleanedData)

# import pandas
#
# with open("weather_data.csv", "r") as data:
#     data = csv.reader(data)
#     temps = []
#     i = 0
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#     print(temps)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print((data[data.day == "Monday"].temp * 9/5)+32)

import pandas

data = pandas.read_csv("sqdata.csv")

greySqs = data[data["Primary Fur Color"] == 'Gray']
blackSqs = data[data["Primary Fur Color"] == 'Black']
cinnamonSqs = data[data["Primary Fur Color"] == 'Cinnamon']

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "total": [len(greySqs), len(blackSqs), len(cinnamonSqs)]
}

df = pandas.DataFrame(data_dict)
df.to_csv("count.csv")


