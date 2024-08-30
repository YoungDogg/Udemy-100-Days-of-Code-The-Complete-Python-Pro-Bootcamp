# import csv
#
# def main():
#     # with open('weather_data.csv', 'r') as weather_file:
#     #     data = []
#     #     for val in weather_file.readlines():
#     #         data.append(val.strip())
#     # print(data)
#
#     with open('weather_data.csv', 'r')  as data_file:
#         data = list(csv.reader(data_file)) # data = list(csv.reader(data_file)) difference?
#         temperatures = []
#
#         for row in data:
#             if not row[1] == 'temp':
#                 temperatures.append(int(row[1]))
#         print(temperatures)
#

import pandas


def main():
    data = pandas.read_csv("weather_data.csv")

    # data_dict = data.to_dict()
    # print(data_dict)

    # temp_list = data["temp"].to_list()
    # print(temp_list)

    avg_temp = 0
    sum_temp = 0
    # for temp in temp_list:
    #     sum_temp += temp
    # avg_temp = sum_temp / len(temp_list)
    # avg_temp = sum(temp_list) / len(temp_list)
    # avg_temp = data["temp"].mean()
    # print(avg_temp)

    # max_temp = data["temp"].max()
    # print(max_temp)
    # print(data.temp)

    # print(data[data.temp == data.temp.max()])

    # monday = data[data.day == "Monday"]
    # print(monday)
    # print(monday.temp[0])
    # to_farenheit = (monday.temp * 9/5) + 32
    # print(to_farenheit[0])

    # create a dataframe from scratch
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    data = pandas.DataFrame(data_dict)
    print(data)
    data.to_csv("new_data.csv")


if __name__ == "__main__":
    main()
