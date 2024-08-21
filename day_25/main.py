
def main():
    with open('weather_data.csv', 'r') as weather_file:
        data = []
        for val in weather_file.readlines():
            data.append(val.strip())
    print(data)


if __name__ == "__main__":
    main()
