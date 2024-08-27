import csv

def main():
    # with open('weather_data.csv', 'r') as weather_file:
    #     data = []
    #     for val in weather_file.readlines():
    #         data.append(val.strip())
    # print(data)

    with open('weather_data.csv', 'r')  as data_file:
        data = csv.reader(data_file) # data = list(csv.reader(data_file)) difference?
        print(data)

        for row in data:
            print(row)

if __name__ == "__main__":
    main()
